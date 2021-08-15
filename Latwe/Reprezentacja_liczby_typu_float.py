# # Program zamienia liczbę dziesiętną typu float na liczbę szesnastkową
#
# def converDectToHex(decimal):
#     hexInfo = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
#
#
#     returnNumber = ""
#     while decimal > 0:
#         divisionRest = decimal % 16
#         decimal = decimal // 16
#         divisionRest = divisionRest
#         decimal = decimal
#
#         print("division rest", divisionRest)
#         print("decimal", decimal)
#
#         if divisionRest in list(hexInfo.keys()):
#             returnNumber += hexInfo[divisionRest]
#         else:
#             returnNumber += str(divisionRest)
#
#     returnNumber = returnNumber[::-1]
#     return returnNumber
#
#
#
#
# testCounter = int(input())
#
# listOfNumbers = []
#
# for test in range(testCounter):
#     listOfNumbers.append(int(input()))
#
# for number in listOfNumbers:
#     print(converDectToHex(number))


# Poniżej w miarę ok, ale wciąż wynik jest inny - zj ajkeigoś powodu jest np drugie f zamiast 8
import struct

def double_to_hex(f):
    return hex(struct.unpack('<Q', struct.pack('<d', f))[0])

double_to_hex(17.5)   # Output: '0x4031800000000000L'

# define double_to_hex as in the other answer

print(double_to_hex(-1)  ) # Output: '0x4031800000000000'
double_to_hex(-17.5)  # Output: '0xc031800000000000'


# print(bytes(hex(1)))