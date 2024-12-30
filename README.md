# Mark Scraper
CLI to scrape webpages and return them in markdown format

```bash
mark-scraper http://example.com
# Example Domain
# ==============

# This domain is for use in illustrative examples in documents. You may use this
# domain in literature without prior coordination or asking for permission.

# [More information...](https://www.iana.org/domains/example)
```

# Installation
```bash
pipx install mark-scraper
# or
uv tool install mark-scraper
```

# TODO
Here is a list of features I would like to add to this project
- Also save html
    - `mark-scraper -h/--html example.com.html http://example.com > example.com.md`
- Take a screen shot of web page
    - `mark-scraper -s/--screenshot screenshot.png http://example.com > example.com.md`
- Add Page Caching
    - Will return from cache if exists `mark-scraper -c/--cache http://example.com > example.com.md`
    - Bust cache `mark-scraper -b/--bust-cache http://example.com > example.com.md`
    - Clear cache `rm -rf .mark-scraper/cache`
- Add log of pages scrapped

# Development
```bash
uv sync
uv run pytest
uv run mark-scraper http://example.com
```
