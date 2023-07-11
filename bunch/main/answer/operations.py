import math

class operations:
    def minus(self, pos1, pos2):
        ans = []
        for i in range(len(pos1)):
            ans.append(pos1[i] - pos2[i])
        return ans # this is the difference between two vectors
    
    def magnitude(self, vector):
        return math.sqrt(vector[0] ** 2 + vector[1] ** 2) # this is the magnitude of vector
    
    def divide(self, vector, n):
        ans = []
        for i in range(len(vector)):
            ans.append(vector[i] / n)
        return ans # this is vector / n
    
    def multi(self, w, vector):
        ans = []
        for i in range(len(vector)):
            ans.append(vector[i] * w)
        return ans # this is vector * n
    
    def plus(self, vector1, vector2):
        ans = []
        for i in range(len(vector1)):
            ans.append(vector1[i] + vector2[i])
        return ans # the sum of two vectors