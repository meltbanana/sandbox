# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?



source  = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 0: ''}

dict = {}
sum = 0

for units in range (1, 20):
    dict[units] = source[units]

for decimals in range (20, 100):
    dict[decimals] = source[(decimals // 10) * 10] + source[decimals % 10]

for x in range(1, 100):
    # print(dict[x], len(dict[x]))
    sum += len(dict[x])
# print(sum)
# 99 ready = 854
# * 10 = 8540

ones = 0
for x in range(1,10):
    ones += len(source[x])

# one/two/three ..  = 36 * 100 = 3600 for hundreds
# "hundred and" * 99 * 9
# 9 "hundred"
# + one thousand

ones = ones * 100 + len("hundredand") * 99 * 9 + len("hundred") * 9 + len("onethousand")

result = sum * 10 + ones
print(result)