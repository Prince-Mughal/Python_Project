import sys

"""
    Solve Arithmetic Single Digit Expression
    for criticism mughalb9291@gmail.com
    Warmly welcome.
    [DD:MM:YY] 26-04-2019, [HH:MM:SS] 14:19:01 Friday
    Soon, code will be updated 
"""


def solve_piecewise(expression, operator):
    """
    :param expression: arithmetic expression in list
    :param operator:  arithmetic operator
    :return:  returns Nothing
    This function will solve arithmetic expression piecewise
    according to given operator only
    improvement are required, see next update

    """
    index = 0
    while operator in expression:
        print(expression)
        if expression[index] == operator:
            left_value = int(expression[index - 1])
            right_value = int(expression[index + 1])
            if operator == '/':
                result = left_value // right_value
            elif operator == '*':
                result = left_value * right_value
            elif operator == '+':
                result = left_value + right_value
            elif operator == '-':
                result = left_value - right_value
            else:
                print("Error: Invalid Operator.")
                sys.exit(-1)
            expression[index] = str(result)
            del expression[index + 1]
            del expression[index - 1]
            index = 0
        index += 1


def division_handler(list_expr):
    """
    :param list_expr: arithmetic expression in list form
    :return: returns Nothing
    This function will handle all floor division
    """
    solve_piecewise(list_expr, "/")


def multiplication_handler(list_expr):
    """
    :param list_expr: arithmetic expression in list form
    :return: returns Nothing
    This function will handle all multiplication
    """
    solve_piecewise(list_expr, "*")


def addition_handler(list_expr):
    """
    :param list_expr: arithmetic expression in list form
    :return: returns Nothing
    This function will handle all addition
    """
    solve_piecewise(list_expr, "+")


def subtraction_handler(list_expr):
    """
    :param list_expr: arithmetic expression in list form
    :return: returns Nothing
    This function will handle all subtraction
    """
    solve_piecewise(list_expr, "-")


def compute(expression):
    """
    :param expression: arithmetic expression in list form
    :return: return result
    This function calls all the arithmetic operational function
    in DMAS(Division, Multiplication, Addition, Subtraction) rule.
    """
    division_handler(expression)  # First Highest Priority
    multiplication_handler(expression)  # Second Highest Priority
    addition_handler(expression)   # Third Highest Priority
    subtraction_handler(expression)  # Fourth Highest Priority
    return int(expression.pop())


def main():
    """
    Take Input An Arithmetic Expression
    Convert it into List Expression
    Call Compute(Expression) to calculate result.
    """
    input_data = input("Enter an Arithmetic Expression: ")
    input_data = list(input_data)
    answer = compute(input_data)
    print("Result = {0}".format(answer))


if __name__ == "__main__":
    main()
