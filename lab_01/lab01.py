#Zadanie 1

int1 = int(17)
int2 = int('1110', 2)

float1 = float(5.87)
float2 = float('4.047e11')

print(int1)
print(int2)
print(float1)
print(float2)

#Zadanie 2

number = 29
bit_count = number.bit_count()
print(f"Liczba bitów dla {number} wynosi: {bit_count}")

variable1 = 7.0
variable2 = 7.9401
print(f"Czy {variable1} to liczba całkowita? {variable1.is_integer()}")
print(f"Czy {variable2} to liczba całkowita? {variable2.is_integer()}")

#Zadanie 3

number2 = 43
decimal_to_binary = bin(number2)
print(f"Liczba dziesiętna {number2} w postaci binarnej wynosi: {decimal_to_binary}")
binary_to_decimal = int(decimal_to_binary, 2)
print(f"Liczba binarna {decimal_to_binary} w postaci dziesiętnej wynosi: {binary_to_decimal}")

#Zadanie 4

number3 = 150
number4 = 23
print("a = ", number3)
print("b = ", number4)
print("bin(a) = ", bin(number3))
print("bin(b) = ", bin(number4))
print()
print("a & b = ", number3 & number4)
print("bin(a & b) = ", bin(number3 & number4))
print()
print("a | b = ", number3 | number4)
print("bin(a | b) = ", bin(number3 | number4))
print()
print("a ^ b = ", number3 ^ number4)
print("bin(a ^ b) = ", bin(number3 ^ number4))
print()
print("a << b = ", number3 << number4)
print("bin(a << b) = ", bin(number3 << number4))
print()
print("a >> b = ", number3 >> number4)
print("bin(a >> b) = ", bin(number3 >> number4))

#Zadanie 5

number5 = 1.618
float_to_hex = number5.hex()
print(f"Liczba {number5} w postaci heksadecymalna wynosi {float_to_hex}")
hex_to_float = float.fromhex(float_to_hex)
print(f"Liczba heksadecymalna {float_to_hex} wynosi: {hex_to_float}")
