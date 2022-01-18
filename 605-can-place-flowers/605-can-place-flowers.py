class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==1 and len(flowerbed)==1 and flowerbed[0]==0:
            return True
        for i in range(len(flowerbed)-1):
            if n==0:
                return True
            elif i==0 and flowerbed[i+1]==0 and flowerbed[i]!=1:
                flowerbed[i]=1
                n-=1
            # elif i==len(flowers)
            elif i==1 or i==len(flowerbed)-1:
                if flowerbed[i-1]==0 and flowerbed[i]!=1:
                    flowerbed[i]=1
                    n-=1
            else:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]!=1:
                    flowerbed[i]=1
                    n-=1
        if n!=0:
            if flowerbed[-1]==0 and flowerbed[-2]==0:
                n-=1
        return n==0
                    