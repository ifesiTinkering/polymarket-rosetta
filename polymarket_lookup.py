#!/usr/bin/env python3
"""
Polymarket ID Lookup Tool
Converts between different Polymarket identifiers (slugs, IDs, condition IDs, etc.)
"""

# Import libraries
import httpx      # For making HTTP requests to the Polymarket API (modern alternative to requests)
import click      # For creating the command-line interface
from typing import Optional, Dict, Any  # For type hints
import json      # For parsing token IDs (stored as JSON strings in API response)


# Base URL for the Polymarket Gamma API
BASE_URL = "https://gamma-api.polymarket.com"


def fetch_event_by_slug(slug: str) -> Optional[Dict[Any, Any]]:
    """
    Fetch event data by slug from Polymarket API

    Args:
        slug: Event slug (e.g., 'new-york-city-mayoral-election')

    Returns:
        Event data dictionary or None if not found
    """
    # Build the API endpoint URL with the slug as a query parameter
    # Example: https://gamma-api.polymarket.com/events?slug=new-york-city-mayoral-election
    url = f"{BASE_URL}/events?slug={slug}"

    try:
        # Make HTTP GET request to the API with a 10 second timeout
        response = httpx.get(url, timeout=10)

        # Raise an exception if the request failed (404, 500, etc.)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        data = response.json()

        # The API returns an array of events, even though we only expect one match
        # Check if we got results and return the first event
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        return None

    except httpx.HTTPError as e:
        # If anything goes wrong (network error, timeout, 404, etc.), print error and return None
        click.echo(f"Error fetching data: {e}", err=True)
        return None


def fetch_event_by_id(event_id: str) -> Optional[Dict[Any, Any]]:
    """
    Fetch event data by event ID from Polymarket API

    Args:
        event_id: Event ID (e.g., '12345')

    Returns:
        Event data dictionary or None if not found
    """
    # Build the API endpoint URL with the event ID in the path
    # Example: https://gamma-api.polymarket.com/events/12345
    url = f"{BASE_URL}/events/{event_id}"

    try:
        # Make HTTP GET request to the API with a 10 second timeout
        response = httpx.get(url, timeout=10)

        # Raise an exception if the request failed (404, 500, etc.)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        # Unlike the slug endpoint, this returns a single event object (not an array)
        data = response.json()

        return data

    except httpx.HTTPError as e:
        # If anything goes wrong (network error, timeout, 404, etc.), print error and return None
        click.echo(f"Error fetching data: {e}", err=True)
        return None


def fetch_market_by_slug(slug: str) -> Optional[Dict[Any, Any]]:
    """
    Fetch market data by slug from Polymarket API

    Args:
        slug: Market slug (e.g., 'will-steve-sweeney-win-the-new-jersey-governor-election-in-2025')

    Returns:
        Market data dictionary or None if not found
    """
    # Build the API endpoint URL with the slug as a query parameter
    # Example: https://gamma-api.polymarket.com/markets?slug=will-steve-sweeney-win-...
    url = f"{BASE_URL}/markets?slug={slug}"

    try:
        # Make HTTP GET request to the API with a 10 second timeout
        response = httpx.get(url, timeout=10)

        # Raise an exception if the request failed (404, 500, etc.)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        data = response.json()

        # The API returns an array of markets, even though we only expect one match
        # Check if we got results and return the first market
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        return None

    except httpx.HTTPError as e:
        # If anything goes wrong (network error, timeout, 404, etc.), print error and return None
        click.echo(f"Error fetching data: {e}", err=True)
        return None


