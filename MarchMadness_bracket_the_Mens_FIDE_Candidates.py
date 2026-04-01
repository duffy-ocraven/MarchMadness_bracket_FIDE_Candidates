# MarchMadness_bracket_candidates.py
# ~/Documents/work/dev/source/games/chess/MarchMadness_bracket_candidates.py

# Original Prompt: show me python code using character graphics to draw the Men's Chess candidates matches like a march madness bracket
# Then playing around with the indentation and truncation manually, I achieved an arrangement I liked. I then told Copilot:

# Addl prompt: I like this layout of character graphics to draw the Men's Chess candidates matches like a march madness bracket
# with a pairing at quarterfinals, pairing those winners at semifinals, and those winners meet at Final

# Sent it that entire source code version of def draw_candidates_bracket(players)
# and Addl prompt: Represent each of these Rounds as a Quarterfinal pairing the White column player vs the Black  

# followed by this table of ROUNDS 1–7 that I had drag-selected and copy-and-paste and performed EMACS comment-region upon, including Round 1 results
# ┌──────────────────────────────────────────────────────────────────────────────┐
# │                 RESULTS ROUNDS 1–7 (FIRST CYCLE)                             │
# └──────────────────────────────────────────────────────────────────────────────┘
# R Praggnanandhaa 1-0 Anish Giri
# Fabiano Caruana 1-0 Hikaru Nakamura
# Matthias Bluebaum 0-5-0.5 Wei Yi
# Javokhir Sindarov 1-0 Andrey Esipenko
# Players: Hikaru Nakamura (USA, ~2810), Fabiano Caruana (USA, ~2795), Anish Giri (Netherlands, ~2753), Praggnanandhaa R (India, ~2741),
#          Javokhir Sindarov (Uzbekistan, ~2745), Wei Yi (China, ~2754), Matthias Bluebaum (Germany, ~2722), Andrey Esipenko (FIDE, ~2720)

# Round 1 — March 29, 2026
# White 		Black
# Javokhir Sindarov	Andrey Esipenko
# Matthias Bluebaum	Wei Yi
# Praggnanandhaa R	Anish Giri
# Fabiano Caruana	Hikaru Nakamura
# Round 2 — March 30, 2026
# White 		Black
# Andrey Esipenko	Hikaru Nakamura
# Anish Giri        	Fabiano Caruana
# Wei Yi        	Praggnanandhaa R
# Javokhir Sindarov	Matthias Bluebaum
# Round 3 — March 31, 2026
# White 		Black
# Matthias Bluebaum	Andrey Esipenko
# Praggnanandhaa R	Javokhir Sindarov
# Fabiano Caruana	Wei Yi
# Hikaru Nakamura	Anish Giri
# Round 4 — April 1, 2026
# White 		Black
# Andrey Esipenko	Anish Giri
# Wei Yi        	Hikaru Nakamura
# Javokhir Sindarov	Fabiano Caruana
# Matthias Bluebaum	Praggnanandhaa R
# Round 5 — April 3, 2026
# White 		Black
# Praggnanandhaa R	Andrey Esipenko
# Fabiano Caruana	Matthias Bluebaum
# Hikaru Nakamura	Javokhir Sindarov
# Anish Giri        	Wei Yi
# Round 6 — April 4, 2026
# White 		Black
# Fabiano Caruana	Andrey Esipenko
# Hikaru Nakamura	Praggnanandhaa R
# Anish Giri        	Matthias Bluebaum
# Wei Yi        	Javokhir Sindarov
# Round 7 — April 5, 2026
# White 		Black
# Andrey Esipenko	Wei Yi
# Javokhir Sindarov	Anish Giri
# Matthias Bluebaum	Hikaru Nakamura
# Praggnanandhaa R	Fabiano Caruana

# Round | 1                 2                 3                 4
# ------+---------------------------------------------------------------------------
# Nak   | ← Caruana         → Esipenko        → Giri            → Wei Yi
# Caru  | → Nakamura        ← Giri            → Wei Yi          ← Sindarov
# Giri  | → Praggnanandhaa  → Caruana         ← Nakamura        ← Esipenko
# Pragg | → Giri            ← Wei Yi          → Sindarov        → Bluebaum
# Sinda | → Esipenko        → Bluebaum        ← Praggnanandhaa  → Caruana
# WeiYi | ← Bluebaum        ← Sindarov        ← Caruana         ← Nakamura
# Blueb | → Wei Yi          → Praggnanandhaa  → Esipenko        ← Pragg
# Esip  | ← Sindarov        ← Nakamura        ← Bluebaum        → Giri


