from struct import calcsize
from turtle import clear


class Calculator:
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
        
    def adder(self):
        result = self.x + self.y
        return result

    def subtractor(self):
        result = self.x - self.y
        return result

    def multiplier(self):
        result = self.x * self.y
        return result

    def divider(self):
        result = self.x / self.y
        return result

    def clear(self):
        self.x = self.y = 0

x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))

getValue = Calculator(x, y)

add = getValue.adder()
print('Addition of x and y result: ', add)

sub = getValue.subtractor()
print('Substration of x and y result: ', sub)

mul = getValue.multiplier()
print('Multiplication of x and y result: ', mul)

div = getValue.divider()
print('Division of x and y result: ', div)

clear = getValue.clear()
print('clear: ', clear)
