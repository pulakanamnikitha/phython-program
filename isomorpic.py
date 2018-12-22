a,b=map(str,raw_input().split())
#a = "aab"
#b = "xxy"

x = {}; y = {}
def is_isomorphic(a, b):
    if len(a) != len(b):
        return "no"
    else:
        for i, v in enumerate(a):
            if v in x and x[v] != b[i]:
                return "no"
            else:
                x[v] = b[i]
            if b[i] in y and y[b[i]] != v:
                return "no"
            else:
                y[b[i]] = v
        return "yes"

print is_isomorphic(a, b)
