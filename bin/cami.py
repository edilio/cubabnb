__author__ = 'edilio'


def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return reduce(gcd, numbers)

# Least common multiple is not in standard libraries? It's in gmpy, but this is simple enough:


def lcm(*numbers):
    """Return lowest common multiple."""
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)


def get_least_common_denominator(d1,d2):

    return lcm(d1,d2)


def simplify(n,d):
    result = n/d
    if result > 0:
        whole = result
        n1 = n % d
        print whole, n1, "/", d
    else:
        print n, "/", d


def add(n1, d1, n2, d2):
    """
    n1 = numerator 1
    d1 = denominator 1
    n2 = numerator 2
    d2 = denominator 2
    use case add(1,3,3,4) == 1/3 + 3/4
    """
    lcd = get_least_common_denominator(d1,d2)
    new_n1 = (lcd / d1)* n1
    new_n2 = (lcd / d2)* n2
    print new_n1, "/", lcd
    print "+"
    print new_n2, "/", lcd
    print new_n1 + new_n2, "/", lcd
    simplify(new_n1 + new_n2, lcd)


def get_values(s):
    lst = s.split('+')
    first = lst[0].strip()
    second = lst[1].strip()
    n1, d1 = first.split('/')
    n2, d2 = second.split('/')
    return int(n1), int(d1), int(n2),int(d2)


def test(s):
    print s
    n1, d1, n2, d2 = get_values(s)
    add(n1,d1,n2,d2)
    print

s = raw_input('--> ')
test(s)
#test("1/3+3/4")
#test("3/10+20/12")




