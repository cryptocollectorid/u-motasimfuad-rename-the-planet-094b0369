"""Rename the Planet — one-line entry.

Writes the final line to /output/entry.txt.
"""

LINE = "Jupiter is now The Eternal Grudge, because its Great Red Spot has stormed for 300 years and it still hasn't forgiven a single cloud."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"{len(LINE)} chars: {LINE}")


if __name__ == "__main__":
    main()
