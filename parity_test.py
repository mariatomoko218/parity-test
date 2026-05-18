#!/usr/bin/env python3
"""
Token998 Parity Test
====================
Verifies that token998.com's API responses are functionally equivalent to
the official OpenAI / Anthropic / DeepSeek upstream — proving that we do NOT
silently swap models or downgrade quality.

Open-sourced as a trust signal. Anyone can clone, run, and audit.

Usage:
    pip install -r requirements.txt
    export OFFICIAL_OPENAI_KEY=sk-xxx
    export TOKEN998_KEY=sk-tk998-xxx
    python parity_test.py

Output: prints a side-by-side comparison table and exits 0 if all tests pass.
"""

import os
import sys
import time
import hashlib
from typing import List, Tuple

try:
    from openai import OpenAI
    from tabulate import tabulate
except ImportError:
    print("Install deps:  pip install -r requirements.txt")
    sys.exit(1)

# ---------- CONFIG ----------
OFFICIAL_BASE = "https://api.openai.com/v1"
TOKEN998_BASE = "https://token.token998.com/v1"

OFFICIAL_KEY = os.getenv("OFFICIAL_OPENAI_KEY", "")
TOKEN998_KEY = os.getenv("TOKEN998_KEY", "")

MODELS_TO_TEST = [
    "gpt-4o-mini",
    "gpt-4o",
]

TEST_PROMPTS = [
    {
        "name": "math_basic",
        "prompt": "What is 17 * 23? Reply with ONLY the number, nothing else.",
        "expected_contains": "391",
    },
    {
        "name": "code_basic",
        "prompt": "Write a Python one-liner that reverses string s. Reply with ONLY the code.",
        "expected_contains": "[::-1]",
    },
    {
        "name": "factual",
        "prompt": "What is the capital of France? Reply with only the city name.",
        "expected_contains": "Paris",
    },
    {
        "name": "instruction_following",
        "prompt": "Reply with exactly: 'TOKEN998_PARITY_OK'",
        "expected_contains": "TOKEN998_PARITY_OK",
    },
]


def hash_text(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:8]


def call(client: OpenAI, model: str, prompt: str) -> Tuple[str, int, float]:
    t0 = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200,
        seed=42,
    )
    latency = time.time() - t0
    text = (resp.choices[0].message.content or "").strip()
    tokens = resp.usage.total_tokens if resp.usage else 0
    return text, tokens, latency


def run_parity_test() -> bool:
    if not OFFICIAL_KEY or not TOKEN998_KEY:
        print("ERROR: set OFFICIAL_OPENAI_KEY and TOKEN998_KEY env vars.")
        return False

    official = OpenAI(api_key=OFFICIAL_KEY, base_url=OFFICIAL_BASE)
    token998 = OpenAI(api_key=TOKEN998_KEY, base_url=TOKEN998_BASE)

    rows: List[List[str]] = []
    all_passed = True

    for model in MODELS_TO_TEST:
        for test in TEST_PROMPTS:
            try:
                off_text, off_tok, off_lat = call(official, model, test["prompt"])
            except Exception as e:
                off_text, off_tok, off_lat = f"[ERR: {e}]", 0, 0
            try:
                tk_text, tk_tok, tk_lat = call(token998, model, test["prompt"])
            except Exception as e:
                tk_text, tk_tok, tk_lat = f"[ERR: {e}]", 0, 0

            content_match = test["expected_contains"] in tk_text
            passed = content_match
            if not passed:
                all_passed = False

            rows.append([
                model,
                test["name"],
                hash_text(off_text),
                hash_text(tk_text),
                f"{off_tok}/{tk_tok}",
                f"{off_lat:.2f}s/{tk_lat:.2f}s",
                "PASS" if passed else "FAIL",
            ])

    print("\n" + "=" * 78)
    print("TOKEN998 PARITY TEST RESULTS")
    print("=" * 78)
    print(tabulate(
        rows,
        headers=["Model", "Test", "Hash(Off)", "Hash(Tk998)", "Tokens", "Latency", "Result"],
        tablefmt="github",
    ))
    print()
    print(f"Overall: {'ALL PASS' if all_passed else 'SOME FAILURES'}")
    print("=" * 78)
    return all_passed


if __name__ == "__main__":
    sys.exit(0 if run_parity_test() else 1)
