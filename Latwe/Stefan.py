import sys

data = sys.stdin

citiesCount = int(data.readline())

incomeList = []

counter = 0
max = 0

for city in range(citiesCount):
    income = int(data.readline())
    counter += income
    if counter > max:
        max = counter
    if counter < 0:
        counter = 0
print(max)
# tourBegin = []
#
# max = 0
# while incomeList:
#     try:
#         tourBegin.append(incomeList.pop(0))
#     except:
#         pass
#     # try:
#     #     tourEnd.append(incomeList.pop(-1))
#     # except:
#     #     pass
#     if sum(tourBegin) > max:
#         max = sum(tourBegin)
#     if sum(tourBegin) < 0:
#         tourBegin = []
#
#     # if sum(tourEnd) < 0:
#     #     tourEnd = []
#
# # maxIncomeList = tourBegin + tourEnd
# print(max)