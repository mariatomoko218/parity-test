# Contributing

Thank you for helping keep Token998 honest.

## How to add a new test case

1. Fork this repo
2. Edit `parity_test.py` → add to `TEST_PROMPTS` list:
   ```python
   {
       "name": "your_test_name",
       "prompt": "Your prompt with a deterministic expected output",
       "expected_contains": "exact substring we look for",
   }
   ```
3. Run locally with your own keys to confirm it works
4. Open a PR

## How to report a parity failure

If you run the test and see a `FAIL`, **please open a GitHub Issue** with:
- Output of the failing test (use the table from console)
- Your timestamp (UTC)
- A description of what you expected vs got

We commit to:
- ✅ Acknowledging within 24 hours
- ✅ Investigating root cause within 48 hours
- ✅ Posting a public post-mortem within 7 days

## What we will NOT accept

- Test cases that depend on non-determinism (e.g. "creative writing should be similar")
- Test cases that require special account permissions
- Test cases that probe rate limits (we have separate tooling for that)

## Questions

- Email: hello@token998.com
- Telegram: https://t.me/token998_global