def fetch_market_by_id(market_id: str) -> Optional[Dict[Any, Any]]:
    """
    Fetch market data by market ID from Polymarket API

    Args:
        market_id: Market ID (e.g., '551142')

    Returns:
        Market data dictionary or None if not found
    """
    # Build the API endpoint URL with the market ID in the path
    # Example: https://gamma-api.polymarket.com/markets/551142
    url = f"{BASE_URL}/markets/{market_id}"

    try:
        # Make HTTP GET request to the API with a 10 second timeout
        response = httpx.get(url, timeout=10)

        # Raise an exception if the request failed (404, 500, etc.)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        # Unlike the slug endpoint, this returns a single market object (not an array)
        data = response.json()

        return data

    except httpx.HTTPError as e:
        # If anything goes wrong (network error, timeout, 404, etc.), print error and return None
        click.echo(f"Error fetching data: {e}", err=True)
        return None


def fetch_market_by_token_id(token_id: str) -> Optional[Dict[Any, Any]]:
    """
    Fetch market data by token ID from Polymarket API

    Args:
        token_id: Token ID (e.g., '16867679388416061053995436140492438650416184687930130083732571696309100575009')

    Returns:
        Market data dictionary or None if not found
    """
    # Build the API endpoint URL with the token ID as a query parameter
    # Note: clob_token_ids is the correct parameter name (with underscores)
    # Example: https://gamma-api.polymarket.com/markets?clob_token_ids=16867679388...
    url = f"{BASE_URL}/markets?clob_token_ids={token_id}"

    try:
        # Make HTTP GET request to the API with a 10 second timeout
        response = httpx.get(url, timeout=10)

        # Raise an exception if the request failed (404, 500, etc.)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        data = response.json()

        # The API returns an array of markets, even though we only expect one match
        # Check if we got results and return the first market
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        return None

    except httpx.HTTPError as e:
        # If anything goes wrong (network error, timeout, 404, etc.), print error and return None
        click.echo(f"Error fetching data: {e}", err=True)
        return None


def fetch_market_by_question_id(question_id: str) -> Optional[Dict[Any, Any]]:
    """
    Fetch market data by question ID from Polymarket API

    Args:
        question_id: Question ID (e.g., '0x5ddb6cc9bcce2d9d810ef66a6ee394f91ecf28b7caa4e405036af1916b26e805')

    Returns:
        Market data dictionary or None if not found
    """
    # Build the API endpoint URL with the question ID as a query parameter
    # Example: https://gamma-api.polymarket.com/markets?question_ids=0x5ddb6cc9...
    url = f"{BASE_URL}/markets?question_ids={question_id}"

    try:
        # Make HTTP GET request to the API with a 10 second timeout
        response = httpx.get(url, timeout=10)

        # Raise an exception if the request failed (404, 500, etc.)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        data = response.json()

        # The API returns an array of markets, even though we only expect one match
        # Check if we got results and return the first market
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        return None

    except httpx.HTTPError as e:
        # If anything goes wrong (network error, timeout, 404, etc.), print error and return None
        click.echo(f"Error fetching data: {e}", err=True)
        return None


def fetch_market_by_condition_id(condition_id: str) -> Optional[Dict[Any, Any]]:
    """
    Fetch market data by condition ID from Polymarket API

    Args:
        condition_id: Condition ID (e.g., '0x201df9b6a68bab220392ca4cd18cf4d8c96b7612568777626292d2fb08954efe')

    Returns:
        Market data dictionary or None if not found
    """
    # Build the API endpoint URL with the condition ID as a query parameter
    # Example: https://gamma-api.polymarket.com/markets?condition_ids=0x201df9b6...
    url = f"{BASE_URL}/markets?condition_ids={condition_id}"

    try:
        # Make HTTP GET request to the API with a 10 second timeout
        response = httpx.get(url, timeout=10)

        # Raise an exception if the request failed (404, 500, etc.)
        response.raise_for_status()

        # Parse the JSON response into a Python dictionary
        data = response.json()

        # The API returns an array of markets, even though we only expect one match
        # Check if we got results and return the first market
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        return None

    except httpx.HTTPError as e:
        # If anything goes wrong (network error, timeout, 404, etc.), print error and return None
        click.echo(f"Error fetching data: {e}", err=True)
        return None


