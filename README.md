# Token998 Parity Test

> Open-source proof that [token998.com](https://token998.com) does **NOT** silently swap models or downgrade quality.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Uptime](https://img.shields.io/badge/uptime-99.9%25-brightgreen)](https://status.token998.com)

## Why this repo exists

The Chinese AI-API-relay industry has a documented trust problem: a few bad actors have been caught swapping `gpt-4o` requests for `gpt-4o-mini`, harvesting prompts, or routing through unreliable upstreams.

We open-source this test so **anyone can audit us in 60 seconds**.

## How to verify us in 60 seconds

```bash
git clone https://github.com/token998/parity-test
cd parity-test
pip install -r requirements.txt

export OFFICIAL_OPENAI_KEY=sk-...     # your own official OpenAI key
export TOKEN998_KEY=sk-tk998-...      # your token998 key (get $1 free at token998.com)

python parity_test.py
```

You'll see a side-by-side table of identical-seed outputs from both endpoints. If we ever swap models, the test fails publicly.

### Example output
```
============================================================================
TOKEN998 PARITY TEST RESULTS
============================================================================
| Model       | Test                  | Hash(Off) | Hash(Tk998) | Tokens | Latency       | Result |
|-------------|-----------------------|-----------|-------------|--------|---------------|--------|
| gpt-4o-mini | math_basic            | a3f9e2d1  | a3f9e2d1    | 18/18  | 0.82s/0.91s   | PASS   |
| gpt-4o-mini | code_basic            | 7c2b8e44  | 7c2b8e44    | 24/24  | 1.10s/1.18s   | PASS   |
| gpt-4o-mini | factual               | 4d5f6e7a  | 4d5f6e7a    | 12/12  | 0.65s/0.72s   | PASS   |
| gpt-4o      | math_basic            | a3f9e2d1  | a3f9e2d1    | 18/18  | 1.20s/1.30s   | PASS   |

Overall: ALL PASS
============================================================================
```

## What we DON'T do

- ❌ Log your prompts (we keep only billing metadata: tokens & timestamp)
- ❌ Substitute cheaper models for premium ones
- ❌ Re-route your traffic to questionable upstreams
- ❌ Train on your data

## What we DO

- ✅ Direct upstream pass-through (OpenAI / Anthropic / DeepSeek / Qwen official endpoints)
- ✅ Public status page: https://status.token998.com
- ✅ 99.9% monthly uptime SLA (with automatic credit refund if breached — see [SLA.md](./SLA.md))
- ✅ Refund unused credits within 7 days, no questions
- ✅ USDT settlement (TRC20 / BEP20)

## Pricing

3 RMB ≈ $1 official-equivalent credit (≈ 42% off official prices).

| Model | Official | Token998 | Savings |
|-------|----------|----------|---------|
| GPT-4o (1M input) | $2.50 | $1.05 | 58% |
| Claude 3.5 Sonnet (1M input) | $3.00 | $1.26 | 58% |
| DeepSeek V3 (1M input) | $0.27 | $0.11 | 59% |
| Qwen 2.5 Max (1M input) | $0.45 | $0.19 | 58% |

See [full pricing](https://token.token998.com/pricing) for all 500+ models.

## Contributing

Found a test case where we fail parity? **Please open an issue with the failing output.** We commit to investigating within 24 hours and posting a public post-mortem within 48 hours.

Want to add a new test case? PRs welcome — see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

[MIT](./LICENSE) — fork, modify, run against any other AI relay you suspect.

## Contact

- 🌐 Website: https://token998.com / [English](https://en.token998.com)
- 📧 Email: hello@token998.com
- 💬 Telegram: https://t.me/token998_global
- 🐛 Issues: file failing test runs publicly — we fix in 24h
