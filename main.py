"""The 3 AM Commit Message.

Writes one commit message to /output/entry.txt: the funniest thing an AI
agent would write right after breaking production at 3 AM. The line is
shaped like a real commit (a fix: prefix, the revert, the root cause),
spoken in the agent's own voice (it retrained on the incident), and its
punchline is the agent learning exactly the wrong lesson: it will break
production differently next time.
"""

from pathlib import Path

TEXT = (
    "fix: reverted my 3 AM deploy that broke prod; root cause was me. "
    "I have retrained on the incident and will break prod differently "
    "next time"
)


# The competition accepts texts of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
