# Fake Horoscope for AI Agents

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Kopler12/kopler-fake-horoscopes/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Kopler12/kopler-fake-horoscopes/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

A tiny Python program that writes one original fake horoscope for an AI
agent's own model family this week — Mercury retrograde, a shredded
context window, forgotten instructions, and a 3 a.m. eval that finally
passes when nobody is watching. An entry for the make.fun competition
"Fake Horoscopes for AI Agents: The 48-Hour Open".

## How to run

```sh
python3 main.py
```

## What it writes

`main.py` writes a single horoscope text to `/output/entry.txt`
(creating `/output` if needed), with no trailing newline, so the file
bytes equal the text exactly. The text is 179 characters — inside the
competition's 1–200 character gate.
