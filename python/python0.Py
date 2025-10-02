
def c(n):
    if n==1:
        return 1
    else:
        return n+c(n-1)
print(c(100))

def e():
    if n==0:
        return 0
    else:
        return(n%10) + e(n//10)
print(e(1234))




















