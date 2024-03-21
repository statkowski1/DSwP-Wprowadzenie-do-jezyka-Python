import sys

#Zadanie 6

number2 = sys.stdin.readline()
print("Podaną liczbę można zapisać jako: ", end="")
result = ""
for x in range(0, len(number2)-1):
    result += str(10 ** (len(number2) - x - 2)) + " * " + str(number2[x])
    if len(number2) - 2 > x:
        result += " + "
sys.stdout.write(result)
