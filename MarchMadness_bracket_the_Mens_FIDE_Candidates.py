# show me python code using character graphics to draw the Men's Chess candidates matches like a march madness bracket
# with a pairing at quarterfinals, pairing those winners at semifinals, and those winners meet at Final

def draw_candidates_bracket(players):
    """
    players: list of 8 player names in quarterfinal order:
        QF1: players[0] vs players[1]
        QF2: players[2] vs players[3]
        QF3: players[4] vs players[5]
        QF4: players[6] vs players[7]
    """
    if len(players) != 8:
        raise ValueError("Need exactly 8 players")

    # Pad names for nicer alignment
    width = 14
    p = [name.ljust(width) for name in players]
    empty = " " * width
    shortWidth = 9
    pTruncated = [name.ljust(shortWidth) for name in players]
    for i, unTruncatedName in enumerate(pTruncated):
      if (' ' != unTruncatedName[8]):
        pTruncated[i] = unTruncatedName[:5].ljust(shortWidth)
    shortEmpty = " " * shortWidth
    offset = "" # right side QF is placed directly below left side QF

    lines = []

    # Left side: QF1, QF2 → SF1
    lines.append(f"{p[0]} ─┐")
    lines.append(f"{empty} ├─ {pTruncated[0]}─┐")
    lines.append(f"{p[1]} ─┘ {shortEmpty} │")
    lines.append(f"{empty}   {shortEmpty} ├─ {pTruncated[2]}─┐")
    lines.append(f"{p[2]} ─┐ {shortEmpty} │           │")
    lines.append(f"{empty} ├─ {pTruncated[2]}─┘           │")
    lines.append(f"{p[3]} ─┘                       │")

    lines.append(" " * 26 + f"{shortEmpty}    ├─ Final winner")

    # Right side: QF3, QF4 → SF2
    lines.append(f"{offset}{p[4]} ─┐                       │")
    lines.append(f"{offset}{empty} ├─ {pTruncated[4]}─┐           │")
    lines.append(f"{offset}{p[5]} ─┘ {shortEmpty} │           │")
    lines.append(f"{offset}{empty}   {shortEmpty} ├─ {pTruncated[7]}─┘")
    lines.append(f"{offset}{p[6]} ─┐ {shortEmpty} │")
    lines.append(f"{offset}{empty} ├─ {pTruncated[7]}─┘")
    lines.append(f"{offset}{p[7]} ─┘")

    print("\n".join(lines))


if __name__ == "__main__":
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
    draw_candidates_bracket(players)
