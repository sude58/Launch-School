import copy
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(copy.deepcopy(sub_list))

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]