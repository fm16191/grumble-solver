import os
import numpy as np


def score(string):
    scores = {
        "b": 3,
        "c": 3,
        "d": 2,
        "f": 4,
        "g": 2,
        "h": 4,
        "j": 8,
        "m": 2,
        "p": 3,
        "q": 8,
        "v": 4,
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
    print(f"Usage : {argv[0]} \"abcdagieetloeurm\"")
    exit()

letters = []
counts = []

for l in argv[1]:
    if not l in letters:
        letters.append(l)
        counts.append(1)
    else:
        counts[letters.index(l)] += 1

# letters = "".join([argv[1][i] for i in range(0, len(argv[1]), 2)])
# counts = "".join([argv[1][i + 1] for i in range(0, len(argv[1]), 2)])
# cc = np.array([int(i) for i in counts], dtype=np.int8).sum()
counts = np.array(counts)

if counts.sum() != 16:
    print(f"It must be missing {16-counts.sum()} letter(s) ... ")
    for i in range(len(letters)):
        print(counts[i], letters[i])
    exit()

alphabet = "abcdefghijklmnopqrstuvwxyz"
unused_letters = alphabet

for l in letters:
    unused_letters = unused_letters.replace(l, "")

maxs = []
for i, l in enumerate(letters):
    if l == "e":
        l = "[e|é|è|ê]"
    elif l == "i":
        l = "[i|î]"
    elif l == "a":
        l = "[a|à|â]"
    elif l == "u":
        l = "[u|ù|û]"
    elif l == "o":
        l = "[o|ô]"
    maxs.append(f"({l}.*){{{int(counts[i])+1}}}")

# Print longuest words : awk '{{ print length(), $0 | "sort -n" }}'
command = f"""grep -Ev "{"|".join(unused_letters)}" dictionary.csv | grep -Ev "\.|-| |\'|’" | grep -Ev "{"|".join(maxs)}" """
# Explanation :
# 1. grep  Invert search to exclude all words with non used letters of dictionnary.csv
# 2. sed   Remove all dictionnary artifacts, that are not actual acceptable words
# 3. grep  Specify the max amount of occurences per used letters

p = os.popen(command)
result = p.read()
p.close()

words = np.array(result.split("\n"))
# words = np.array(np.char.split(np.array([result]))[0])

tab = np.empty(len(words), dtype=np.uint8)
for i, res in enumerate(words):
    tab[i] = score(res)

# Print last 300 best words & their score
tab_sort = tab.argsort()[-300:]
w = words[tab_sort]
t = tab[tab_sort]
for i, res in enumerate(w):
    print(t[i], res)
