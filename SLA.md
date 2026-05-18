# Token998 Service Level Agreement (SLA)

**Effective Date:** 2026-05-17
**Version:** 1.0

This SLA is a binding commitment between Token998 ("we", "us") and our paying users ("you").

---

## 1. Uptime Commitment

We commit to **99.9% monthly uptime** for the API service at `https://token.token998.com/v1`.

| Monthly Uptime | Max Allowed Downtime | Service Credit |
|----------------|---------------------|----------------|
| ≥ 99.9% | ≤ 43.2 minutes | No credit (SLA met) |
| 99.0% – 99.89% | 43.2 min – 7.2 hours | **10%** of monthly spend |
| 95.0% – 98.99% | 7.2 hours – 36 hours | **25%** of monthly spend |
| < 95.0% | > 36 hours | **50%** of monthly spend |

**Uptime is measured by our public status page**: https://status.token998.com (third-party verified via BetterStack).

---

## 2. What Counts as Downtime

- HTTP 5xx errors on `/v1/chat/completions` or `/v1/models` endpoints (excluding upstream-attributable errors)
- Sustained latency > 30 seconds for `gpt-4o-mini` requests (a known-fast baseline)
- Console (`/console/topup`) unreachable for > 5 minutes

## 3. What Does NOT Count

- Scheduled maintenance (announced ≥ 48h in advance via status page)
- Upstream provider outages (OpenAI / Anthropic / DeepSeek official going down) — but we will publicly disclose
- Force majeure: war, natural disasters, government action
- Your own network or API key issues

## 4. How to Claim Service Credit

1. Within 30 days of the incident, email `sla@token998.com` with:
   - Your account ID
   - Affected time window
   - Sample failed request IDs (any 3)
2. We respond within 5 business days
3. Credit is issued as account balance (not cash refund), usable on any model

## 5. Parity Commitment

We additionally commit:

- **No model substitution**: requests for `gpt-4o` will only be served by `gpt-4o` upstream
- **No prompt logging**: we retain only `{request_id, timestamp, model, token_count, user_id}` for billing
- **No training on user data**: ever

Violation of these commitments triggers **automatic full refund of current month's spend** plus removal of the affected account from future logging entirely.

Our [open-source parity test](https://github.com/token998/parity-test) lets you verify this independently.

## 6. Refund Policy

- **First 7 days**: 100% refund of unused credits, no questions
- **After 7 days**: account credits are non-refundable but never expire

## 7. Termination

Either party may terminate at any time. Upon termination:
- Unused credits ≤ 7 days old → refunded to original payment method
- All user data → deleted within 30 days

## 8. Contact

- SLA claims: `sla@token998.com`
- General support: `hello@token998.com`
- Public status: https://status.token998.com
- Open audit: https://github.com/token998/parity-test

---

> This SLA is published under the MIT license — fork it, adapt it, hold us to it.