def display_event_info(event: Dict[Any, Any]) -> None:
    """
    Display formatted event information

    Args:
        event: Event data dictionary from API
    """
    # Print header for event information section
    click.echo("\n" + "=" * 70)
    click.echo("EVENT INFORMATION")
    click.echo("=" * 70)

    # Display high-level event details
    # Using .get() with 'N/A' default in case field is missing from API response
    click.echo(f"├─ Event ID: {event.get('id', 'N/A')}")
    click.echo(f"├─ Event Slug: {event.get('slug', 'N/A')}")
    click.echo(f"├─ Event Title: {event.get('title', 'N/A')}")
    click.echo(f"├─ NegRisk Market ID: {event.get('negRiskMarketID', 'N/A')}")
    click.echo(f"└─ Is NegRisk: {event.get('negRisk', False)}")  # NegRisk = mutually exclusive outcomes

    # Extract markets from the event (an event can have multiple markets)
    # For example, NYC mayoral race has one market per candidate
    markets = event.get('markets', [])

    # Filter to only show active markets (not closed/archived)
    active_markets = [m for m in markets if m.get('active', False)]

    # Print header for markets section
    click.echo(f"\n{'=' * 70}")
    click.echo(f"MARKETS IN THIS EVENT ({len(active_markets)} active, {len(markets)} total)")
    click.echo("=" * 70 + "\n")

    # Loop through each active market and display all its identifiers
    for idx, market in enumerate(active_markets, 1):
        # Display the market title (e.g., candidate name)
        click.echo(f"{idx}. {market.get('groupItemTitle', 'Unknown Candidate')}")

        # Display all the different IDs associated with this market
        click.echo(f"   ├─ Market ID: {market.get('id', 'N/A')}")
        click.echo(f"   ├─ Market Slug: {market.get('slug', 'N/A')}")
        click.echo(f"   ├─ Question: {market.get('question', 'N/A')}")
        click.echo(f"   ├─ Condition ID: {market.get('conditionId', 'N/A')}")  # Used in smart contracts
        click.echo(f"   ├─ Question ID: {market.get('questionID', 'N/A')}")

        # Parse token IDs (these are stored as a JSON string like '["123", "456"]')
        # Token IDs represent the Yes and No positions for this market
        token_ids_str = market.get('clobTokenIds', '[]')
        try:
            # Convert JSON string to Python list
            token_ids = json.loads(token_ids_str)

            # Display Yes and No token IDs separately if available
            if len(token_ids) >= 2:
                click.echo(f"   ├─ Token ID (Yes): {token_ids[0]}")
                click.echo(f"   └─ Token ID (No): {token_ids[1]}")
            else:
                # Fallback if format is different
                click.echo(f"   └─ Token IDs: {token_ids}")
        except json.JSONDecodeError:
            # If JSON parsing fails, just show the raw string
            click.echo(f"   └─ Token IDs: {token_ids_str}")

        # Add blank line between markets for readability
        click.echo()


