def curry3(f):
    """
    Convert f(a, b, c) into a curried version:
    curry3(f)(a)(b)(c)
    """
    # fill in answer here
    def curry2(a):
        def curry1(b):
            def curry0(c):
                return f(a,b,c)
            return curry0
        return curry1
    return curry2


# Tests
def f(a, b, c):
    return a * (b + c)

g = curry3(f)

print(g(2)(3)(1))             # 8
print(g(1)(10)(5))            # 15

h = g(5)
i = h(2)
print(i(3))                   # 25

def join3(a, b, c):
    return f"{a}-{b}-{c}"

jg = curry3(join3)
print(jg("x")("y")("z"))      # x-y-z

# Edge case: division error only happens on final call
def div3(a, b, c):
    return a / (b - c)

dg = curry3(div3)
print(dg(10)(5)(3))           # 5.0

try:
    print(dg(10)(5)(5))       # ZeroDivisionError expected
except ZeroDivisionError:
    print("ZeroDivisionError")
