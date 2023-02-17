""" Problem 1: Math and Biology Students in class """
def students():
    total_students = int(input("Enter total number of students in the class: "))
    math_students = int(input("Enter number of students with mathematics: "))
    bio_students = int(input("Enter number of students with biology: "))

    with_math_bio = math_students + bio_students
    without_math_bio = total_students - (math_students + bio_students)

    print("Number of students with math and bio: ", with_math_bio)
    print("Number of students without math and bio: ", without_math_bio)

students()
