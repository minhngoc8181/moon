nText = input()
occurs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum = 0
for c in nText:
    sum += int(c)
    occurs[int(c)] += 1

if sum % 9 != 0:
    print(-1)
elif nText == "0":
    print(0)
elif nText in ["27", "36", "63", "72"]:
    a, b = map(int, nText)
    if (10 * a + b) % 36 == 0:
        print(str(a) + str(b))
    else:
        print(str(b) + str(a))
else:
    found = False
    for i in range(1, 10):
        if occurs[i] > 0 and found == False:
            state = occurs[::]
            state[i] -= 1
            for j in range(9, -1, -1):
                if found != False:
                    break
                for k in range(9, j - 1, -1):
                    if (j == k and state[j] >= 2 and (j * 10 + k) % 4 == 0) or (
                        j != k
                        and state[j] >= 1
                        and state[k] >= 1
                        and ((j * 10 + k) % 4 == 0 or (k * 10 + j) % 4 == 0)
                    ):
                        state[j] -= 1
                        state[k] -= 1
                        ans = str(i)
                        for l in range(0, 10):
                            if state[l] > 0:
                                ans += str(l) * state[l]
                        if (j * 10 + k) % 4 == 0:
                            ans += str(j) + str(k)
                        else:
                            ans += str(k) + str(j)
                        print(ans)
                        found = True
                        break
    if found == False:
        print(-1)
