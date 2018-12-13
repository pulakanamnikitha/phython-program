m,n=map(int,raw_input().split())
def gcd(m,n):
    z=abs(m-n)
    if (m-n)==0:
        return n
    else:
        return gcd(z,min(m,n))
print gcd(m,n)
