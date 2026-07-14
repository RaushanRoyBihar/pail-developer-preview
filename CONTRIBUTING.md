# Contributing

This repository accepts documentation corrections, client compatibility fixes,
and public-contract tests. It does not accept private rule implementations,
runtime archives, datasets, credentials, database snapshots, wave capsules, or
trained memory files.

Before proposing a change, run:

```bash
bash scripts/public-safety-check.sh
python3 -m unittest discover -s clients/python -p 'test_*.py' -v
node --test clients/js/*.test.mjs
```
