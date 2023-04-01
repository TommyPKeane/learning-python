# Examples of Numerical Operations from the PSL `math` Package
#
# References:
# - https://docs.python.org/3/library/math.html
import math


def log_floor_truc_ceil(x):
    x_floor = math.floor(x)
    x_trunc = math.trunc(x)
    x_ceil = math.ceil(x)
    print(f"x: {x} | floor: {x_floor} | trunc: {x_trunc} | ceil: {x_ceil}")
    return None


if __name__ == "__main__":
    log_floor_truc_ceil(3.14159)
    log_floor_truc_ceil(-3.14159)
    log_floor_truc_ceil(0.14159)
    log_floor_truc_ceil(-0.14159)
    log_floor_truc_ceil(0.59)
    log_floor_truc_ceil(-0.59)
