
def chk_sudoku(data_list):
    result = ''
    for x in data_list:
        seen = set()
        result =  not any(i in seen or seen.add(i) for i in x)
        if result is False:
            break
    return result
#print(chk_sudoku(['123456789','978654321','543216789']))

row_data_lst = list()
col_data_lst = list()
cube_data_lst = list()
#For making row string
for i in range(1,10):
    data = input("enter " + str(i) + " row for sudoku from 1 to 9 :")
    row_data_lst.append(data)
#For making column string
for k in range(9):
    col_data = ''
    for j in range(len(row_data_lst)):
        col_data += row_data_lst[j][k]
    col_data_lst.append(col_data)
#For making cube string
a = 0
for l in range(3):
    cube_str = ''
    counter = 1
    for m in row_data_lst:
        if counter < 4:
            cube_str += m[a] + m[a+1] + m[a+2]
            counter += 1

        if counter == 4:
            cube_data_lst.append(cube_str)
            cube_str = ''
            counter = 1
    a += 3

row_result = chk_sudoku(row_data_lst)
col_result = chk_sudoku(col_data_lst)
cube_result = chk_sudoku(cube_data_lst)

if row_result == col_result == cube_result == True:
    print("Sudoku is correct")
else:
    print("Sudoku is wrong")