# Round | 5                 6                 7
# ------+---------------------------------------------------------------------------
# Nak   | → Sindarov        → Pragg           ← Bluebaum
# Caru  | → Bluebaum        → Esipenko        ← Pragg
# Giri  | → Wei Yi          → Bluebaum        ← Sindarov
# Pragg | → Esipenko        → Nakamura        → Caruana
# Sinda | ← Nakamura        ← Wei Yi          → Giri            
# WeiYi | ← Giri            → Sindarov        ← Esipenko
# Blueb | ← Caruana         ← Giri            → Nakamura
# Esip  | ← Pragg           ← Caruana         → Wei Yi
# All entries above come from the official round‑by‑round schedule published for the 2026 Candidates Tournament

# 📙 Rounds 8–14 (Second Cycle)
# Rounds 8–14 repeat the same pairings with colors reversed.

players = [
    "Caruana",
    "Nakamura",
    "Wei Yi",
    "Esipenko",
    "Bluebaum",
    "Giri",
    "Sindarov",
    "Praggnanandhaa"
]
def draw_round_as_bracket(round_name, pairings):
    """
    pairings: list of 4 tuples (White, Black)
        pairings[0] = QF1
        pairings[1] = QF2
        pairings[2] = QF3
        pairings[3] = QF4
    """

    if len(pairings) != 4:
        raise ValueError("Need exactly 4 pairings")

    # Flatten into list of 8 names
    players = [pairings[0][0], pairings[0][1],
               pairings[1][0], pairings[1][1],
               pairings[2][0], pairings[2][1],
               pairings[3][0], pairings[3][1]]

    # Pad names for alignment
    width = 18
    p = [name.ljust(width) for name in players]
    empty = " " * width

    shortWidth = 9
    pTruncated = [name.lstrip().ljust(shortWidth) for name in players]

    # Truncate long names
    for i, unTruncatedName in enumerate(pTruncated):
        if unTruncatedName[8] != ' ':
            pTruncated[i] = unTruncatedName[:5].ljust(shortWidth)
        else:
            pTruncated[i] = unTruncatedName[:8].ljust(shortWidth)

    shortEmpty = " " * shortWidth

    print(f"\n===== {round_name} =====\n")

    lines = []

    # Left side: QF1, QF2 → SF1
    lines.append(f"{p[0]} ─┐")
    lines.append(f"{empty} ├─ {pTruncated[0]}─┐")
    lines.append(f"{p[1]} ─┘ {shortEmpty} │")
    lines.append(f"{empty}   {shortEmpty} ├─ {pTruncated[2]}─┐")
    lines.append(f"{p[2]} ─┐ {shortEmpty} │           │")
    lines.append(f"{empty} ├─ {pTruncated[2]}─┘           │")
    lines.append(f"{p[3]} ─┘                       │")

    # Center
    lines.append(" " * 30 + f"{shortEmpty}    ├─ Round winner")

    # Right side: QF3, QF4 → SF2
    lines.append(f"{p[4]} ─┐                       │")
    lines.append(f"{empty} ├─ {pTruncated[4]}─┐           │")
    lines.append(f"{p[5]} ─┘ {shortEmpty} │           │")
    lines.append(f"{empty}   {shortEmpty} ├─ {pTruncated[7]}─┘")
    lines.append(f"{p[6]} ─┐ {shortEmpty} │")
    lines.append(f"{empty} ├─ {pTruncated[7]}─┘")
    lines.append(f"{p[7]} ─┘")

    print("\n".join(lines))

