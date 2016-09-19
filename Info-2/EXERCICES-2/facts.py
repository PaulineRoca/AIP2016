##

def fact1(n):
    if n == 0:
        return 1
    else:
        return n * fact1(n - 1)


##

Fact = [1, 1, 2]

def fact5(n):
    global Fact
    p = len(Fact) - 1
    fac = Fact[p]
    if n <= p:
        return Fact[n]
    for i in range(p + 1, n + 1):
        fac = fac * i
        Fact = Fact + [ fac ]
    return Fact[n]


##

factorials = {0:1, 1:1}

def fact2(n):
    if n in factorials: return factorials[n]
    value = n * fact2(n - 1)
    factorials[n] = value
    return value

## 

    
def memoize(fn):
    stored_results = {}
 
    def memoized(*args):
        try:
            # try to get the cached result
            return stored_results[args]
        except KeyError:
            # nothing was cached for those args. let's fix that.
            result = stored_results[args] = fn(*args)
            return result
 
    return memoized

@memoize
def fact3(n):
    return n if n in [0, 1] else n * fact3(n - 1) 