def display_market_info(market: Dict[Any, Any]) -> None:
    """
    Display formatted market information

    Args:
        market: Market data dictionary from API
    """
    # Print header for market information section
    click.echo("\n" + "=" * 70)
    click.echo("MARKET INFORMATION")
    click.echo("=" * 70)

    # Display high-level market details
    click.echo(f"├─ Market ID: {market.get('id', 'N/A')}")
    click.echo(f"├─ Market Slug: {market.get('slug', 'N/A')}")
    click.echo(f"├─ Question: {market.get('question', 'N/A')}")
    click.echo(f"├─ Condition ID: {market.get('conditionId', 'N/A')}")
    click.echo(f"├─ Question ID: {market.get('questionID', 'N/A')}")
    click.echo(f"├─ NegRisk Market ID: {market.get('negRiskMarketID', 'N/A')}")
    click.echo(f"└─ Is NegRisk: {market.get('negRisk', False)}")

    # Display token IDs
    click.echo(f"\n{'=' * 70}")
    click.echo("TOKEN IDS")
    click.echo("=" * 70)

    token_ids_str = market.get('clobTokenIds', '[]')
    try:
        token_ids = json.loads(token_ids_str)
        if len(token_ids) >= 2:
            click.echo(f"├─ Token ID (Yes): {token_ids[0]}")
            click.echo(f"└─ Token ID (No): {token_ids[1]}")
        else:
            click.echo(f"└─ Token IDs: {token_ids}")
    except json.JSONDecodeError:
        click.echo(f"└─ Token IDs: {token_ids_str}")

    # Display market status and metadata
    click.echo(f"\n{'=' * 70}")
    click.echo("MARKET STATUS")
    click.echo("=" * 70)
    click.echo(f"├─ Active: {market.get('active', 'N/A')}")
    click.echo(f"├─ Closed: {market.get('closed', 'N/A')}")
    click.echo(f"├─ Archived: {market.get('archived', 'N/A')}")
    click.echo(f"├─ Start Date: {market.get('startDate', 'N/A')}")
    click.echo(f"└─ End Date: {market.get('endDate', 'N/A')}")

    # Display market metrics
    click.echo(f"\n{'=' * 70}")
    click.echo("MARKET METRICS")
    click.echo("=" * 70)
    click.echo(f"├─ Volume: ${market.get('volume', 'N/A')}")
    click.echo(f"├─ Liquidity: ${market.get('liquidity', 'N/A')}")

    # Parse and display outcome prices
    outcomes_str = market.get('outcomes', '[]')
    prices_str = market.get('outcomePrices', '[]')
    try:
        outcomes = json.loads(outcomes_str)
        prices = json.loads(prices_str)
        if len(outcomes) >= 2 and len(prices) >= 2:
            click.echo(f"├─ {outcomes[0]} Price: {prices[0]}")
            click.echo(f"└─ {outcomes[1]} Price: {prices[1]}")
        else:
            click.echo(f"├─ Outcomes: {outcomes}")
            click.echo(f"└─ Prices: {prices}")
    except json.JSONDecodeError:
        click.echo(f"├─ Outcomes: {outcomes_str}")
        click.echo(f"└─ Prices: {prices_str}")

    # Display associated event if available
    events = market.get('events', [])
    if events:
        click.echo(f"\n{'=' * 70}")
        click.echo("ASSOCIATED EVENT")
        click.echo("=" * 70)
        event = events[0]
        click.echo(f"├─ Event ID: {event.get('id', 'N/A')}")
        click.echo(f"├─ Event Slug: {event.get('slug', 'N/A')}")
        click.echo(f"└─ Event Title: {event.get('title', 'N/A')}")


# This decorator creates a command group, which allows us to have multiple subcommands
# (like "event-slug" and "event-id") under one main CLI program
@click.group()
def cli():
    """
    Polymarket ID Lookup Tool

    Convert between different Polymarket identifiers:
    slugs, market IDs, condition IDs, question IDs, and token IDs.
    """
    pass  # This group is just a container for subcommands


# Define a command called "event-slug" that users can run
# Usage: python3 polymarket_lookup.py event-slug --slug "some-event"
@cli.command()
@click.option(
    '--slug',
    required=True,  # User must provide this parameter
    help='Event slug (e.g., "new-york-city-mayoral-election")'
)
def event_slug(slug: str):
    """
    Lookup event by slug and display all related IDs

    This command takes an event slug and shows you all the associated IDs:
    - Market ID, Condition ID, Question ID, Token IDs, etc.

    Example:
        python3 polymarket_lookup.py event-slug --slug "new-york-city-mayoral-election"
    """
    # Print what we're searching for
    click.echo(f"Looking up event: {slug}...")

    # Call the API to fetch event data
    event = fetch_event_by_slug(slug)

    # If nothing was found, show error and exit
    if event is None:
        click.echo(f"Event not found with slug: {slug}", err=True)
        return

    # Display all the IDs we found
    display_event_info(event)

    # Print success message
    click.echo("\n" + "=" * 70)
    click.echo("Lookup complete!")
    click.echo("=" * 70)