def draw_round_showing_draws(round_name, pairings):
    """
    pairings: list of 4 tuples
        (White, Black) → no score → semifinal label = "0.5-0.5"
        (White, Black, score) → semifinal label = score
    """

    if len(pairings) != 4:
        raise ValueError("Need exactly 4 pairings")

    players = []
    sf_labels = []

    # Normalize tuples
    for tup in pairings:
        if len(tup) == 2:
            white, black = tup
            score = "0.5-0.5"
        else:
            white, black, score = tup

        players.append(white)
        players.append(black)
        sf_labels.append(score)

    # Formatting
    width = 18
    p = [name.ljust(width) for name in players]
    empty = " " * width

    shortWidth = 9
    pTruncated = [name.lstrip().ljust(shortWidth) for name in players]

    # Truncate long names
    for i, unTruncatedName in enumerate(pTruncated):
        if unTruncatedName[8] != ' ':
            pTruncated[i] = unTruncatedName[:5].ljust(shortWidth)
        else:
            pTruncated[i] = unTruncatedName[:8].ljust(shortWidth)

    shortEmpty = " " * shortWidth

    sf1, sf2, sf3, sf4 = sf_labels

    print(f"\n===== {round_name} =====\n")

    lines = []

    # LEFT SIDE — QF1, QF2 → SF1
    lines.append(f"{p[0]} ─┐")
    lines.append(f"{empty} ├─ {sf1.ljust(shortWidth)}─┐")
    lines.append(f"{p[1]} ─┘ {shortEmpty} │")
    lines.append(f"{empty}   {shortEmpty} ├─ {sf2.ljust(shortWidth)}─┐")
    lines.append(f"{p[2]} ─┐ {shortEmpty} │           │")
    lines.append(f"{empty} ├─ {sf2.ljust(shortWidth)}─┘           │")
    lines.append(f"{p[3]} ─┘                       │")

    # CENTER
    lines.append(" " * 30 + f"{shortEmpty}    ├─ Round winner")

    # RIGHT SIDE — QF3, QF4 → SF2
    lines.append(f"{p[4]} ─┐                       │")
    lines.append(f"{empty} ├─ {sf3.ljust(shortWidth)}─┐           │")
    lines.append(f"{p[5]} ─┘ {shortEmpty} │           │")
    lines.append(f"{empty}   {shortEmpty} ├─ {sf4.ljust(shortWidth)}─┘")
    lines.append(f"{p[6]} ─┐ {shortEmpty} │")
    lines.append(f"{empty} ├─ {sf4.ljust(shortWidth)}─┘")
    lines.append(f"{p[7]} ─┘")

    print("\n".join(lines))
rounds = [
    ["Round 1 — March 29, 2026", [
        ("Javokhir Sindarov", "Andrey Esipenko", "1-0"),
        ("Matthias Bluebaum", "Wei Yi"),
        ("Praggnanandhaa R", "Anish Giri", "1-0"),
        ("Fabiano Caruana", "Hikaru Nakamura", "1-0")
    ]],
    ["Round 2 — March 30, 2026", [
        ("Andrey Esipenko", "Hikaru Nakamura"),
        ("Anish Giri", "Fabiano Caruana"),
        ("Wei Yi", "Praggnanandhaa R"),
        ("Javokhir Sindarov", "Matthias Bluebaum")
    ]],
    ["Round 3 — March 31, 2026", [
        ("Matthias Bluebaum", "Andrey Esipenko"),
        ("Praggnanandhaa R", "Javokhir Sindarov", "0-1"),
        ("Fabiano Caruana", "Wei Yi", "1-0"),
        ("Hikaru Nakamura", "Anish Giri")
    ]],
    ["Round 4 — April 1, 2026", [
        ("Andrey Esipenko", "Anish Giri"),
        ("Wei Yi", "Hikaru Nakamura"),
        ("Javokhir Sindarov", "Fabiano Caruana"),
        ("Matthias Bluebaum", "Praggnanandhaa R")
    ]],
    ["Round 5 — April 2, 2026", [
        ("Praggnanandhaa R", "Andrey Esipenko"),
        ("Fabiano Caruana", "Matthias Bluebaum"),
        ("Hikaru Nakamura", "Javokhir Sindarov"),
        ("Anish Giri", "Wei Yi")
    ]],
    ["Round 6 — April 3, 2026", [
        ("Fabiano Caruana", "Andrey Esipenko"),
        ("Hikaru Nakamura", "Praggnanandhaa R"),
        ("Anish Giri", "Matthias Bluebaum"),
        ("Wei Yi", "Javokhir Sindarov")
    ]],
    ["Round 7 — April 5, 2026", [
        ("Andrey Esipenko", "Wei Yi"),
        ("Javokhir Sindarov", "Anish Giri"),
        ("Matthias Bluebaum", "Hikaru Nakamura"),
        ("Praggnanandhaa R", "Fabiano Caruana")
    ]],
    ["Round 8 — April 6, 2026", [
    ]],
    ["Round 9 — April 8, 2026", [
    ]],
    ["Round 10 — April 9, 2026", [
    ]],
    ["Round 11 — April 10, 2026", [
    ]],
    ["Round 12 — April 12, 2026", [
    ]],
    ["Round 13 — April 13, 2026", [
    ]],
    ["Round 14 — April 15, 2026", [
    ]]
]

# Addl prompt that produced ./5/: if the result score is not mentioned in the tuple, output "0.5-0.5" in place of the player at Semifinal level

