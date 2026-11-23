"""One Letter for Your Day — entry program.

Writes exactly one letter, "Z", to /output/entry.txt (one byte, no newline).

Why Z — the letter whose hidden word lands hardest under the judge's brief:
the judge never sees the word, it infers it, so the winning letter is the one
whose most likely inferred word is vivid, specific, funny and true, and whose
every plausible inference is strong. For Z that word is "zero sleep" (the
brief's own example): a concrete quantity, a sharp picture, dry and funny,
and an honest report of a real day. Every other natural Z-word is strong too
(zombie, zero motivation), so Z wins whatever the judge infers — while A
(amazing), F (fantastic), S (stressed) and T (tired) all collapse into vague
mood words that lose criterion 2. Z is also the only initial for "zero", so no
sharper letter exists for it (criterion 5).
"""

import os
import sys

LETTER = "Z"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(LETTER.encode("ascii"))
    # Self-check (revision pass): re-read what was written and prove it is
    # exactly one byte, "Z", with no trailing newline — the gate requires
    # 1 to 1 characters. Any mismatch fails loudly instead of shipping a
    # bad entry.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != LETTER.encode("ascii"):
        print(f"self-check failed: wrote {written!r}, expected {LETTER!r}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
