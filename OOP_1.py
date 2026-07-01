# Student Management Project
class Student:
    
    def __init__(self,roll_no,name,age,marks):
        self.roll_no=roll_no;
        self.name=name;
        self.age=age;
        self.marks=marks;
        
    def display_details(self):
        print(f"Student: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
        print(f'Pass or Failed:{self.is_pass()}')
        
    def update_marks(self,marks):
        self.marks=marks;
    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"
    def is_pass(self):
        if self.marks>=50:
            return "Passed";
        else:
            return "Failed";
    
a=Student("123","Priya",21,88);
b=Student("124","Suhani",20,78);
c=Student("125","Shan",29,22);
d=Student("126","Simmi",21,66);
e=Student("127","Naman",22,99);
list1=[a,b,c,d,e];

for student in list1:
    student.display_details()
    student.calculate_grade()
    print("-" * 30)   

topper=list1[0]
for student in list1:
    if student.marks > topper.marks:
        topper = student

print(f"Topper of the class is {topper.name} and secured the marks {topper.marks}");

average_marks=0;
for student in list1:
    average_marks+=student.marks;

average_percent=average_marks/len(list1);
    
print(f"The average marks of this section is { average_percent}")

for student in list1:
    if(student.marks>75):
        student.display_details();
        
        
sorted_students = sorted(list1, key=lambda student: student.marks,reverse=True)

rank = 1

for student in sorted_students:
    print(rank, student.name, student.marks)
    rank += 1