# Addl prompt that produced ./6/: if the cummulative score of the two opponents when they face each other in a round is the same, then place the match at Semifinal level, and instead show at Quarterfinal level the prior decisive results of those players against other opponents they played in an earlier round 

# You’re asking for something genuinely interesting:
# a context‑aware bracket where the Semifinal connector only shows the head‑to‑head score if the two players have different cumulative scores so far, and if their cumulative scores are equal, then:

# Semifinal level shows the match itself
# Quarterfinal level shows each player’s most recent decisive result from earlier rounds
# This is no longer just formatting — it’s tournament logic.
# Let me break it down cleanly and then give you the code that does exactly what you want.

# 🎯 Your Rule, Formalized
# For each pairing in a round:

# 1. Compute each player’s cumulative score before this round
# Win = 1

# Draw = 0.5

# Loss = 0

# 2. Compare the two cumulative scores
# If different → Semifinal label = actual match score (or "0.5-0.5" if missing)

# If equal →

# Semifinal label = the match itself (score or "0.5-0.5")

# Quarterfinal label = each player’s most recent decisive result

# If the player has no decisive result yet → "="

# If the player won last decisive game → "W"

# If the player lost last decisive game → "L"

# This is exactly what you described.

# then it asked for:
# Just confirm the QF label format and I’ll deliver the full working system.

# prefer something else (e.g., "  1-0  ", "  0-1  ", "0.5-0.5")
# I'm sorry, I'm having trouble responding to requests right now. Let's try this again in a bit.

# Quarterfinal labels be "W", "L", "=" as shown
# Perfect — now that you’ve confirmed Quarterfinal labels should be "W", "L", "="

# Example A — replace labels:
# or
# Example B — append labels:

# Code
# Fabiano Caruana (W) ─┐
# Hikaru Nakamura (L) ─┘
# Both are easy — I just need to know which style you prefer so the ASCII layout stays clean.

# Tell me A (replace) or B (append) and I’ll deliver the full implementation.

# A (replace)
# Excellent — with A (replace) confirmed, we can now finalize the full logic and build the upgraded bracket engine.

# You’re going to like how cleanly this comes together.

# 🎯 Final Behavior (Locked In)
# For each pairing in a round:

# 1. Compute cumulative scores BEFORE the round
# Win = 1

# Draw = 0.5

# Loss = 0

# 2. Compare cumulative scores
# Case A — Scores DIFFER
# Quarterfinal level → show player name (normal)

# Semifinal level → show match score (or "0.5-0.5")

# Case B — Scores EQUAL
# Semifinal level → show match score (or "0.5-0.5")

# Quarterfinal level → show decisive result label:

# Player’s last decisive result	QF label
# Win	"W"
# Loss	"L"
# No decisive result yet	"="

# And because you chose A (replace):

# Quarterfinal level replaces the player name entirely
# Example:

# Code
# W ─┐
# L ─┘
# 🧠 Before I generate the full implementation…
# I need one last tiny detail so the code is 100% correct:

# ❓ When cumulative scores are equal, and we replace the player name with "W", "L", or "=",
# should the replacement be padded to the same width as names?
# Your bracket uses:

# Code
# width = 14
# So should "W" become:

# Code
# "W             "   (left‑justified to width 14)
# Or should it remain a single character?

# Option 1 — padded (keeps bracket alignment perfect)
# Code
# W              ─┐
# L              ─┘
# Option 2 — not padded (more compact, but shifts ASCII alignment)
# Code
# W ─┐
# L ─┘
# Your original bracket is very alignment‑sensitive, so I want to match your aesthetic exactly.

# 👉 Which do you prefer?
# 1 — padded to width 14
# 2 — single character, not padded
# Tell me the number, and I’ll deliver the full working code with:

# cumulative score tracking

# decisive result tracking

# equal‑score logic

# your exact ASCII bracket layout

# support for all 7 rounds

# Ready when you are.

# 1 — padded to width 14
# See my thinking
# I'm sorry, I'm having trouble responding to requests right now. Let's try this again in a bit.

# 1 — padded to width 14, and proceed to show the code

# ============================================================
#   SCORE + DECISIVE RESULT TRACKER
# ============================================================

def result_value(score_str):
    """Convert '1-0', '0-1', '0.5-0.5' into numeric score for White."""
    if score_str == "1-0":
        return 1.0, 0.0
    if score_str == "0-1":
        return 0.0, 1.0
    return 0.5, 0.5  # default draw


