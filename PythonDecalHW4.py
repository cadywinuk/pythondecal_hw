# 1 Errors at End of File

# 2.1 Making a List Variable
list_of_nums =  [*range(0,21)]
print(list_of_nums)

# 2.2 
def square(list_of_nums):
    list = []
    for i in list_of_nums:
        list.append(i ** 2)
    return list
print(square(list_of_nums))

#2.3 
square = square(list_of_nums)
def first15(square):
    print(square[0:15:1])
first15(square)

# 2.4
def every_fifth(square):
    print(square[4::5])
every_fifth(square)

#2.5 Slicing and Striding
def fancy_func(square):
    print( 
        square[2::3]
    )
fancy_func(square)

#3.1
def create_2d_list():
    matrix = []
    number = 1
    for i in range(5):  
        row = []  
        for j in range(5): 
            row.append(number)
            number += 1 
        matrix.append(row) 
    return matrix

matrix = create_2d_list()

print(matrix)

#3.2
def replace_multiples_of_3(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): 
            if matrix[i][j] % 3 == 0:  
                matrix[i][j] = 0  
    return matrix

updated_matrix = replace_multiples_of_3(matrix)

print(updated_matrix)

#3.3
def sum_non_question_elements(matrix):
    total = 0
    for row in matrix: 
        for element in row: 
            if element != "?": 
                total += element  
    return total


sum_result = sum_non_question_elements(updated_matrix)

print(sum_result)