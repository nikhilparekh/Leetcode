class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        arr = []
        for i in s:
            arr.append(int(i))
        arr.sort()
        a=b=0
        j = 0
        for i in arr:
            if j==0:
                j=1
                a*=10
                a+=i
            else:
                j=0
                b*=10
                b+=i
        print(a,b)
        return a+b
                