# Define a command called "event-id" that users can run
# Usage: python3 polymarket_lookup.py event-id --id "12345"
@cli.command()
@click.option(
    '--id',
    required=True,  # User must provide this parameter
    help='Event ID (e.g., "12345")'
)
def event_id(id: str):
    """
    Lookup event by event ID and display all related IDs

    This command takes an event ID and shows you all the associated information:
    - Event Slug, Market IDs, Condition IDs, Question IDs, Token IDs, etc.

    Example:
        python3 polymarket_lookup.py event-id --id "12345"
    """
    # Print what we're searching for
    click.echo(f"Looking up event ID: {id}...")

    # Call the API to fetch event data by ID
    event = fetch_event_by_id(id)

    # If nothing was found, show error and exit
    if event is None:
        click.echo(f"Event not found with ID: {id}", err=True)
        return

    # Display all the IDs we found
    display_event_info(event)

    # Print success message
    click.echo("\n" + "=" * 70)
    click.echo("Lookup complete!")
    click.echo("=" * 70)


# Define a command called "market-slug" that users can run
# Usage: python3 polymarket_lookup.py market-slug --slug "some-market"
@cli.command()
@click.option(
    '--slug',
    required=True,  # User must provide this parameter
    help='Market slug (e.g., "will-steve-sweeney-win-the-new-jersey-governor-election-in-2025")'
)
def market_slug(slug: str):
    """
    Lookup market by slug and display all related IDs

    This command takes a market slug and shows you all the associated IDs:
    - Market ID, Condition ID, Question ID, Token IDs, etc.

    Example:
        python3 polymarket_lookup.py market-slug --slug "will-steve-sweeney-win-the-new-jersey-governor-election-in-2025"
    """
    # Print what we're searching for
    click.echo(f"Looking up market: {slug}...")

    # Call the API to fetch market data
    market = fetch_market_by_slug(slug)

    # If nothing was found, show error and exit
    if market is None:
        click.echo(f"Market not found with slug: {slug}", err=True)
        return

    # Display all the IDs we found
    display_market_info(market)

    # Print success message
    click.echo("\n" + "=" * 70)
    click.echo("Lookup complete!")
    click.echo("=" * 70)


# Define a command called "market-id" that users can run
# Usage: python3 polymarket_lookup.py market-id --id "551142"
@cli.command()
@click.option(
    '--id',
    required=True,  # User must provide this parameter
    help='Market ID (e.g., "551142")'
)
def market_id(id: str):
    """
    Lookup market by market ID and display all related IDs

    This command takes a market ID and shows you all the associated information:
    - Market Slug, Condition ID, Question ID, Token IDs, etc.

    Example:
        python3 polymarket_lookup.py market-id --id "551142"
    """
    # Print what we're searching for
    click.echo(f"Looking up market ID: {id}...")

    # Call the API to fetch market data by ID
    market = fetch_market_by_id(id)

    # If nothing was found, show error and exit
    if market is None:
        click.echo(f"Market not found with ID: {id}", err=True)
        return

    # Display all the IDs we found
    display_market_info(market)

    # Print success message
    click.echo("\n" + "=" * 70)
    click.echo("Lookup complete!")
    click.echo("=" * 70)


