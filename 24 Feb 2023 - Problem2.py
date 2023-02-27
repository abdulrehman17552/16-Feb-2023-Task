def add_to_list(value, lst):
    lst.insert(0, value)
    if len(lst) > 5:
        lst.pop()

my_list = []

for i in range(5):
    value = input(f"Enter {i+1} Value: ")
    my_list.insert(0,value)
print(my_list)
while True :
    value = input("Enter a Value: ")
    add_to_list(value, my_list)
    print(my_list)
