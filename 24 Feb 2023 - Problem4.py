def create_table(rows,cols):
    multi_array = [[None] * cols for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            multi_array[i][j] = input("Enter the value for element at row " + str(i) + " and column " + str(j) + ": ")

    print("Multi-dimensional array:")
    for i in range(rows):
        for j in range(cols):
            print(multi_array[i][j], end="\t")
        print()

while True:
    try:
        rows = int(input("Enter the number of rows: "))
        break
    except ValueError:
        print("Invalid input. Please enter int.")

while True:
    try:
        columns = int(input("Enter the number of columns: "))
        break
    except ValueError:
        print("Invalid input. Please enter int.")


create_table(rows,columns)