def update_scores_and_history(pairings, cumulative, history):
    """Update cumulative scores and decisive history after a round."""
    for white, black, *rest in pairings:
        score = rest[0] if rest else "0.5-0.5"
        w_score, b_score = result_value(score)

        cumulative[white] += w_score
        cumulative[black] += b_score

        # Track decisive results only (ignore draws)
        if score == "1-0":
            history[white].append("W")
            history[black].append("L")
        elif score == "0-1":
            history[white].append("L")
            history[black].append("W")
        else:
            history[white].append("=")
            history[black].append("=")


def last_decisive(history_list):
    """Return last decisive result: W, L, or =."""
    for r in reversed(history_list):
        if r in ("W", "L"):
            return r
    return "="  # no decisive result yet
        

# ============================================================
#   BRACKET DRAWER WITH YOUR RULES
# ============================================================

def draw_round_pairing_equals(round_name, pairings, cumulative_before, history):
    """
    pairings: list of 4 tuples (White, Black) or (White, Black, Score)
    """

    # Build QF and SF labels
    qf_labels = []
    sf_labels = []
    players = []

    for white, black, *rest in pairings:
        score = rest[0] if rest else "0.5-0.5"

        # cumulative scores BEFORE this round
        w_cum = cumulative_before[white]
        b_cum = cumulative_before[black]

        # equal cumulative scores?
        equal = abs(w_cum - b_cum) < 1e-9

        # semifinal label always the score
        sf_labels.append(score)

        if equal:
            # replace names with decisive labels
            w_label = white + last_decisive(history[white])
            b_label = black + last_decisive(history[black])
        else:
            # normal: show names
            w_label = white
            b_label = black

        qf_labels.append(w_label)
        qf_labels.append(b_label)
        players.append(white)
        players.append(black)

    # Formatting
    width = 18
    p = [label.ljust(width) for label in qf_labels]
    empty = " " * width

    shortWidth = 9
    sf = [s.ljust(shortWidth) for s in sf_labels]
    shortEmpty = " " * shortWidth

    print(f"\n===== {round_name} =====\n")

    lines = []
#debug_print
    if (0 == len(p)):
      print(f'{qf_labels}')
      return
    # LEFT SIDE — QF1, QF2 → SF1
    lines.append(f"{p[0]} ─┐")
    lines.append(f"{empty} ├─ {sf[0]}─┐")
    lines.append(f"{p[1]} ─┘ {shortEmpty} │")
    lines.append(f"{empty}   {shortEmpty} ├─ {sf[1]}─┐")
    lines.append(f"{p[2]} ─┐ {shortEmpty} │           │")
    lines.append(f"{empty} ├─ {sf[1]}─┘           │")
    lines.append(f"{p[3]} ─┘                       │")

    # CENTER
    lines.append(" " * 30 + f"{shortEmpty}    ├─ Round winner")

    # RIGHT SIDE — QF3, QF4 → SF2
    lines.append(f"{p[4]} ─┐                       │")
    lines.append(f"{empty} ├─ {sf[2]}─┐           │")
    lines.append(f"{p[5]} ─┘ {shortEmpty} │           │")
    lines.append(f"{empty}   {shortEmpty} ├─ {sf[3]}─┘")
    lines.append(f"{p[6]} ─┐ {shortEmpty} │")
    lines.append(f"{empty} ├─ {sf[3]}─┘")
    lines.append(f"{p[7]} ─┘")

    print("\n".join(lines))


# ============================================================
#   RUN ALL ROUNDS
# ============================================================

def run_all_rounds(rounds):
    # Initialize cumulative scores and history
    players = set()
    for _, pairings in rounds:
        for tup in pairings:
            players.add(tup[0])
            players.add(tup[1])

    cumulative = {p: 0.0 for p in players}
    history = {p: [] for p in players}

    for round_name, pairings in rounds:
        # snapshot BEFORE round
        cumulative_before = cumulative.copy()

        # draw bracket
#debug_print
#        print(f'{round_name}, {pairings}\n{cumulative_before}, {history}')
        draw_round_pairing_equals(round_name, pairings, cumulative_before, history)

        # update scores AFTER round
        update_scores_and_history(pairings, cumulative, history)

# commented-out invocatin of the older styling
# for rdNum, roundPairings in enumerate(rounds):
#   round_name, pairings = roundPairings
#   if (0 < len(pairings)):
#     draw_round_showing_draws(round_name, pairings)
#   else:
#     draw_round_as_bracket(round_name, [(black, white) for white, black, *_ in rounds[rdNum - 7][1]])

run_all_rounds(rounds)

