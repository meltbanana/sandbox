import re
import collections
import csv

with open('onegin.txt', encoding='utf-8') as fsrc:
    words = re.findall(r'\w+', fsrc.read().lower())
    counter = collections.Counter(words)
    print(counter.most_common(10))

    with open("onegin_words.txt", "w+", encoding='utf-8', newline="") as fdest:
        writer = csv.writer(fdest)
        for key, value in dict(counter).items():
            writer.writerow([key, value])
        fdest.close()
