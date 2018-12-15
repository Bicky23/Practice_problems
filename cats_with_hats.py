hats = [0 for i in range(100)]

trials = len(hats)
init = 0

while init < trials:
    for i in range(len(hats)):
        if not (i+1) % (init+1):
            if hats[i] == 0:
                hats[i] = 1
            else:
                hats[i] = 0
    init += 1

answer = [i+1 for i in range(len(hats)) if hats[i] != 0]
print(answer)