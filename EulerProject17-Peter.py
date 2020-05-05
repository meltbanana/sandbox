dic = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
    }


def textout(num):
    str = ''
    if num//10 == 0:
        str = dic[num]
    elif num//100 == 0:
        if num<20:
            str = dic[num]
        else:
            str = dic[num//10*10]
            rest = num-num//10*10
            if rest!=0: str += textout(rest)
    elif num//1000 == 0:
        str = dic[num//100]
        str += dic[100]
        rest = num-num//100*100
        if rest!=0: str += 'and' + textout(rest)
    else:
        str = dic[1] + dic[1000]

    return str


lst = [len(textout(i)) for i in range(1,1001)]
print(sum(lst))
