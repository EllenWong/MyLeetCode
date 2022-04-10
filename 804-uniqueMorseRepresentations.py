class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            cur = ""
            for w in word:
                cur = cur + mos[ord(w)-ord('a')]
            s.add(cur)
        return len(s)
