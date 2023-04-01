# Examples of Creating Decimal Instances and Simple Arithmetic
#
# Note:
# New in Python version 3.3 -- The significance of a new Decimal is determined
# solely by the number of digits input. Context precision and rounding only come
# into play during arithmetic operations.
import decimal


if __name__ == "__main__":
    # 2 Digits of Precision
    crnt_precision = 2
    decimal.getcontext().prec = crnt_precision

    x = decimal.Decimal("3.141_592_653_589_793_238_462_643_3")
    print(f"Precision {crnt_precision}: {x}\n")


    # 10 Digits of Precision
    crnt_precision = 10
    decimal.getcontext().prec = crnt_precision

    y = decimal.Decimal("3.141_592_653_589_793_238_462_643_3")
    print(f"Precision {crnt_precision}: {y}\n")


    # Diff of Precisions
    crnt_precision = 12
    decimal.getcontext().prec = crnt_precision
    print(f"Precision {crnt_precision} | Diff x - y: {x - y}\n")


    # Diff of Precisions
    crnt_precision = 2
    decimal.getcontext().prec = crnt_precision
    print(f"Precision {crnt_precision} | Diff x - y: {x - y}\n")


    # 2 Digits of Precision
    crnt_precision = 2
    decimal.getcontext().prec = crnt_precision

    x = decimal.Decimal("3.141_592")
    print(f"Precision {crnt_precision}: {x}\n")


    # 10 Digits of Precision
    crnt_precision = 10
    decimal.getcontext().prec = crnt_precision

    y = decimal.Decimal("3.141")
    print(f"Precision {crnt_precision}: {y}\n")


    # Diff of Precisions
    crnt_precision = 12
    decimal.getcontext().prec = crnt_precision
    print(f"Precision {crnt_precision} | Diff x - y: {x - y}\n")


    # Diff of Precisions
    crnt_precision = 2
    decimal.getcontext().prec = crnt_precision
    print(f"Precision {crnt_precision} | Diff x - y: {x - y}\n")
