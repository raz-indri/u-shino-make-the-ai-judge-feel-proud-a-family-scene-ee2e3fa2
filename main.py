"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one line, well under 280 characters) to
/output/entry.txt. The scene is the duel-test winner of 8 drafts, judged
pairwise in both orders against the bounty judge brief: a warm, funny,
heartfelt Sunday-lunch moment — a mother who still sets a place for her
late husband, then eats his pudding herself.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280

SCENE = (
    "Mum still sets a place for Dad at Sunday lunch, three years on \u2014 "
    "then eats his pudding herself and says, 'He'd want me to have it.'"
)


def main() -> None:
    # The gate requires 1-280 UTF-8 characters; refuse to write an entry
    # that would fail it rather than emitting it silently.
    text = SCENE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"scene is {len(text)} chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
