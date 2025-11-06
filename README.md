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

## Usage

### Web App
1. Go to [https://ifesitinkering.github.io/polymarket-rosetta/](https://ifesitinkering.github.io/polymarket-rosetta/)
2. Select your lookup type from the tabs
3. Enter your identifier
4. Click "Lookup"

### CLI Tool

**Installation:**
```bash
pip3 install httpx click
```

**Usage:**
```bash
# Event lookups
python3 polymarket_lookup.py event-slug --slug "new-york-city-mayoral-election"
python3 polymarket_lookup.py event-id --id "23246"

# Market lookups
python3 polymarket_lookup.py market-slug --slug "will-eric-adams-win-the-2025-nyc-mayoral-election"
python3 polymarket_lookup.py market-id --id "538928"
python3 polymarket_lookup.py condition-id --id "0x201df9b6a68bab220392ca4cd18cf4d8c96b7612568777626292d2fb08954efe"
python3 polymarket_lookup.py question-id --id "0x5ddb6cc9bcce2d9d810ef66a6ee394f91ecf28b7caa4e405036af1916b26e805"
python3 polymarket_lookup.py token-id --id "16867679388416061053995436140492438650416184687930130083732571696309100575009"
```

## Use Cases

**For Developers:**
- Quickly find blockchain contract addresses (Condition IDs) from market slugs
- Get token IDs for trading bots from human-readable market names
- Reverse lookup: find the market page from on-chain data

**For Traders:**
- Find CLOB token IDs for API trading
- Verify market details before placing orders
- Cross-reference different data sources

**For Researchers:**
- Map between Polymarket's frontend and blockchain data
- Build datasets linking all identifier types
- Analyze market structures and relationships

## Local Development

**Web App:**
```bash
git clone https://github.com/ifesiTinkering/polymarket-rosetta.git
cd polymarket-rosetta

# Run local server
python3 -m http.server 8000
# Visit http://localhost:8000
```

**CLI Tool:**
```bash
python3 polymarket_lookup.py --help
```

## Technical Details

- **Frontend:** Pure HTML/CSS/JavaScript (no frameworks)
- **API:** Polymarket Gamma API (`gamma-api.polymarket.com`)
- **Backend:** AWS Lambda proxy for CORS handling
- **Caching:** Browser localStorage with 1-hour expiration
- **Hosting:** GitHub Pages (static site)

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
