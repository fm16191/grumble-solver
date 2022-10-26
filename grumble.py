import os
import numpy as np


def score(string):
    scores = {
        "c": 3,
        "d": 2,
        "j": 8,
        "v": 4,
        "m": 2,
        "p": 3,
        "q": 8,
    }

    sc = 0
    for l in string:
        if l in scores:
            sc = sc + scores[l]
        else:
            sc = sc + 1
    return sc


from sys import argv
if len(argv) <= 1:
    print(f"Usage : {argv[0]} \"a2c3b1e5\"")
    exit()

letters = "".join([argv[1][i] for i in range(0, len(argv[1]), 2)])
counts = "".join([argv[1][i + 1] for i in range(0, len(argv[1]), 2)])

cc = np.array([int(i) for i in counts], dtype=np.int8).sum()
if cc != 16:
    print(f"It must be missing {16-cc} letter(s) ... ")
    for i in range(len(letters)):
        print(counts[i], letters[i])

alphabet = "abcdefghijklmnopqrstuvwxyz"
uletters = alphabet
# print(letters)
for l in letters:
    uletters = uletters.replace(l, "")

maxs = []
for i, l in enumerate(letters):
    if l == "e":
        l = "[e|é|è|ê]"
    elif l == "i":
        l = "[i|î]"
    elif l == "a":
        l = "[a|à|â]"
    maxs.append(f"({l}.*){{{int(counts[i])+1}}}")

#  | awk '{{ print length(), $0 | "sort -n" }}'
command = f"""cat dictionary.csv | grep -Ev "{"|".join(uletters)}" | sed "/\'.*/d;/’.*/d" | sed "s/ .*//g" | grep -Ev "{"|".join(maxs)}" """

print(command)

p = os.popen(command)
result = p.read()
p.close()

words = np.array(result.split("\n"))

tab = np.empty(len(words), dtype=np.int8)
for i, res in enumerate(words):
    tab[i] = score(res)

for i, res in enumerate(words[tab.argsort()][-300:]):
    print(tab[tab.argsort()][-300:][i], res)
