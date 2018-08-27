import random

numberOfRolls = int(input("Roll how many d6?"))

while numberOfRolls < 1 or numberOfRolls > 100000:
    numberOfRolls = int(input("Enter an numner between 1 & 100000"))

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
   
saveFile = open("HW1output.txt", "w")

for x in range(numberOfRolls):
    dieRoll = random.randint(1, 6)
    if dieRoll == 1:
        print("1")
        saveFile.write("1\n")
        one += 1
    if dieRoll == 2:
        print(" 2")
        saveFile.write(" 2\n")
        two += 1
    if dieRoll == 3:
        print("  3")
        saveFile.write("  3\n")
        three += 1
    if dieRoll == 4:
        print("   4")
        saveFile.write("   4\n")
        four += 1
    if dieRoll == 5:
        print("    5")
        saveFile.write("    5\n")
        five += 1
    if dieRoll == 6:
        print("     6")
        saveFile.write("     6\n")
        six += 1

print("Number of times wo got 1:", one)
print("Number of times wo got 1:", one)
print("Number of times wo got 2:", two)
print("Number of times wo got 2:", two)
print("Number of times wo got 3:", three)
print("Number of times wo got 3:", three)
print("Number of times wo got 4:", four)
print("Number of times wo got 4:", four)
print("Number of times wo got 5:", five)
print("Number of times wo got 5:", five)
print("Number of times wo got 6:", six)
print("Number of times wo got 6:", six)
    