# AWS Lambda Setup Guide

This guide will help you deploy a Lambda function to proxy Polymarket API requests, eliminating CORS issues and providing much faster performance.

## Prerequisites

- AWS Account
- AWS CLI installed (optional, but helpful)

## Step 1: Create Lambda Function

1. Go to [AWS Lambda Console](https://console.aws.amazon.com/lambda/)
2. Click **Create function**
3. Choose **Author from scratch**
4. Configure:
   - **Function name**: `polymarket-proxy`
   - **Runtime**: Python 3.12 (or latest Python 3.x)
   - **Architecture**: x86_64
5. Click **Create function**

## Step 2: Add Function Code

1. In the Lambda function page, scroll to **Code source**
2. Delete the default code
3. Copy and paste the entire contents of `lambda_function.py` from this repository
4. Click **Deploy**

## Step 3: Create API Gateway

1. In the Lambda function page, click **Add trigger**
2. Select **API Gateway**
3. Configure:
   - **Create a new API**
   - **API type**: HTTP API (cheaper and simpler)
   - **Security**: Open (no auth needed for public API)
4. Click **Add**

## Step 4: Get Your API URL

1. After creating the trigger, you'll see it under **Function overview**
2. Click on the API Gateway trigger to expand details
3. Copy the **API endpoint** URL
   - It will look like: `https://abc123xyz.execute-api.us-east-1.amazonaws.com/default/polymarket-proxy`

## Step 5: Update Your Frontend

Now update `index.html` to use your Lambda function:

```javascript
// Replace this:
const BASE_URL = 'https://gamma-api.polymarket.com';

function proxyUrl(url) {
    return `https://api.allorigins.win/raw?url=${encodeURIComponent(url)}`;
}

// With this:
const LAMBDA_URL = 'YOUR-API-GATEWAY-URL-HERE';  // Paste your API Gateway URL

function proxyUrl(url) {
    const path = url.replace('https://gamma-api.polymarket.com', '');
    return `${LAMBDA_URL}?path=${encodeURIComponent(path)}`;
}
```

## Step 6: Test Your Lambda

Test with curl:

```bash
# Test event lookup
curl "YOUR-LAMBDA-URL?path=/events/23246"

# Test market lookup
curl "YOUR-LAMBDA-URL?path=/markets/551142"
```

You should see valid JSON responses.

## Step 7: Deploy to GitHub Pages

1. Update `index.html` with your Lambda URL
2. Commit and push:
   ```bash
   git add index.html
   git commit -m "Switch to AWS Lambda backend for reliable API access"
   git push
   ```

3. Wait 2-3 minutes for GitHub Pages to rebuild

## Expected Performance

- **Before (CORS proxy)**: 2-4 seconds
- **After (Lambda)**: 0.5-1 second (3-5x faster!)
- **Cost**: Free tier covers 1M requests/month

## Optional: Add CloudFront CDN

For even better global performance:

1. Go to [CloudFront Console](https://console.aws.amazon.com/cloudfront/)
2. Create a distribution pointing to your API Gateway
3. Update frontend to use CloudFront URL instead

This adds edge caching worldwide.

## Troubleshooting

### CORS Errors
Make sure Lambda returns these headers:
```python
'Access-Control-Allow-Origin': '*'
```

### Timeout Errors
Increase Lambda timeout:
1. Go to **Configuration** → **General configuration**
2. Set **Timeout** to 30 seconds
3. Save

### Test Failed
Check CloudWatch Logs:
1. Go to **Monitor** → **View CloudWatch logs**
2. Look for error messages

## Cost Estimate

**AWS Lambda**:
- Free tier: 1M requests/month
- After free tier: $0.20 per 1M requests

**API Gateway**:
- Free tier: 1M requests/month
- After free tier: $1.00 per 1M requests

**Total**: Free for most use cases (unless you get 1M+ lookups/month)

## Security Notes

- This Lambda is public (no authentication)
- It only proxies GET requests to Polymarket API
- No sensitive data is stored or logged
- Rate limiting is handled by AWS automatically

## Next Steps

Once your Lambda is working:
1. The cache versioning in the frontend will automatically clear old proxy data
2. Users will experience much faster lookups
3. No more CORS proxy failures

---

**Questions?** Open an issue on GitHub or check AWS Lambda documentation.
