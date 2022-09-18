# declaration function
def is_one_away(word1, word2):
    word1, word2 = list(word1), list(word2)
    
    if len(word1) != len(word2):
        return False
    
    for i in word1:
        if i in word2:
            word2.remove(i)
    
    return len(word2) == 1

# data input
txt1 = input()
txt2 = input()

# function call
print(is_one_away(txt1, txt2))