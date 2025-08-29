operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "%": lambda x, y: x % y,
    "**": lambda x, y: x ** y,
    "//": lambda x, y: x // y,
    "sqrt": lambda x: x ** 0.5,
    "abs": lambda x: abs(x),
    "round": lambda x: round(x),
    "max": lambda x, y: max(x, y),
    "min": lambda x, y: min(x, y),
    "pow": lambda x, y: pow(x, y),
    "divmod": lambda x, y: divmod(x, y),
    "sum": lambda x, y: sum([x, y]),
    "all": lambda x: all(x),
    "any": lambda x: any(x),
    "enumerate": lambda x: list(enumerate(x)),
    "filter": lambda x, y: list(filter(x, y)),
    "map": lambda x, y: list(map(x, y)),
    "zip": lambda x, y: list(zip(x, y)),
    "sorted": lambda x: sorted(x),
    "reversed": lambda x: list(reversed(x)),
    "len": lambda x: len(x),
    "list": lambda x: list(x),
    "tuple": lambda x: tuple(x),
    "set": lambda x: set(x),
}

number1 = float(input("input the first number"))
number2 = float(input("input the second number"))
operations_input = input("choose operations(+, -, *, /): ")

print("Result", operations.get(operations_input, lambda x, y: "incorrect operations")(number1, number2))
