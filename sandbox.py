end_dic = {0:'тов', 1: 'т'}
end_dic.update({x: 'та' for x in range(2,5)})
end_dic.update({x: 'тов' for x in range(5,21)})

try:
    x = int(input("Введите целое число программистов :"))
    print (x,'программис'+end_dic[x%100] if x%100 in end_dic else end_dic[x%10])

except ValueError:
    print("Ошибка, нужно было ввести целое число, попробуйте еще раз.")