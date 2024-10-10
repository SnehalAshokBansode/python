class Student:
    def GetStudent(self):
        self.RollNo = int(input("\nEnter Student Roll No: "))
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Student Age: "))
        self.Gender = input("Enter Student Gender: ")

    def PutStudent(self):
        print("Student Roll No:", self.RollNo)
        print("Student Name:", self.Name)
        print("Student Age:", self.Age)
        print("Student Gender:", self.Gender)


class Test(Student):
    def GetMarks(self):
        self.MarkMar = int(input("Enter Marks of Marathi Subject: "))
        self.MarkHin = int(input("Enter Marks of Hindi Subject: "))
        self.MarkEng = int(input("Enter Marks of English Subject: "))

    def PutMarks(self):
        print("Marks in Marathi:", self.MarkMar)
        print("Marks in Hindi:", self.MarkHin)
        print("Marks in English:", self.MarkEng)

    def TotalMarks(self):
        return self.MarkMar + self.MarkHin + self.MarkEng


# Create three objects of the Test class
students = []
for i in range(3):
    print(f"\nEntering details for Student {i + 1}:")
    student = Test()
    student.GetStudent()
    student.GetMarks()
    students.append(student)

# Display details of each student
for student in students:
    student.PutStudent()
    student.PutMarks()
    print("Total Marks:", student.TotalMarks())
