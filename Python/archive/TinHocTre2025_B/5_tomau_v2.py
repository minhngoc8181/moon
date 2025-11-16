import sys

def ask(cells):
    if not cells:
        print("? 0")
        sys.stdout.flush()
        return int(sys.stdin.readline().strip())
    out = ["? {}".format(len(cells))]
    for r, c in cells:
        out.append(str(r)); out.append(str(c))
    print(" ".join(out))
    sys.stdout.flush()
    return int(sys.stdin.readline().strip())

def rectocells(recs, size):
    return [(r + i, c + j) for r, c in recs for i in range(size) for j in range(size)]

def findcandidate(recs, size, K):
    if size == 1:
        return rectocells(recs, 1), K  # K is number of blacks among these 8 cells

    new_size = size // 2
    subrecs1, subrecs2 = [], []
    for r, c in recs:
        subrecs1.append((r, c))
        subrecs1.append((r + new_size, c + new_size))
        subrecs2.append((r, c + new_size))
        subrecs2.append((r + new_size, c))

    cells1 = rectocells(subrecs1, new_size)
    a = ask(cells1)          # blacks in subrecs1
    # choose the heavier half by blacks, not by area
    if a * 2 >= K:
        return findcandidate(subrecs1, new_size, a)
    else:
        return findcandidate(subrecs2, new_size, K - a)

def solveone():
    # 3 queries to isolate 8 cells with >=5 blacks
    cells, K8 = findcandidate([(1, 1)], 8, 33)

    chosen = []
    # three pair-queries on first 6 cells
    for i in range(0, 6, 2):
        ans = ask(cells[i:i+2])
        if ans == 2:
            chosen.extend(cells[i:i+2])
        elif ans == 1:
            ans_sub = ask(cells[i:i+1])
            if ans_sub == 1:
                chosen.append(cells[i])
            else:
                chosen.append(cells[i+1])
        if len(chosen) >= 5:
            break

    if len(chosen) < 5:
        if len(chosen) == 3:
            # need both from the last pair to reach at least 5
            chosen.extend(cells[6:8])
        elif len(chosen) == 4:
            # need exactly one from the last pair
            ans_sub = ask(cells[6:7])
            if ans_sub == 1:
                chosen.append(cells[6])
            else:
                chosen.append(cells[7])

    chosen = chosen[:5]
    out = ["!"]
    for r, c in chosen:
        out.append(str(r)); out.append(str(c))
    print(" ".join(out))
    sys.stdout.flush()

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        solveone()

if __name__ == "__main__":
    main()
