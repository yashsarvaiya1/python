from collections import Counter

def anagram(s1:str,s2:str):
    if len(s1)!=len(s2):
        return False
    else:
        return Counter(s1) == Counter(s2)
    
print(anagram("danger","garden"))