# Define a command called "token-id" that users can run
# Usage: python3 polymarket_lookup.py token-id --id "16867679388..."
@cli.command()
@click.option(
    '--id',
    required=True,  # User must provide this parameter
    help='Token ID (e.g., "16867679388416061053995436140492438650416184687930130083732571696309100575009")'
)
def token_id(id: str):
    """
    Lookup market by token ID and display all related IDs

    This command takes a token ID (CLOB token ID) and shows you the associated market:
    - Market ID, Market Slug, Condition ID, Question ID, etc.

    Token IDs represent Yes/No positions in a market.

    Example:
        python3 polymarket_lookup.py token-id --id "16867679388416061053995436140492438650416184687930130083732571696309100575009"
    """
    # Print what we're searching for
    click.echo(f"Looking up token ID: {id}...")

    # Call the API to fetch market data by token ID
    market = fetch_market_by_token_id(id)

    # If nothing was found, show error and exit
    if market is None:
        click.echo(f"Market not found with token ID: {id}", err=True)
        return

    # Display all the IDs we found
    display_market_info(market)

    # Highlight which token was queried
    click.echo(f"\n{'=' * 70}")
    click.echo("TOKEN ID MATCH")
    click.echo("=" * 70)

    # Parse token IDs to show which one was queried (Yes or No)
    token_ids_str = market.get('clobTokenIds', '[]')
    try:
        token_ids = json.loads(token_ids_str)
        if len(token_ids) >= 2:
            if id == token_ids[0]:
                click.echo(f"└─ This token represents the 'Yes' outcome")
            elif id == token_ids[1]:
                click.echo(f"└─ This token represents the 'No' outcome")
            else:
                click.echo(f"└─ Token ID matched this market")
        else:
            click.echo(f"└─ Token ID matched this market")
    except json.JSONDecodeError:
        click.echo(f"└─ Token ID matched this market")

    # Print success message
    click.echo("\n" + "=" * 70)
    click.echo("Lookup complete!")
    click.echo("=" * 70)


# Define a command called "question-id" that users can run
# Usage: python3 polymarket_lookup.py question-id --id "0x5ddb6cc9..."
@cli.command()
@click.option(
    '--id',
    required=True,  # User must provide this parameter
    help='Question ID (e.g., "0x5ddb6cc9bcce2d9d810ef66a6ee394f91ecf28b7caa4e405036af1916b26e805")'
)
def question_id(id: str):
    """
    Lookup market by question ID and display all related IDs

    This command takes a question ID and shows you the associated market:
    - Market ID, Market Slug, Condition ID, Token IDs, etc.

    Example:
        python3 polymarket_lookup.py question-id --id "0x5ddb6cc9bcce2d9d810ef66a6ee394f91ecf28b7caa4e405036af1916b26e805"
    """
    # Print what we're searching for
    click.echo(f"Looking up question ID: {id}...")

    # Call the API to fetch market data by question ID
    market = fetch_market_by_question_id(id)

    # If nothing was found, show error and exit
    if market is None:
        click.echo(f"Market not found with question ID: {id}", err=True)
        return

    # Display all the IDs we found
    display_market_info(market)

    # Print success message
    click.echo("\n" + "=" * 70)
    click.echo("Lookup complete!")
    click.echo("=" * 70)


# Define a command called "condition-id" that users can run
# Usage: python3 polymarket_lookup.py condition-id --id "0x201df9b6..."
@cli.command()
@click.option(
    '--id',
    required=True,  # User must provide this parameter
    help='Condition ID (e.g., "0x201df9b6a68bab220392ca4cd18cf4d8c96b7612568777626292d2fb08954efe")'
)
def condition_id(id: str):
    """
    Lookup market by condition ID and display all related IDs

    This command takes a condition ID and shows you the associated market:
    - Market ID, Market Slug, Question ID, Token IDs, etc.

    Condition IDs are used in smart contracts to identify prediction markets.

    Example:
        python3 polymarket_lookup.py condition-id --id "0x201df9b6a68bab220392ca4cd18cf4d8c96b7612568777626292d2fb08954efe"
    """
    # Print what we're searching for
    click.echo(f"Looking up condition ID: {id}...")

    # Call the API to fetch market data by condition ID
    market = fetch_market_by_condition_id(id)

    # If nothing was found, show error and exit
    if market is None:
        click.echo(f"Market not found with condition ID: {id}", err=True)
        return

    # Display all the IDs we found
    display_market_info(market)

    # Print success message
    click.echo("\n" + "=" * 70)
    click.echo("Lookup complete!")
    click.echo("=" * 70)


# Entry point: when you run this script, it starts the CLI
if __name__ == '__main__':
    cli()