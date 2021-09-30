w1 = str(input())
w2 = str(input())

def anagrams(w1, w2):
    if(sorted(w1) == sorted(w2)):
        return True 
    else:
        return False 
