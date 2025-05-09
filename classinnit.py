'''class Student:
    def __init__(self):
        choice = input("(A) BCA \n(B) BCA+MCA \nEnter your choice = ")
        if choice == "A" or "a":
            print("Duration of your course is 3 years")
        elif choice == "B" or "b":
            print("Duration of your course is 5 years")
        else:
            print("You have entered a wrong choice")


class Result:
    def __init__(self):
        self.c = input("Enter your name: ")
        self.d = int(input("Enter your marks in Python: "))
        self.e = int(input("Enter your marks in DBMS: "))
        self.f = int(input("Enter your marks in C programming: "))
        print("Name of student is:", self.c)
        percentage = (self.d + self.e + self.f) / 3
        print("Total percentage of student is:", percentage)


# Create objects to execute code
Student()
Result()
'''



'''
class Student:
    def __init__(self):
        choice = input("(A) BCA \n(B) BCA+MCA \nEnter your choice = ").lower()
        if choice == "a":
            print("Duration of your course is 3 years")
        elif choice == "b":
            print("Duration of your course is 5 years")
        else:
            print("You have entered a wrong choice")
            exit()



class Result:
    def __init__(self):
        self.c = input("Enter your name: ")
        self.d = int(input("Enter your marks in Python: "))
        self.e = int(input("Enter your marks in DBMS: "))
        self.f = int(input("Enter your marks in C programming: "))
        self.percentage = (self.d + self.e + self.f) / 3
        self.grade = self.get_grade()

    def get_grade(self):
        if self.percentage >= 90:
            return "A"
        elif self.percentage >= 75:
            return "B"
        elif self.percentage >= 60:
            return "C"
        elif self.percentage >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nStudent Name:", self.c)
        print("Percentage:", self.percentage)
        print("Grade:", self.grade)


# Main Program
num_students = int(input("How many students do you want to enter? "))
for i in range(num_students):
    print(f"\n--- Student {i + 1} ---")
    Student()
    result = Result()
    result.display()
'''
class Student:
    def __init__(self):
        self.choice = input("(A) BCA \n(B) BCA+MCA \nEnter your choice = ").lower()

    def is_valid_choice(self):
        if self.choice == "a":
            print("Duration of your course is 3 years")
            return True
        elif self.choice == "b":
            print("Duration of your course is 5 years")
            return True
        else:
            print("You have entered a wrong choice. Skipping this student.")
            return False


class Result:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.python = int(input("Enter your marks in Python: "))
        self.dbms = int(input("Enter your marks in DBMS: "))
        self.c_prog = int(input("Enter your marks in C programming: "))
        self.percentage = (self.python + self.dbms + self.c_prog) / 3
        self.grade = self.get_grade()

    def get_grade(self):
        if self.percentage >= 90:
            return "A"
        elif self.percentage >= 75:
            return "B"
        elif self.percentage >= 60:
            return "C"
        elif self.percentage >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nStudent Name:", self.name)
        print("Percentage:", round(self.percentage, 2))
        print("Grade:", self.grade)

    def to_text(self):
        return f"Name: {self.name}, Python: {self.python}, DBMS: {self.dbms}, C Programming: {self.c_prog}, Percentage: {round(self.percentage, 2)}%, Grade: {self.grade}"


# Main Program
all_results = []

while True:
    try:
        num_students = int(input("How many students do you want to enter? "))
        for i in range(num_students):
            print(f"\n--- Student {i + 1} ---")
            student = Student()
            if not student.is_valid_choice():
                continue  # Skip this student if invalid choice
            result = Result()
            result.display()
            all_results.append(result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    again = input("\nDo you want to enter more students? (y/n): ").lower()
    if again != 'y':
        break

# Display all collected results
print("\n====== All Students' Results ======")
for idx, res in enumerate(all_results, start=1):
    print(f"\n--- Student {idx} ---")
    res.display()

# Save to file
save = input("\nDo you want to save the results to a file? (y/n): ").lower()
if save == 'y':
    with open("student_results.txt", "w") as file:
        file.write("====== All Students' Results ======\n")
        for idx, res in enumerate(all_results, start=1):
            file.write(f"\n--- Student {idx} ---\n")
            file.write(res.to_text() + "\n")
    print("Results saved to 'student_results.txt'")
