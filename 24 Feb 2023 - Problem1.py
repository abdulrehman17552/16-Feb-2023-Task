def add_to_list(key, value, lst):
    # check key and add item to list
    if key in [item[0] for item in lst]:
        print("Key already exists, please choose another key.")
    else:
        lst.append((key, value))


my_list = []

while True:
    # length of list 10
    if len(my_list) == 10:
        print("List is full, cannot add more items.")
        break

    key = input("Enter a key: ")
    value = input("Enter a value: ")
    add_to_list(key, value, my_list)
    print(my_list)
