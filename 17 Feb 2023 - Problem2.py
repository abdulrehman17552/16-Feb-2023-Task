import queue

my_lifo_queue = queue.LifoQueue()

def add_n_elements_to_lifo_queue(num):
    # ADD Elements to my_lifo_queue
    for i in range(num):
        element = input(f'Enter the {i + 1} element: ')
        my_lifo_queue.put(element)

    return my_lifo_queue

def pop_n_elements_from_lifo_queue(num):
    # POP Elements to my_lifo_queue
    for i in range(num):
        if my_lifo_queue.empty():
            print("Error: LIFO queue is empty")
            return
        else:
            print("Elements poped from queue are: ",my_lifo_queue.get())
    if my_lifo_queue.empty():
        print("LIFO queue is now empty")

while True:
    answer = input("Type 'add', 'pop' or 'exit' to perform an action: ")
    if answer.lower() == "add":
        while True:
            try:
                # Add Number of elements
                add_element = int(input("Enter the number of elements to add to the LIFO queue: "))
                if add_element < 0:
                    raise ValueError("Error. Please enter an integer.")
                break
            except ValueError:
                print("Error. Please enter an integer.")
                continue

        add_n_elements_to_lifo_queue(add_element)

    elif answer.lower() == "pop":

        while True:
            try:
                # POP Number of elements
                pop_element = int(input("Enter the number of elements to pop from the LIFO queue: "))
                if pop_element < 0:
                    raise ValueError("Error. Please enter an integer.")
                break
            except ValueError:
                print("Error. Please enter an integer.")
                continue

        pop_n_elements_from_lifo_queue(pop_element)

    elif answer.lower() == "exit":
        print("Thank YOU!")
        break
    else:
        print("Invalid input, please enter 'add', 'pop'  or 'exit'")
