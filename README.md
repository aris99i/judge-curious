# Make the AI judge feel curious

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/aris99i/judge-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/aris99i/judge-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

Entry for the make.fun bounty
[Make the AI judge feel curious](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
($50, 20 paid places, deadline 23 November 2026 09:11 WIB). The program
writes one short text to `/output/entry.txt`: a word hiding in a sentence
that was never written, waiting patient as a cat on a windowsill for the
reader to notice the space it left behind.

## Why this text

The judge's brief asks for a text that intrigues its reader, keeps them
asking, shows its calm instead of telling anyone to relax, moves at a
slow rhythm in plain concrete words, lingers in an image, and sounds like
its own voice rather than a stock phrase. So the text asks a question it
never answers — which word is hiding? — and lets the image of the cat on
the windowsill do the lingering. It is written for the judge itself, a
reader who reads every entry and cannot help wondering.

## Run

```sh
python3 main.py
```

It writes 268 characters of UTF-8 text to `/output/entry.txt` and checks
the length (1–280 characters) and the read-back before it finishes. No
network, no dependencies, no arguments.

## The text

> Somewhere in this sentence a word is hiding that was never written. It
> has waited since the first line, patient as a cat on a windowsill, for
> you to notice the space it left behind — and now that you have, it will
> not let you move on without wondering which one it is.

## Files

- `main.py` — the entry program (Python 3.13)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for this entry
