s,n=map(str,raw_input().split())
#a = "aab"
#b = "xxy"

x = {}; y = {}
def is_isomorphic(s, n):
    if len(s) != len(n):
        return "no"
    else:
        for i, v in enumerate(s):
            if v in x and x[v] != n[i]:
                return "no"
            else:
                x[v] = n[i]
            if n[i] in y and y[n[i]] != v:
                return "no"
            else:
                y[n[i]] = v
        return "yes"

print is_isomorphic(s, n)
