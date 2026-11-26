#mlib. py
import random, time, math, sys
def mtool():
    return input("> ").lower().rstrip()
def mclear():
    print('\033[2J\033[H', end='')
def mtime(a):
    time.sleep(a)
def mrandomint(a, b):
    return random.randint(a, b)
def mrandomice(a, b, c):
    return random.choice((a, b, c))
def mmenu(options):
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    try:
        return int(input("cat> ")) - 1
    except ValueError:
        return -1
def mprint(text, color="green"):
    colors = {"green": "\033[92m", "red": "\033[91m", "yellow": "\033[93m", "blue": "\033[94m"}
    print(f"{colors.get(color, '')}{text}\033[0m")
def advertisement(a, adver):
    for _ in range(a):
        print(adver) # useless? I know
def mmath(cst, a):
    if cst == "cos":
        return math.cos(a)
    elif cst == "sin":
        return math.sin(a)
    elif cst == "tan":
        return math.tan(a)
    else:
        raise ValueError(f"no function: {cst}")
def mexit(code):
    sys.exit(code)

def relu(x):
    return max(0.0, x)
def relu_vec(vec):
    return [relu(v) for v in vec]
def dot(a, b):
    if len(a) != len(b):
        raise ValueError("")
    return sum(x * y for x, y in zip(a, b))

def mtranspose(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]
# Micro lib
