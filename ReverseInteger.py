def revInt(num):
    if num>0:
        res = 0
        while num>0:
            res*=10
            res+=num%10
            num//=10
        return res
    num*=-1
    res=0
    while num>0:
        res*=10
        res+=num%10
        num//=10
    res*=-1
    return res


print(revInt(-123))
