"""
Scientific Computing with Python Projects
Arithmetic Formatter
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
"""


def arithmetic_arranger(problems, prnt=False):

    # The limit is five, anything more will return: Error: Too many problems.
    if len(problems) > 5:
        return "Error: Too many problems."

    space = []  # spaces needed

    x_lst = []  # first operand
    i_lst = []  # operator +/-
    y_lst = []  # second operand
    r_lst = []  # result
    for l in problems:
        x, i, y = l.split(" ")

        # Each number (operand) should only contain digits.
        if x.isdigit() == False or y.isdigit() == False:
            return "Error: Numbers must only contain digits."

        # Each operand (aka number on each side of the operator) has a max of four digits in width.
        if len(x) > 4 or len(y) > 4:
            return "Error: Numbers cannot be more than four digits."

        # list - longest numbers
        if len(x) > len(y):
            space.append(len(x))
        else:
            space.append(len(y))

        x_lst.append(x)
        i_lst.append(i)
        y_lst.append(y)
        if i == "+":
            r = int(x) + int(y)
        elif i == "-":
            r = int(x) - int(y)

        # The appropriate operators the function will accept are addition and subtraction.
        else:
            return "Error: Operator must be '+' or '-'."
        r_lst.append(str(r))

    first_row = ""
    q = 0
    for n in x_lst:
        first_row = first_row + f"{x_lst[q].rjust(space[q]+2)}    "
        q = q + 1
    first_row = first_row.rstrip()

    second_row = ""
    q = 0
    for n in i_lst:
        second_row = second_row + f"{i_lst[q].ljust(0)} {y_lst[q].rjust(space[q])}    "
        q = q + 1
    second_row = second_row.rstrip()

    third_row = ""
    q = 0
    for n in space:
        spc = "-" * (space[q] + 2)
        third_row = third_row + f"{spc.ljust(0)}    "
        q = q + 1
    third_row = third_row.rstrip()

    fourth_row = ""
    if prnt:
        q = 0
        for n in r_lst:
            fourth_row = fourth_row + f"{r_lst[q].rjust(space[q]+2)}    "
            q = q + 1

        fourth_row = fourth_row.rstrip()
        arranged_problems = (
            first_row + "\n" + second_row + "\n" + third_row + "\n" + fourth_row
        )

    else:
        arranged_problems = first_row + "\n" + second_row + "\n" + third_row

    return arranged_problems


#####
## EXAMPLES
#####

print(arithmetic_arranger(["322 - 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print("\n")

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print("\n")
print(arithmetic_arranger(["32 + 11111", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print("\n")

print(arithmetic_arranger(["32 + b", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print("\n")

print(arithmetic_arranger(["1200 * 6985", "3801 + 2", "45 + 43", "123 + 49"], True))
