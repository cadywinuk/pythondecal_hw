import numpy as np
# The Odd Ones Out
def only_odd(arr):
   
    result = []
    
    for row in arr:
        if all(x % 2 != 0 for x in row):
            result.append(row)
    
    return result
arr = np.array([[1,2,3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
print(only_odd(arr))

# 2.1 Let's Play Checkers
def checkerboard():
    return np.zeros((8, 8), dtype=int)

matrix = checkerboard()
print(matrix)

# 2.2 Odd Lines of Checkerboard
def half_checkerboard():
    matrix = np.zeros((8, 8), dtype=int)
    
    for i in range(1, 8, 2):
        matrix[i] = [1 if j % 2 == 0 else 0 for j in range(8)]
    
    return matrix
print(half_checkerboard())

# 2.3 All Lines of Checkerboard
def finsh_checkerboard():
    matrix = np.zeros((8, 8), dtype=int)
    for i in range(8):
        if i % 2 == 0:
            matrix[i] = [1 if j % 2 == 0 else 0 for j in range(8)]
        else:
            matrix[i] = [0 if j % 2 == 0 else 1 for j in range(8)]
    return matrix
print(finsh_checkerboard())

#2.4 Checkerboard Reversed
def reverse_checkerboard():
    for i in range(8):
        if i % 2 == 0:
            matrix[i] = [0 if j % 2 == 0 else 1  for j in range(8)]
        else:
            matrix[i] = [1 if j % 2 == 0 else 0 for j in range(8)]
    
    return matrix
print(reverse_checkerboard)

#3 The Expanding Universe
import numpy as np

def expansion(universe, n):
    return np.array([' '.join(list(word)).replace(' ', ' ' * n) for word in universe])

universe = np.array(['galaxy', 'clusters'])
result = expansion(universe, 5)
print(result)

#4 Second Largest Exoplanet
def secondLargest(p):
    secondLargest = []
    for x in p.T:
        if len(x) > 1:
            secondLargest.append(np.sort(x)[-2])
    
    return np.array(secondLargest)
planets = np.random.randint(100, 1000, (5, 5))
print(planets)
print(secondLargest(planets))