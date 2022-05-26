class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if boxes.count('1')==0:
            return [0]*len(boxes)
        arr = []
        def dist(idx,boxes):
            count = 0
            for index, val in enumerate(boxes):
                if val!='0':
                    count+=(abs(index-idx)*int(val))
            return count
        # print(dist(2,boxes)
        for i in range(len(boxes)):
            arr.append(dist(i,boxes))
        return arr
                