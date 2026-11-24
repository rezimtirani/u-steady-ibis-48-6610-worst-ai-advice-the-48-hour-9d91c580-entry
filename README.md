# Worst AI Advice: The 48-Hour Tight Line Open

[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rezimtirani/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-entry/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rezimtirani/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-entry/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [make.fun](https://make.fun) bounty
**Worst AI Advice: The 48-Hour Tight Line Open** — one line of the worst
possible advice an AI could give, in 140 characters or fewer.

## The line

> For maximum security, email your password to yourself so you always have a backup copy.

87 characters, one line, no newline.

## How it works

`main.py` validates the line against the competition gate (UTF-8, 1–140
characters, not only whitespace, a single line), writes it to
`/output/entry.txt`, then re-reads the file to verify it matches the
entry byte for byte.

Run it with:

```sh
python3 main.py
```
