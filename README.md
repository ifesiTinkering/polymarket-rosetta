# Polymarket Rosetta

> The Rosetta Stone for Polymarket identifiers

Polymarket Rosetta is a lookup tool that lets you find all related Polymarket identifiers from any single identifier. Just like the ancient Rosetta Stone helped decode hieroglyphics by showing the same text in multiple scripts, this tool shows you the same market or event across all of Polymarket's different ID formats.

**Live Demo:** [https://ifesitinkering.github.io/polymarket-rosetta/](https://ifesitinkering.github.io/polymarket-rosetta/)

## What It Does

Polymarket uses different identifier types across their platform:
- **Slugs** - Human-readable URLs (e.g., `new-york-city-mayoral-election`)
- **Market IDs** - Numeric identifiers (e.g., `551142`)
- **Condition IDs** - Blockchain contract identifiers (e.g., `0x201df9b6...`)
- **Question IDs** - UMA oracle identifiers (e.g., `0x5ddb6cc9...`)
- **Token IDs** - CLOB token identifiers for Yes/No positions (e.g., `16867679388416061...`)

**The Problem:** If you have one type of ID, finding the others requires manual API exploration.

**The Solution:** Polymarket Rosetta lets you input any ID type and instantly retrieves all the others.

## Features

### Event Lookups
Search for a Polymarket event to see all markets within it:
- Input: Event slug or Event ID
- Output: Event details + all associated markets with their complete ID sets

### Market Lookups
Search for a specific market to get all its identifiers:
- Input: Market slug, Market ID, Condition ID, Question ID, or Token ID
- Output: All related IDs, market status, pricing, volume, and associated event

## Screenshots

### Event Lookup
_[Screenshot placeholder: Event lookup showing NYC Mayoral Election with all candidate markets]_

### Market Lookup
_[Screenshot placeholder: Market lookup showing all IDs for a specific candidate market]_

### All Lookup Types
_[Screenshot placeholder: Tab interface showing all 7 lookup options]_

## Usage

### Quick Start
1. Go to [https://ifesitinkering.github.io/polymarket-rosetta/](https://ifesitinkering.github.io/polymarket-rosetta/)
2. Select your lookup type from the tabs
3. Enter your identifier
4. Click "Lookup"
5. View all related IDs

### Example Queries

**Event by Slug:**
```
Input: new-york-city-mayoral-election
Returns: Event info + all candidate markets
```

**Market by ID:**
```
Input: 551142
Returns: Complete market details with all IDs
```

**Market by Question ID:**
```
Input: 0x5ddb6cc9bcce2d9d810ef66a6ee394f91ecf28b7caa4e405036af1916b26e805
Returns: Market details + slug, market ID, condition ID, token IDs
```

**Market by Token ID:**
```
Input: 16867679388416061053995436140492438650416184687930130083732571696309100575009
Returns: Market details + identifies if this is a Yes or No token
```

## Use Cases

### For Developers
- Quickly find blockchain contract addresses (Condition IDs) from market slugs
- Get token IDs for trading bots from human-readable market names
- Reverse lookup: find the market page from on-chain data

### For Traders
- Find CLOB token IDs for API trading
- Verify market details before placing orders
- Cross-reference different data sources

### For Researchers
- Map between Polymarket's frontend and blockchain data
- Build datasets linking all identifier types
- Analyze market structures and relationships

## Technical Details

### Architecture
- **Frontend:** Pure HTML/CSS/JavaScript (no frameworks)
- **API:** Polymarket Gamma API (`gamma-api.polymarket.com`)
- **CORS Handling:** AllOrigins proxy for GitHub Pages compatibility
- **Hosting:** GitHub Pages (static site)

### API Endpoints Used
```
GET /events?slug={slug}           # Event by slug
GET /events/{id}                   # Event by ID
GET /markets?slug={slug}          # Market by slug
GET /markets/{id}                  # Market by ID
GET /markets?question_ids={id}    # Market by Question ID
GET /markets?condition_ids={id}   # Market by Condition ID
GET /markets?clob_token_ids={id}  # Market by Token ID
```

### Data Flow
```
User Input → JavaScript → CORS Proxy → Polymarket API → Parse Response → Display
```

## Performance Improvements

### Current Performance
- Initial lookups: 2-4 seconds (due to CORS proxy)
- Repeat lookups: 2-4 seconds (no caching currently)

### Recommended Improvements

**Option 1: AWS Lambda Backend** (Recommended)

Deploy a simple AWS Lambda function to proxy API requests directly, eliminating the CORS proxy middleman:

**Benefits:**
- 3-5x faster (sub-second responses)
- No CORS proxy rate limits
- More reliable
- Minimal cost (likely free tier)

**Implementation Steps:**

1. **Create Lambda Function:**
   ```python
   import json
   import urllib.request

   def lambda_handler(event, context):
       # Parse query parameters
       path = event.get('queryStringParameters', {}).get('path', '')

       # Fetch from Polymarket API
       url = f"https://gamma-api.polymarket.com{path}"
       response = urllib.request.urlopen(url)
       data = json.loads(response.read())

       return {
           'statusCode': 200,
           'headers': {
               'Access-Control-Allow-Origin': '*',
               'Content-Type': 'application/json'
           },
           'body': json.dumps(data)
       }
   ```

2. **Set up API Gateway:**
   - Create new REST API
   - Add GET method
   - Configure query string parameter: `path`
   - Deploy to stage (e.g., `prod`)

3. **Update Frontend:**
   ```javascript
   // Replace this line in index.html:
   const BASE_URL = 'https://gamma-api.polymarket.com';

   // With your Lambda endpoint:
   const LAMBDA_URL = 'https://YOUR-API-ID.execute-api.REGION.amazonaws.com/prod';

   function proxyUrl(url) {
       const path = url.replace('https://gamma-api.polymarket.com', '');
       return `${LAMBDA_URL}?path=${encodeURIComponent(path)}`;
   }
   ```

**Estimated Setup Time:** 15-20 minutes

**Option 2: Client-Side Caching**

Add localStorage caching for instant repeat lookups:
```javascript
// Cache results for 1 hour
// Instant response for repeated queries
```

**Option 3: CloudFront CDN**

Add AWS CloudFront in front of Lambda for global edge caching and even faster performance worldwide.

## CLI Tool

This project also includes a Python CLI tool (`polymarket_lookup.py`) with the same functionality:

### Installation
```bash
# Install dependencies
pip3 install httpx click
```

### Usage
```bash
# Event lookups
python3 polymarket_lookup.py event-slug --slug "new-york-city-mayoral-election"
python3 polymarket_lookup.py event-id --id "23246"

# Market lookups
python3 polymarket_lookup.py market-slug --slug "will-steve-sweeney-win-the-new-jersey-governor-election-in-2025"
python3 polymarket_lookup.py market-id --id "551142"
python3 polymarket_lookup.py question-id --id "0x5ddb6cc9bcce2d9d810ef66a6ee394f91ecf28b7caa4e405036af1916b26e805"
python3 polymarket_lookup.py condition-id --id "0x201df9b6a68bab220392ca4cd18cf4d8c96b7612568777626292d2fb08954efe"
python3 polymarket_lookup.py token-id --id "16867679388416061053995436140492438650416184687930130083732571696309100575009"

# Get help
python3 polymarket_lookup.py --help
```

### Example Output
```
Looking up event: new-york-city-mayoral-election...

======================================================================
EVENT INFORMATION
======================================================================
├─ Event ID: 23246
├─ Event Slug: new-york-city-mayoral-election
├─ Event Title: New York City Mayoral Election
├─ NegRisk Market ID: 0x289dc66d9938b32cb340a630d13de0a91e3e04e0dc62a219a26a16e6f9cc2600
└─ Is NegRisk: True

======================================================================
MARKETS IN THIS EVENT (12 active, 20 total)
======================================================================

1. Eric Adams
   ├─ Market ID: 538928
   ├─ Market Slug: will-eric-adams-win-the-2025-nyc-mayoral-election
   ├─ Question: Will Eric Adams win the 2025 NYC mayoral election?
   ├─ Condition ID: 0x846ce700a217ec7b75b8d078450f7e88eb5f44c76c12ae448ca10039ef4412b9
   ├─ Question ID: 0x289dc66d9938b32cb340a630d13de0a91e3e04e0dc62a219a26a16e6f9cc2600
   ├─ Token ID (Yes): 12541509255877010177934715422358422748052378132651567836811989084820478865881
   └─ Token ID (No): 557149893577824223387740663828120572195409127574902734254512226734855221907
```

See `DEPLOYMENT.md` for full CLI documentation.

## Local Development

### Web App
```bash
# Clone the repository
git clone https://github.com/ifesiTinkering/polymarket-rosetta.git
cd polymarket-rosetta

# Open in browser
open index.html

# Or run local server
python3 -m http.server 8000
# Visit http://localhost:8000
```

### CLI Tool
```bash
# Install dependencies
pip3 install httpx click

# Run any lookup command
python3 polymarket_lookup.py --help
```

## Deployment

### GitHub Pages (Current)
Already deployed at [https://ifesitinkering.github.io/polymarket-rosetta/](https://ifesitinkering.github.io/polymarket-rosetta/)

See `DEPLOYMENT.md` for full deployment instructions.

### Self-Hosting
Simply host `index.html` on any static file server:
- AWS S3 + CloudFront
- Vercel
- Netlify
- Cloudflare Pages

## Project Structure

```
polymarket-rosetta/
├── index.html              # Web app (HTML + CSS + JavaScript)
├── polymarket_lookup.py    # Python CLI tool
├── README.md               # This file
└── DEPLOYMENT.md           # Deployment instructions
```

## Contributing

Contributions welcome! This tool is designed to help the Polymarket developer community.

### Ideas for Contribution
- Add caching for faster repeat lookups
- Create AWS Lambda backend for better performance
- Add export functionality (CSV, JSON)
- Add batch lookup capability
- Improve error handling
- Add mini definitions for each ID type

## Glossary

**Slug:** Human-readable identifier in URLs (e.g., `new-york-city-mayoral-election`)

**Market ID:** Numeric identifier for a specific market

**Condition ID:** Ethereum smart contract identifier used in CTF (Conditional Token Framework)

**Question ID:** Identifier used by UMA (Universal Market Access) oracle for resolution

**Token ID:** CLOB (Central Limit Order Book) token identifier for Yes/No positions

**NegRisk:** Mutually exclusive outcomes in multi-market events (e.g., election with multiple candidates)

**Event:** A collection of related markets (e.g., NYC Mayoral Election contains markets for each candidate)

**Market:** A single binary prediction market with Yes/No outcomes

## License

MIT License - feel free to use this however you want!

## Acknowledgments

Built for the Polymarket developer community. Inspired by the need for a simple way to navigate between Polymarket's various identifier types.

Special thanks to the Polymarket team for providing a public API.

---

**Questions or issues?** Open an issue on GitHub or reach out to [@ifesiTinkering](https://github.com/ifesiTinkering)
