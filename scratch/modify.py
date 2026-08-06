import os
import re
import urllib.request
import json
import subprocess

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Social-Listening-Platform\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. SaaS Products sorting & company size
saas_data = [
    {"name": "Brandwatch", "desc": "Enterprise-grade consumer intelligence...", "price": "Custom", "free": "N/A", "size": 100000000, "size_str": "$100M+ Revenue"},
    {"name": "Meltwater", "desc": "Media intelligence and social listening suite...", "price": "Custom", "free": "N/A", "size": 400000000, "size_str": "$400M+ Revenue"},
    {"name": "Sprinklr", "desc": "Unified customer experience platform...", "price": "Custom", "free": "N/A", "size": 700000000, "size_str": "$700M+ Revenue"},
    {"name": "Talkwalker", "desc": "Large-scale social listening and media monitoring...", "price": "Custom", "free": "N/A", "size": 50000000, "size_str": "$50M+ Revenue"},
    {"name": "YouScan", "desc": "AI-powered visual and social listening...", "price": "Custom", "free": "N/A", "size": 5000000, "size_str": "$5M Revenue"},
    {"name": "Awario", "desc": "Accessible social listening and brand monitoring...", "price": "Starts at ~$39/mo", "free": "N/A", "size": 2000000, "size_str": "$2M Revenue"},
    {"name": "Mention", "desc": "Real-time brand monitoring platform...", "price": "Starts at ~$41/mo", "free": "1 alert, 1k mentions/mo", "size": 5000000, "size_str": "$5M Revenue"},
    {"name": "Keyhole", "desc": "Social listening and analytics platform...", "price": "Starts at ~$99/mo", "free": "N/A", "size": 1000000, "size_str": "$1M Revenue"},
    {"name": "Brand24", "desc": "Real-time brand monitoring and social listening...", "price": "Starts at ~$99/mo", "free": "N/A", "size": 5000000, "size_str": "$5M Revenue"},
    {"name": "Synthesio", "desc": "Consumer intelligence and social listening...", "price": "Custom", "free": "N/A", "size": 20000000, "size_str": "$20M Revenue"},
    {"name": "Digimind", "desc": "Social listening and competitive intelligence...", "price": "Custom", "free": "N/A", "size": 15000000, "size_str": "$15M Revenue"},
    {"name": "NetBase Quid", "desc": "AI-driven consumer and market intelligence...", "price": "Custom", "free": "N/A", "size": 50000000, "size_str": "$50M Revenue"}
]

saas_data.sort(key=lambda x: x["size"], reverse=True)

saas_table = "| Product | Description | Pricing | Free Tier Limit | Company Size |\n|---|---|---|---|---|\n"
for item in saas_data:
    url = f"https://www.{item['name'].lower().replace(' ', '')}.com/"
    saas_table += f"| **[{item['name']}]({url})** | {item['desc']} | {item['price']} | {item['free']} | {item['size_str']} |\n"

# Open Source Repos
os_repos = [
    {"name": "Harken", "url": "https://github.com/VladUZH/harken", "desc": "Self-hosted, open-source social listening tool...", "repo": "VladUZH/harken"},
    {"name": "OpenMagpie", "url": "https://github.com/obris-dev/openmagpie", "desc": "Open-source, self-hostable social listening platform...", "repo": "obris-dev/openmagpie"},
    {"name": "Open Social Media Monitoring", "url": "https://github.com/openstream/open-social-media-monitoring", "desc": "Classic open-source social media monitoring suite...", "repo": "openstream/open-social-media-monitoring"},
    {"name": "Watchman", "url": "https://github.com/Sotera/watchman", "desc": "Open-source social-media event-detection system...", "repo": "Sotera/watchman"},
    {"name": "SONDY", "url": "https://github.com/AdrienGuille/SONDY", "desc": "Open-source social media data mining software...", "repo": "AdrienGuille/SONDY"},
    {"name": "Brandtrack", "url": "https://github.com/RkayG/brandtrack", "desc": "Open-source social listening projects...", "repo": "RkayG/brandtrack"},
    {"name": "Social-Analyzer", "url": "https://github.com/qeeqbox/social-analyzer", "desc": "API, CLI & Web App for analyzing & finding a person's profile...", "repo": "qeeqbox/social-analyzer"} # Added more
]

for repo in os_repos:
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{repo['repo']}")
        req.add_header('User-Agent', 'Mozilla/5.0')
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        repo["stars"] = data.get("stargazers_count", 0)
    except Exception as e:
        print(f"Error fetching {repo['repo']}: {e}")
        repo["stars"] = 0

os_repos.sort(key=lambda x: x["stars"], reverse=True)

os_content = ""
for r in os_repos:
    badge = f"[![Stars](https://img.shields.io/github/stars/{r['repo']}?style=social&color=white)](https://github.com/{r['repo']}/stargazers)"
    os_content += f"- **[{r['name']}]({r['url']})** {badge} \n  {r['desc']}\n\n"

# Generate Banner SVG
assets_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Social-Listening-Platform\assets"
os.makedirs(assets_dir, exist_ok=True)
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#1a2a6c"><animate attributeName="stop-color" values="#1a2a6c;#b21f1f;#fdbb2d;#1a2a6c" dur="10s" repeatCount="indefinite"/></stop>
            <stop offset="100%" stop-color="#b21f1f"><animate attributeName="stop-color" values="#b21f1f;#fdbb2d;#1a2a6c;#b21f1f" dur="10s" repeatCount="indefinite"/></stop>
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" rx="15"/>
    <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">Awesome Social Listening Platform 🚀</text>
    <text x="50%" y="75%" font-family="Arial, sans-serif" font-size="20" fill="#f0f0f0" text-anchor="middle" dominant-baseline="middle">Curated list of Top SaaS &amp; Open Source Tools</text>
</svg>"""
with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

new_content = f"""<div align="center">
  <img src="assets/banner.svg" alt="Awesome Social Listening Banner"/>
</div>

# Awesome Social Listening Platform 🌟📊

<div align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" align="right"/></a>
</div>

**Curated List of SaaS Products & Open-Source GitHub Projects** 🌍  
*Focused on Social Listening, Brand Monitoring, Sentiment Analysis, Media Intelligence & Conversation Tracking* 🔍  

This repository tracks notable **SaaS platforms** 🏢 and **open-source projects** 💻 for **Social Listening**.

## Table of Contents 📑
- [SaaS/Hosted Platforms](#saashosted-platforms)
- [Open-Source GitHub Projects](#open-source-github-projects)
- [How to Contribute](#how-to-contribute)
- [Disclaimer](#disclaimer)

## SaaS/Hosted Platforms 🚀
{saas_table}

## Open-Source GitHub Projects 🌐
{os_content}

## Additional Strong Open-Source Options 🛠️
- **Sentiment analysis libraries** (VADER, NLP.js, spaCy-based pipelines, transformer models) combined with custom scrapers or APIs.
- **Fediverse / Mastodon / Bluesky monitoring scripts** and self-hosted collectors.

## How to Contribute 🤝
1. Fork the repo 🍴
2. Add/edit entries in `README.md` (follow existing format).
3. Submit PR with a short explanation 🚀

## Disclaimer ⚠️
- This is a **community-curated** list — not exhaustive and not an endorsement.

## Star History 📈
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Social-Listening-Platform&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Social-Listening-Platform&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Social-Listening-Platform&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Social-Listening-Platform&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

new_content = new_content.replace("chartrepos", "chart?repos")
new_content = new_content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Markdown updated.")
