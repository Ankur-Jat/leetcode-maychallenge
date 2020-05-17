"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel 
value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of 
the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color 
as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""
class Solution(object):
    def isSafe(self, image, row, column, colorValue, traversedPath):
        if row < 0 or column < 0 or row >= len(image) or column >= len(image[0]) or traversedPath[row][column]:
            # print("Returning first", row, column, len(image), len(image[0]), colorValue, traversedPath, image[row][column])
            return False
        if image[row][column] == colorValue:
            # print("Returing true")
            return True
        # print("No valid case", row, column, colorValue)
        return False
    
    def pushRelatedCoordinates(self, image, row, column, colorValue, pendingCoordinates, traversedPath):    
        directionsToTraverse = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directionsToTraverse:
            new_row = row + direction[0]
            new_column = column + direction[1]
            if (self.isSafe(image, new_row, new_column, colorValue, traversedPath)):
                pendingCoordinates.append((new_row, new_column))
                
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        traversedPath = []
        for _ in xrange(len(image)):
            row = []
            for _ in xrange(len(image[0])):
                row.append(0)
            traversedPath.append(row)
        
        originalColor = image[sr][sc]
        pendingCoordinates = [(sr, sc)]
        while len(pendingCoordinates) > 0:
            coordinate = pendingCoordinates.pop(0)
            traversedPath[coordinate[0]][coordinate[1]] = 1
            self.pushRelatedCoordinates(image, coordinate[0], coordinate[1], originalColor, pendingCoordinates, traversedPath)
            image[coordinate[0]][coordinate[1]] = newColor
            # print(coordinate, traversedPath, image, pendingCoordinates)
        return image

def test():
    testCases = [
        {
            "input": {
                "image": [[1,1,1],[1,1,0],[1,0,1]],
                "sr": 1,
                "sc": 1,
                "newColor": 2,
            },
            "output": [[2,2,2],[2,2,0],[2,0,1]]
        },
    ]
    for testCase in testCases:
        expected = testCase["output"]
        result = Solution().floodFill(testCase["input"]["image"], testCase["input"]["sr"], 
            testCase["input"]["sc"], testCase["input"]["newColor"])
        assert expected == result, "Expected: {0} Got: {1}".format(expected, result)

if __name__ == "__main__":
    test()