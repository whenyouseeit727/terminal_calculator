a = float(input("input 1st number\n"))
b = float(input("input 2nd number\n"))
function = input("input function(+)\n")


def addition(a, b):
    return a + b


if function == "+" or function == "addition":
    result = addition(a,b)
    print(result)