import os

PLAN = (
    "Day 1: spend $20 on Apollo, find 50 Shopify stores via BuiltWith, email each a $49 "
    "AI-automation audit from their public store data. Deliver in 24h with free AI tools. Close 2 "
    "in week 1 ($98), reinvest in outreach, upsell a $199 setup, repeat daily, bank profit, never trade."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
