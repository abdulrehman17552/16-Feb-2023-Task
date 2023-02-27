import random

def add_to_list(new_value, my_list):
    if new_value in my_list:
        print(f"Value {new_value} is already in the list.")
    else:
        my_list.append(new_value)
        print("The updated list is: ", my_list)


my_list = []
for i in range(10):
    my_list.append(random.randint(0, 100))

print(f"The initial list is: {my_list}")

while True:
    new_value = int(input("Enter a new value to add to the list: "))
    add_to_list(new_value , my_list)