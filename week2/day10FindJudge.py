"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""
class Solution(object):
    def makeTrustDict(self, trust):
        self.trustDict = {}
        for value in trust:
            if not self.trustDict.get(value[0]):
                self.trustDict[value[0]] = {}
            self.trustDict[value[0]][value[1]] = True
    
    def isTrust(self, person1, person2):
        if self.trustDict.get(person1) and self.trustDict[person1].get(person2):
            return True
        return False
    
    def validateJudge(self, judge, N):
        if self.trustDict.get(judge) and len(self.trustDict[judge]):
            # judge knows someone
            return -1
        for person in xrange(1, N + 1):
            if not self.isTrust(person, judge) and person != judge:
                # There is someone who doesn't know judge
                return -1
        return judge
    
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        self.makeTrustDict(trust)
        stack = []
        for person in xrange(1, N+1):
            stack.append(person)
        while len(stack) > 1:
            person1 = stack.pop()
            person2 = stack.pop()
            if self.isTrust(person1, person2):
                stack.append(person2)
            else:
                stack.append(person1)
        return self.validateJudge(stack.pop(), N)

def test():
    testCases = [
        {
            "input": {
                "N": 2,
                "trust": [[1,2]]
            },
            "output": 2
        },
        {
            "input": {
                "N": 3,
                "trust": [[1,3],[2,3]]
            },
            "output": 3
        },
        {
            "input": {
                "N": 3,
                "trust": [[1,3],[2,3],[3,1]]
            },
            "output": -1
        },
        {
            "input": {
                "N": 3,
                "trust": [[1,2],[2,3]]
            },
            "output": -1
        },
        {
            "input": {
                "N": 4,
                "trust": [[1,3],[1,4],[2,3],[2,4],[4,3]]
            },
            "output": 3
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().findJudge(testCase["input"]["N"], testCase["input"]["trust"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()        