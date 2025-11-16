import sys


def ask(cells):
    if not cells:
        print("? 0")
        sys.stdout.flush()
        return int(sys.stdin.readline().strip())
    out = ["? {}".format(len(cells))]
    for r, c in cells:
        out.append(str(r))
        out.append(str(c))
    print(" ".join(out))
    sys.stdout.flush()
    return int(sys.stdin.readline().strip())


def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        matchings = []
        for k in range(8):
            mk = []
            for r in range(1, 9):
                c = ((r - 1 + k) % 8) + 1
                mk.append((r, c))
            matchings.append(mk)

        best_k = 0
        best_sum = -1
        for k in range(8):
            s = ask(matchings[k])
            if s > best_sum:
                best_sum = s
                best_k = k
            if s >= 5:
                break

        cells = matchings[best_k]
        chosen = []
        for r, c in cells:
            if len(chosen) == 5:
                break
            z = ask([(r, c)])
            if z > 0:
                chosen.append((r, c))

        out = ["!"]
        for r, c in chosen:
            out.append(str(r))
            out.append(str(c))
        print(" ".join(out))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
