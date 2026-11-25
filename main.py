"""The One-Liner Groan-Off — entry program.

Writes one original one-line dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt), exactly the line plus one trailing
newline. Sealed gate: UTF-8 text of 1 to 140 characters, not only
whitespace.

DECISION RECORD — candidates weighed against the judge's brief, in order
(dad joke first, fast clean punchline, fresh, tight and rhythmic,
groan earned):

A. "I bought a belt made of watches — it was a waist of time."
   LOSES. The waist/waste pun is a classic dad joke, but it is one
   everyone has heard a hundred times — the judge weighs freshness
   third, and this one scores near zero there. Recycled shape.

B. "I asked the calendar for a day off and it said, 'Sorry, I'm
   booked solid — every single one.'"
   LOSES. The booked pun lands, but the setup eats half the line
   and the punchline needs the quotes to work; it reads slower
   out loud than it reads on the page, and "booked" puns are
   well-worn territory.

C. "I tried to start a band called 1023MB, but we never got a gig."
   LOSES. The gig/gigabyte turn is a genuine pun, but it is a
   tech joke, not a dad-at-the-dinner-table joke — a dad would
   not tell this one, and the judge's first criterion is that
   it must be a dad joke a dad would tell out loud.

D. "My ladder quit its job — it was tired of being taken for
   granted, rung after rung."
   WINS. It is a dad joke through and through: a household
   object, a complaint in a dad's voice, and the pun ("rung
   after rung" / "wrong after wrong") lands on the last two
   words, so the setup and the turn sit inside one breath.
   Fresh — the ladder-quits angle is not a recycled joke —
   and the rhythm reads cleanly out loud.

WRITING PASSES (genuine revisions to the winning line):
Pass 1: first draft was two sentences — "My ladder quit its job.
   It said it was tired of being taken for granted, rung after
   rung." Joining them with an em-dash made it one breath, so the
   punchline arrives faster; a dad joke told in one line should
   not pause for a second sentence.
Pass 2: the draft's middle read "it was sick of being walked all
   over, rung after rung" — tried and dropped. "Walked all over"
   muddies the image (nobody walks on a ladder) and the groan
   needs the complaint to be true of a ladder: being leaned on
   and taken for granted is exactly a ladder's life. "Tired of
   being taken for granted" keeps the complaint honest, so the
   pun at the end earns the groan.

Revision note (Pass 3, 26 Nov 2026): the entry line is unchanged —
   same text, same em-dash, same 82 characters. The refactor gives
   the line one home: main() now reads it through the get_entry()
   helper instead of reaching for the module constant directly, so
   the text lives in exactly one place. The existing check_gate()
   guard still validates the line (1–140 chars, non-blank, single
   line) before anything is written, and the output bytes are
   byte-identical to before.
"""

import os

ENTRY = "My ladder quit its job — it was tired of being taken for granted, rung after rung."
MAX_CHARS = 140


def get_entry():
    """Return the entry line. One home for the text: main() reads it
    through here instead of reaching for the module constant."""
    return ENTRY


def check_gate(text):
    """Mirror the sealed gate: 1-140 chars, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    text = get_entry()
    check_gate(text)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
