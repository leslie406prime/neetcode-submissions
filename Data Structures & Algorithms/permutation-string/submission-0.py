class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        win_count = [0]* 26

        for i in range(len(s1)):
            s1_count[ ord(s1[i]) - ord("a")] += 1
            win_count[ ord(s2[i]) - ord("a")] += 1

        matches = sum( 1 for i in range(26) if s1_count[i] == win_count[i])

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True 

            r = ord(s2[right]) - ord("a")
            win_count[r] += 1
            if win_count[r] == s1_count[r]:
                matches += 1
            elif win_count[r] - 1 == s1_count[r]:
                matches-= 1

            l = ord(s2[left]) - ord("a")
            win_count[l] -= 1
            if win_count[l] == s1_count[l]:
                matches += 1
            elif win_count[l] + 1== s1_count[l]:
                matches -= 1

            left += 1
        
        return matches == 26


  
            


        

        