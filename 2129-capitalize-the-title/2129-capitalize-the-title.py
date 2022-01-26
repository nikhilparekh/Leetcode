class Solution:
    def capitalizeTitle(self, title: str) -> str:
        li = title.split(" ")
        res = ""
        for i in li:
            if len(i)<=2:
                res+=i.lower()
            else:
                res+=i.capitalize()
            res+=" "
        res = res.rstrip()
        return res