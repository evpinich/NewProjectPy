print('===============  TASK №1 ======================================================================')

list1 = [1, 3, 4, 56, 7, 8, 25]
sum = 0
while list1:
    sum += list1.pop(0)
print(sum)

print('===============  TASK №2 ======================================================================')

a = float(input(' введіть число а у проміжку де 1<a<1.5   '))
i = 2
while ( (1+1/i) >= a):
    print(1 + 1 / i)
    i += 1

print('===============  TASK №3 ======================================================================')
list3 = [ "Su","Mn","Tu", "We", "Th", "Fr", "St"]
n = int (input(' введіть день 2023 року  -  '))+6
print ( n, "- день у 2023 це -", list3[n%7-1] )

print('===============  TASK №4 ======================================================================')

list3 = ["ojkdfddejjjjjjdseiue", "sdsfdpopwem,m", "banana", "kjkjasdssssssss", "sdsdsdsdsdsds", "sjkkjhjsidbww"]
n = input(' введіть вимвол для підрахунку кількості символів що входять в рядок -  ')
for s in list3:
    print("символ <", n, "> повторюеться ", s.count(n), " разів в рядку - ", s)

print('===============  TASK №5 ======================================================================')
list5 = [ 44, 23, 34, 56, 57, 48, 85, 76, 42, 12, 37, 99, 53, 91, 35, 86, 99]
print ( list4)
n = int(input(' введіть число для перевірки входження в список -  '))
if n in list4 :
    print ( "число - ", n, " входить в заданий список чисел")
else:
    print("число - ", n, " не входить в заданий список чисел")
