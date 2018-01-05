number = int( input("Give a number to calculate its factorial value\n") )

lib = [*range(1, number + 1)]
result = 1

print("!{} = ".format(number), end="")
for i in lib:
    result = result * i
    if i != lib[-1]:
        print(str(i)+" . ",end="")
    if i == lib[-1]:
        print(str(i) + " = {}".format(result))