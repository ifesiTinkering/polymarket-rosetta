"""
AWS Lambda function to proxy Polymarket API requests
This eliminates CORS issues and provides faster responses
"""

import json
import urllib.request
import urllib.error


def lambda_handler(event, context):
    """
    Handle API Gateway requests and proxy to Polymarket API

    Expected query parameter: path (e.g., /events/23246)
    """

    try:
        # Get the path from query parameters
        query_params = event.get('queryStringParameters', {})

        if not query_params or 'path' not in query_params:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    'error': 'Missing required parameter: path'
                })
            }

        path = query_params['path']

        # Build the Polymarket API URL
        base_url = 'https://gamma-api.polymarket.com'
        url = f"{base_url}{path}"

        # Fetch from Polymarket API
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()

        # Return the response
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
                'Cache-Control': 'public, max-age=300'  # Cache for 5 minutes
            },
            'body': data.decode('utf-8')
        }

    except urllib.error.HTTPError as e:
        return {
            'statusCode': e.code,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': f'API request failed: {e.reason}'
            })
        }

    except urllib.error.URLError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': f'Network error: {str(e.reason)}'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': f'Internal server error: {str(e)}'
            })
        }


# For OPTIONS requests (CORS preflight)
def handle_options(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': ''
    }
