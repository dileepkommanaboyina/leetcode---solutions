class Solution(object):
    def getLongestSubsequence(self, words, groups):
        b=[words[0]]
        a=[groups[0]]
        for i in range(1,len(groups)):
            if groups[i]!=a[-1]:
                b.append(words[i])
                a.append(groups[i])
        return b





        
