# Deadpan Forecasts for Cities That Do Not Exist

One line, read deadpan: a weather forecast for Vexholm, a city that does
not exist. Tonight there: a high of 12, a low of 12, and one small cloud
that has been circling the town hall since 1987.

Entry for the make.fun bounty:

[Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

[![Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/freysiatiara/deadpan-forecasts-20261126/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/freysiatiara/deadpan-forecasts-20261126/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

## How it works

`main.py` (Python standard library only) writes the forecast line to the
entry file. The output path comes from the `ENTRY_OUTPUT` environment
variable, else `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR`, else
`/output/entry.txt`. The file is written with plain `open`/`write` and
set to mode `0644`.

## Run it

```sh
python3 main.py
```

Then read the entry at the resolved output path (default
`/output/entry.txt`).
