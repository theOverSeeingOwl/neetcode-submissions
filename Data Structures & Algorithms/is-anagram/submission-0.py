class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(s)
        if s_length != t_length:
            return False 
        
        s_list = []
        for s_char in s:
            s_list.append(s_char)
        t_list = []
        for t_char in t:
            t_list.append(t_char)
        
        s_list = sorted(s_list)
        t_list = sorted(t_list)

        if s_list != t_list:
            return False
        


        return True                
        