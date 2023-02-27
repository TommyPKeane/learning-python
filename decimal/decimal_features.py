# Examples of Decimal Instances' features
#
# Note:
# New in Python version 3.3 -- The significance of a new Decimal is determined
# solely by the number of digits input. Context precision and rounding only come
# into play during arithmetic operations.
import decimal

if __name__ == "__main__":
    x = decimal.Decimal("3.141_592_653_589_793_238_462_643_3")
    y = decimal.Decimal("3.142")
