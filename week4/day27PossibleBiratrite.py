class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = {}
        colorMatrix = [None for _ in range(N + 1)]
        
        for node in dislikes:
            if graph.get(node[0]):
                graph[node[0]].append(node[1])
            else:
                graph[node[0]] = [node[1]]
            if graph.get(node[1]):
                graph[node[1]].append(node[0])
            else:
                graph[node[1]] = [node[0]]
        # print("graph", graph)
        visited = {}
        for index in graph.keys():
            queue = [index]
            while queue:
                node = queue.pop(0)

                if visited.get(node, False):
                    continue
                visited[node] = True
                nodes = graph.get(node, [])
                
                color = colorMatrix[node]
                if not color:
                    color = "RED"
                colorMatrix[node] = color
                newColor = "BLUE" if color == "RED"  else "RED"

                for tempNode in nodes:
                    tempNodeColor = colorMatrix[tempNode]
                    if tempNodeColor == None:
                        queue.append(tempNode)
                        colorMatrix[tempNode] = newColor
                    elif tempNodeColor == newColor:
                        queue.append(tempNode)
                    else:
                        # print("Failure is here", index, node, tempNodeColor, newColor)
                        return False
                # print("while", node, index, visited, colorMatrix)
            # print("for", index, visited, colorMatrix)
        return True

def testSolution():
    testCases = [
        {
            "input": {
                "N": 50,
                "dislikes": [[21,47],[4,41],[2,41],[36,42],[32,45],[26,28],[32,44],[5,41],[29,44],[10,46],[1,6],[7,42],[46,49],[17,46],[32,35],[11,48],[37,48],[37,43],[8,41],[16,22],[41,43],[11,27],[22,44],[22,28],[18,37],[5,11],[18,46],[22,48],[1,17],[2,32],[21,37],[7,22],[23,41],[30,39],[6,41],[10,22],[36,41],[22,25],[1,12],[2,11],[45,46],[2,22],[1,38],[47,50],[11,15],[2,37],[1,43],[30,45],[4,32],[28,37],[1,21],[23,37],[5,37],[29,40],[6,42],[3,11],[40,42],[26,49],[41,50],[13,41],[20,47],[15,26],[47,49],[5,30],[4,42],[10,30],[6,29],[20,42],[4,37],[28,42],[1,16],[8,32],[16,29],[31,47],[15,47],[1,5],[7,37],[14,47],[30,48],[1,10],[26,43],[15,46],[42,45],[18,42],[25,42],[38,41],[32,39],[6,30],[29,33],[34,37],[26,38],[3,22],[18,47],[42,48],[22,49],[26,34],[22,36],[29,36],[11,25],[41,44],[6,46],[13,22],[11,16],[10,37],[42,43],[12,32],[1,48],[26,40],[22,50],[17,26],[4,22],[11,14],[26,39],[7,11],[23,26],[1,20],[32,33],[30,33],[1,25],[2,30],[2,46],[26,45],[47,48],[5,29],[3,37],[22,34],[20,22],[9,47],[1,4],[36,46],[30,49],[1,9],[3,26],[25,41],[14,29],[1,35],[23,42],[21,32],[24,46],[3,32],[9,42],[33,37],[7,30],[29,45],[27,30],[1,7],[33,42],[17,47],[12,47],[19,41],[3,42],[24,26],[20,29],[11,23],[22,40],[9,37],[31,32],[23,46],[11,38],[27,29],[17,37],[23,30],[14,42],[28,30],[29,31],[1,8],[1,36],[42,50],[21,41],[11,18],[39,41],[32,34],[6,37],[30,38],[21,46],[16,37],[22,24],[17,32],[23,29],[3,30],[8,30],[41,48],[1,39],[8,47],[30,44],[9,46],[22,45],[7,26],[35,42],[1,27],[17,30],[20,46],[18,29],[3,29],[4,30],[3,46]]
            },
            "output": True
        }
    ]

    solution = Solution()
    for testCase in testCases:
        output = solution.possibleBipartition(testCase["input"]["N"], testCase["input"]["dislikes"])
        assert testCase["output"] == output, "FAILED! Expected: {}, Got: {}".format(testCase["output"], output)

if __name__ == "__main__":
    testSolution()        