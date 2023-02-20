def sort_and_add_to_list(my_list, num):
    try:
        my_list.append(int(num))
        # Sort list
        my_list.sort()
        # Print sorted list
        print("Sorted list: ", my_list)
    except ValueError:
        print("Error: Please enter an integer.")

while True:
    try:
        #Number of int to add to list
        length_list = int(input("Enter the number of integers to add to the list: "))
        if length_list < 0:
            raise ValueError("Error: Please enter an integer.")
        new_list = []
        break
    except ValueError:
        print("Error: Please enter an integer.")
        continue

for i in range(length_list):
    while True:
        try:
            num_list = int(input(f'Enter the {i+1} integer: '))
            new_list.append(num_list)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

print("Original is:", new_list)
#sort original list
new_list.sort()
print("Sorted List is:", new_list)

while True:
    answer = input("Do you want to another number to List? (yes/no) ")
    if answer.lower() == "yes":
        new_num = input("Enter a number to add to the list: ")
        sort_and_add_to_list(new_list, new_num)
    elif answer.lower() == "no":
        print("Thank YOU!")
        break
    else:
        print("Invalid input, please enter 'yes' or 'no'")
