# Deploying Polymarket ID Lookup to GitHub Pages

## Quick Deploy (Easiest Method)

### Step 1: Create a GitHub Repository
1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `polymarket-lookup` or `polymarket-glossary`
3. Make it **public** (required for free GitHub Pages)
4. Don't add README, .gitignore, or license (we'll push our existing files)

### Step 2: Push Your Code
```bash
cd /Users/ifesionubogu/Desktop/POLYMARKET_DIRECTORY

# Initialize git repository (if not already done)
git init

# Add your files
git add index.html

# Create first commit
git commit -m "Initial commit: Polymarket ID Lookup Tool"

# Add your GitHub repository as remote (replace USERNAME and REPO_NAME)
git remote add origin https://github.com/USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Source", select **main** branch
5. Keep the folder as **/ (root)**
6. Click **Save**

### Step 4: Access Your Site
Your site will be live at:
```
https://USERNAME.github.io/REPO_NAME/
```

It may take 2-5 minutes for the site to go live after enabling GitHub Pages.

---

## Alternative: Deploy with One Command

If you have GitHub CLI installed:

```bash
# Create repo and push
gh repo create polymarket-lookup --public --source=. --remote=origin
git add index.html
git commit -m "Initial commit"
git push -u origin main

# Enable GitHub Pages
gh api repos/:owner/:repo/pages -X POST -f source[branch]=main -f source[path]=/
```

---

## What Gets Deployed

- **index.html** - The complete web app (includes HTML, CSS, and JavaScript)
- No backend needed - runs entirely in the browser
- Calls Polymarket Gamma API directly from user's browser

---

## Features Included

✅ Event Slug lookup
✅ Event ID lookup
✅ Market Slug lookup
✅ Market ID lookup
✅ Question ID lookup
✅ Condition ID lookup
✅ Token ID lookup

All 7 lookup types from your Python CLI tool!

---

## Testing Locally

Before deploying, you can test locally by:
1. Opening `index.html` directly in your browser, OR
2. Running a local server:
   ```bash
   python3 -m http.server 8000
   # Visit http://localhost:8000
   ```

---

## Updating Your Site

After making changes:
```bash
git add index.html
git commit -m "Update: description of changes"
git push
```

GitHub Pages will automatically rebuild (takes 1-2 minutes).

---

## Troubleshooting

**Site not loading?**
- Wait 5 minutes after enabling GitHub Pages
- Make sure repository is public
- Check that index.html is in the root directory
- Verify GitHub Pages is enabled in Settings → Pages

**API not working?**
- Check browser console for errors (F12)
- Polymarket API must be accessible (not blocked by firewall)
- The API is public and doesn't require authentication

---

## Custom Domain (Optional)

To use your own domain:
1. Add a CNAME file to your repository with your domain
2. In GitHub Settings → Pages, enter your custom domain
3. Update your domain's DNS to point to GitHub Pages

---

## Example Repository Structure

```
polymarket-lookup/
├── index.html          (your web app)
├── DEPLOYMENT.md       (this file)
└── polymarket_lookup.py (optional - keep for CLI version)
```

The Python file is not used by GitHub Pages but you can keep it in the repo for reference.
