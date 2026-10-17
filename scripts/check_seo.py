from pathlib import Path

html = Path("index.html").read_text(encoding="utf-8")
required = [
    '<title>Bismi Boutique', 'name="description"', 'rel="canonical"',
    'property="og:title"', 'property="og:image"', 'name="twitter:card"',
    'application/ld+json', 'id="products"', 'Women', 'Kids', 'View more styles'
]
missing = [item for item in required if item not in html]
if missing:
    raise SystemExit("Missing SEO/storefront markers: " + ", ".join(missing))
for file_name in ["robots.txt", "sitemap.xml", "manifest.json", "llms.txt", "humans.txt", "privacy-policy.html", "terms-and-conditions.html", "shipping-returns.html", "contact.html"]:
    if not Path(file_name).exists():
        raise SystemExit(f"Missing {file_name}")
for stale in ["UlarSuvai", "Chicken Oorugai", "Karuvadu", "Uppukandam"]:
    if stale in html:
        raise SystemExit("Old food-brand content remains in homepage: " + stale)
print("Bismi Boutique SEO, AI discovery, catalogue and policy-page markers are present.")
