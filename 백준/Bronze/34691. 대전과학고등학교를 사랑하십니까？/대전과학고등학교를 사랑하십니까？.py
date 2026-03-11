import sys

answers = {
    "animal": "Panthera tigris",
    "flower": "Forsythia koreana",
    "tree": "Pinus densiflora"
}

for line in sys.stdin:
    q = line.strip()
    if q == "end":
        break
    print(answers[q])