class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        cmax = 0
        for i in s:
            if i in st:
                cmax = max(cmax, len(st))
                # print(st)
                while st[0]!=i:
                    st.pop(0)
                
                st.pop(0)
                st.append(i)
            else:
                st.append(i)
                # cmax+=1
            # print(st)
        return max(cmax,len(st))
        
                
                
                
            
        