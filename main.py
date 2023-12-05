import json
# ----------------------------------------------------------------------------
row_value = {
    'perm': {'fkOtherParameter': '84',
             'fkLifeCycleTs': '14',
             'fkDataQuality': '85',
             'fkHistoricCompany': '33',
             'fkOilAndGas': '12'},
    'parentId': -7124,
    'props': {'lifeCycleDetailTs': 'Producing >75%',
              'lifeCycleCategoryTs': 'Producing',
              'lifeCycleDetail': 'Producing >75%',
              'historicCompany': 'Petronas',
              'dataType': 'Modeled'}
}
schema = {
    'keys': [
        {'keyType': 'STRING', 'name': 'FK Asset'},
        {'keyType': 'INT', 'name': 'FK Other Parameter'},
        {'keyType': 'INT', 'name': 'FK Oil And Gas'},
        {'keyType': 'INT', 'name': 'FK Historic Company'},
        {'keyType': 'INT', 'name': 'FK Life Cycle TS'},
        {'keyType': 'INT', 'name': 'FK Life Cycle'},
        {'keyType': 'STRING', 'name': 'FK Company'},
        {'keyType': 'INT', 'name': 'FK Economics Type'},
        {'keyType': 'INT', 'name': 'FK Data Quality'},
        {'keyType': 'INT', 'name': 'FK Oil And Gas Type'},
        {'keyType': 'STRING', 'name': 'Time Series Name'},
        {'keyType': 'STRING', 'name': 'Commerciality'},
        {'keyType': 'STRING', 'name': 'Entitlement'},
        {'keyType': 'STRING', 'name': 'Green Brown Field'},
        {'keyType': 'STRING', 'name': 'Minority Interest'},
        {'keyType': 'STRING', 'name': 'Oil And Gas Category'},
        {'keyType': 'STRING', 'name': 'Oil And Gas Group'},
        {'keyType': 'STRING', 'name': 'Oil And Gas Detail'},
        {'keyType': 'STRING', 'name': 'Historic Company'},
        {'keyType': 'STRING', 'name': 'Historical Company Segment'},
        {'keyType': 'STRING', 'name': 'Historical Company Subsegment'},
        {'keyType': 'STRING', 'name': 'Life Cycle Category TS'},
        {'keyType': 'STRING', 'name': 'Life Cycle Detail TS'},
        {'keyType': 'STRING', 'name': 'Life Cycle Group TS'},
        {'keyType': 'STRING', 'name': 'Life Cycle Detail'},
        {'keyType': 'STRING', 'name': 'Life Cycle Category'},
        {'keyType': 'STRING', 'name': 'Life Cycle Group'},
        {'keyType': 'STRING', 'name': 'Economics Group'},
        {'keyType': 'STRING', 'name': 'Economics Category'},
        {'keyType': 'STRING', 'name': 'Data Confidence'},
        {'keyType': 'STRING', 'name': 'Data Source'},
        {'keyType': 'STRING', 'name': 'Data Type'},
        {'keyType': 'STRING', 'name': 'Oil And Gas Type Detail'},
        {'keyType': 'STRING', 'name': 'Currency'},
        {'keyType': 'STRING', 'name': 'Frequency'}
    ]
}
#  convert input dict to one level dict with lowercase of key ----------------

row_value_as_one_level_dict = row_value['perm'] | row_value['props']
list_of_key_from_row_value = [key.casefold() for key in row_value_as_one_level_dict.keys()]
list_of_value_from_row_value = list( row_value_as_one_level_dict.values())
row_value_dict = dict(zip(list_of_key_from_row_value, list_of_value_from_row_value))
print(row_value_dict)

#  convert  row_value_dict according to schema -------------------------------

schema_to_list = schema['keys']

print(' ****************************  OUTPUT *******************************')
for nested_dict in schema_to_list:
    if nested_dict['name'].replace(" ","").casefold() in row_value_dict:
        nested_dict['keyType'] = row_value_dict[nested_dict ['name'].replace(" ","").casefold()]
    else:
        nested_dict['keyType'] = 1 if nested_dict['keyType'] == 'INT' else " "
    print(nested_dict)

#  convert to json format and saving to file ---------------------------------

json_dict = {'keys': schema_to_list}
with open("output.json", "w") as outfile:
    json.dump(json_dict, outfile)

# HW dict
# Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами значения первого и последнего элемент объекта. Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
# Как получить значение по ключу "marks" словаря student = {"name": "Emma", "class": 9, "marks": 75}
# Что выведет этот код?
# p = {"name": "Mike", "salary": 8000} print(p.get("age")).
#
# Как получить "d": sample = {"1":["a","b"], "2":["c","d"]}.
# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
# Дано
# list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
# list_2 = ["Киев", "Токио", "Минск"]
# Получить
# dict_ = ["Украина": "Киев", "Япония": "Токио", "Беларусь": "Минск"]

# Сгенерировать словарь-шифратор, то есть словарь, где ключ и значение являются символами. Используя словарь, зашифровать/расшифровать введенное сообщение.
# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
# Создайте словарь из строки следующим образом: в качестве ключей возьмите буквы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
# Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.). Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось количество учащихся, б) в школе появился новый класс, с) в школе был расформирован (удален) другой класс. Вычислите общее количество учащихся в школе.
# Создайте словарь, где ключами являются числа, а значениями – строки. Создайте функционал которий вернет новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями – числа.


























# print('===============  TASK №1 ======================================================================')
#
# list1 = [1, 3, 4, 56, 7, 8, 25]
# sum = 0
# while list1:
#     sum += list1.pop(0)
# print(sum)
#
# print('===============  TASK №2 ======================================================================')
#
# a = float(input(' введіть число а у проміжку де 1<a<1.5   '))
# i = 2
# while ( (1+1/i) >= a):
#     print(1 + 1 / i)
#     i += 1
#
#
# print('===============  TASK №3 ======================================================================')
# list3 = [ "Su","Mn","Tu", "We", "Th", "Fr", "St"]
# n = int (input(' введіть день 2023 року  -  '))+6
# print ( n, "- день у 2023 це -", list3[n%7-1] )
#
# print('===============  TASK №4 ======================================================================')
#
# list3 = ["ojkdfddejjjjjjdseiue", "sdsfdpopwem,m", "banana", "kjkjasdssssssss", "sdsdsdsdsdsds", "sjkkjhjsidbww"]
# n = input(' введіть вимвол для підрахунку кількості символів що входять в рядок -  ')
# for s in list3:
#     print("символ <", n, "> повторюється ", s.count(n), " разів в рядку - ", s)
#
# print('===============  TASK №5 ======================================================================')
# list5 = [ 44, 23, 34, 56, 57, 48, 85, 76, 42, 12, 37, 99, 53, 91, 35, 86, 99]
# print ( list5)
# n = int(input(' введіть число для перевірки входження в список -  '))
# if n in list5 :
#     print ( "число - ", n, " входить в заданий список чисел")
# else:
#     print("число - ", n, " не входить в заданий список чисел")
#
# print('===============  TASK № 2.1 ======================================================================')
# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
#
# list_resolt = list(zip(list_a,list_b))
# print(list_resolt)
#
#
# print('===============  TASK № 2.2 ======================================================================')
# list_d = ["bar", "baz", "qux", "etc"]
# tuple_d = ("foo",*list_d)
# print(tuple_d)
