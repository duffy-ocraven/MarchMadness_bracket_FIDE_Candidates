# MarchMadness_bracket_candidates.txt
# ~/Documents/work/dev/source/games/chess/MarchMadness_bracket_candidates.txt

# Original Prompt: show me python code using character graphics to draw the Men's Chess candidates matches like a march madness bracket

# Starting afresh prompt: I like this layout of character graphics to draw the Men's Chess candidates matches like a march madness bracket
# with a pairing at quarterfinals, pairing those winners at semifinals, and those winners meet at Final

# ./3/QFSFFinal.py version of def draw_candidates_bracket(players):

# Represent each of these Rounds as a Quarterfinal pairing the White column player vs the Black  

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
rounds = [
    ["Round 1 — March 29, 2026", [
        ("Javokhir Sindarov", "Andrey Esipenko"),
        ("Matthias Bluebaum", "Wei Yi"),
        ("Praggnanandhaa R", "Anish Giri"),
        ("Fabiano Caruana", "Hikaru Nakamura")
    ]],
    ["Round 2 — March 30, 2026", [
        ("Andrey Esipenko", "Hikaru Nakamura"),
        ("Anish Giri", "Fabiano Caruana"),
        ("Wei Yi", "Praggnanandhaa R"),
        ("Javokhir Sindarov", "Matthias Bluebaum")
    ]],
    ["Round 3 — March 31, 2026", [
        ("Matthias Bluebaum", "Andrey Esipenko"),
        ("Praggnanandhaa R", "Javokhir Sindarov"),
        ("Fabiano Caruana", "Wei Yi"),
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
for rdNum, roundPairings in enumerate(rounds):
  round_name, pairings = roundPairings
  if (0 < len(pairings)):
    draw_round_as_bracket(round_name, pairings)
  else:
    draw_round_as_bracket(round_name, [(black, white) for white,black in rounds[rdNum - 7][1]])
