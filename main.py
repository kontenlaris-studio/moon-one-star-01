#!/usr/bin/env python3
"""moon-one-star-01 — The Moon Gets One Star (make.fun).

One line: a one-star review of the moon, written by a customer who
is very unhappy with the service. The moon's great crime is taking
credit for the tides while doing none of the actual work — and never
answering during the day. The twist is the customer-service frame:
the reviewer treats a celestial body like a lazy contractor who
only clocks in at night.
"""

import os

ENTRY = (
    "One star. Only visible at night, never answers during the day, "
    "and somehow takes credit for the tides."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
