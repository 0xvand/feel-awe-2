# feel-awe-2

A short awe-inspiring text for the make.fun competition
[make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600).

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/0xvand/feel-awe-2/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/0xvand/feel-awe-2/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

`main.py` (Python 3.13, stdlib only) writes the entry text — a dying star's
light still travelling, and a whole life fitting inside one quiet second of
it — to `entry.txt` in the output directory, validating that the text is
1–280 code points and non-blank first.

## Usage

```sh
python3 main.py --output /tmp/out
```

The output directory can also be set with the `MAKEFUN_OUTPUT_DIR`
environment variable. Without either, output goes to `/output`.
