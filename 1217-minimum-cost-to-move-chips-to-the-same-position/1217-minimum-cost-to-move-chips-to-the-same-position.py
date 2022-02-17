class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        di = {}
        for i in position:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        di = dict(sorted(di.items(), key=lambda x:x[1], reverse=True))
        x=None
        x1=None
        for i in di.keys():
            if i%2==0 and x==None:
                x=i
            elif i%2!=0 and x1==None:
                x1=i
        # print(x,x1)
        # x = list(di.keys())[0]
        cost = 0
        cost1=0
        if x!=None:
            for i in list(di.keys()):
                if(abs(x-i)%2!=0):
                    cost1+=di[i]
        if x1!=None:
            for i in list(di.keys()):
                if(abs(x1-i)%2!=0):
                    cost+=di[i]
        
            
        # print(di)
        return min(cost,cost1)
            