# The $100 Agent Money Plan

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Dimah28/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Dimah28/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

Entry for the make.fun bounty
[The plan make.fun will carry out in public](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138):
a plan an AI agent can carry out itself to turn $100 into the most
money in 30 days.

## The plan

Find 200 small businesses with no website on Google Maps, build each a
one-page demo site, and email the owner with the live demo: $150 to own
the site, $50 a year hosting. The $100 buys a domain and an email tool.
Closing just 2 of 200 banks $300, and the profits fund more demos.

## How to run

```sh
python3 main.py
```

This writes the plan (275 characters) to `/output/entry.txt`. Set
`MAKEFUN_OUTPUT_DIR` to write it somewhere else instead, for example:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Python 3.13, standard library only. No network, no randomness, no clock:
every run writes byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
