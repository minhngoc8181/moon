nText = input()
occurs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_sum = 0

for c in nText:
    total_sum += int(c)
    occurs[int(c)] += 1

if total_sum % 9 != 0:
    print(-1)
elif nText == "0":
    print(0)
else:
    candidates = []
    for i in range(9, -1, -1):
        for j in range(9, i - 1, -1):
            if (10 * i + j) % 4 == 0 or (10 * j + i) % 4 == 0:
                state = occurs[:]
                state[i] -= 1
                state[j] -= 1
                if state[i] >= 0 and state[j] >= 0:
                    found_k = False
                    k_val = ""
                    
                    for k in range(1, 10):
                        if state[k] > 0:
                            state[k] -= 1
                            k_val = str(k)
                            found_k = True
                            break
                            
                    if found_k or len(nText) == 2:
                        candidate = k_val
                        for l in range(0, 10):
                            candidate += str(l) * state[l]
                            
                        if (10 * i + j) % 4 == 0:
                            candidates.append(candidate + str(i) + str(j))
                        if i != j and (10 * j + i) % 4 == 0: 
                            candidates.append(candidate + str(j) + str(i))
                            
    if len(candidates) > 0:
        print(min(candidates))
    else:
        print(-1)