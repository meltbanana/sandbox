import re
import collections
import csv
import matplotlib.pyplot as plt
from math import log

with open('onegin.txt', encoding='utf-8') as fsrc:
    words = re.findall(r'\w+', fsrc.read().lower())
    counter = collections.Counter(words)
    print(counter.most_common(10))

    with open("onegin_words.txt", "w+", encoding='utf-8', newline="") as fdest:
        writer = csv.writer(fdest)
        for key, value in dict(counter).items():
            writer.writerow([key, value])
        fdest.close()

    frequences = sorted(dict(counter).values(), reverse = True)
    x, y = zip(*enumerate(frequences, 1))
    x = [log(i) for i in x]
    y = [log(i) for i in y]

    plt.plot(x, y)
    plt.show()

