"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNoteDict = {}
        for char in ransomNote:
            ransomNoteDict[char] = ransomNoteDict.get(char, 0) + 1
        magazineDict = {}
        for char in magazine:
            magazineDict[char] = magazineDict.get(char, 0) + 1
        for key in ransomNoteDict.keys():
            if magazineDict.get(key, 0) < ransomNoteDict[key]:
                return False
        return True


def test():
    testCases = [
        {
            "input": {
                "ransomNote": "a", 
                "magazine": "b"
            },
            "output": False
        },
        {
            "input": {
                "ransomNote": "aa", 
                "magazine": "ab"
            },
            "output": False
        },
        {
            "input": {
                "ransomNote": "aa", 
                "magazine": "aab"
            },
            "output": True
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().canConstruct(testCase["input"]["ransomNote"], testCase["input"]["magazine"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()        