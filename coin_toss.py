from random import randint as i

flips = 0
trials = 10000

for _ in range(trials):
    flips += 1
    if i(0,1) == 0:
        flips += 1
        while i(0,1) == 0:
            flips += 1
    else:
        flips += 1
        while i(0,1) == 1:
            flips += 1

print(flips/trials)