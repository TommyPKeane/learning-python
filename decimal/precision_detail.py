# Examples of Creating Decimal Instances and Simple Arithmetic
#
# Note:
# New in Python version 3.3 -- The significance of a new Decimal is determined
# solely by the number of digits input. Context precision and rounding only come
# into play during arithmetic operations.
import decimal


def print_difference(x, y, precision):
    decimal.getcontext().prec = precision
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"Precision {precision} | Diff x - y: {x - y}\n")
    return None


if __name__ == "__main__":
    x = decimal.Decimal("3.141_592_653_589_793_238_462_643_3")
    y = decimal.Decimal("3.142")

    print_difference(x, y, precision=1)
    print_difference(x, y, precision=3)
    print_difference(x, y, precision=5)
    print_difference(x, y, precision=12)
