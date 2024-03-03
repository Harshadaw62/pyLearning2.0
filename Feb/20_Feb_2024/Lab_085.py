class Student:
    stud_id=None
    stud_name=None

    def display_stud(self):

        print(f"Student id: {self.stud_id} \n Student Name: {self.stud_name}")

class Course:
    def course_info(self,course_id,course_name):
        print("Course_id: ",course_id,"\n Course name: ",course_name)

class Transaction:
    def transaction_info(self,payment_method,amount):
        print(f"Payment method: {payment_method} \n Amount: {amount}")

stud1=Student()
stud1.stud_id=1
stud1.stud_name="Harshada"
stud1.display_stud()


course1=Course()
course1.course_info(101,"Python")
course2=Course()
course2.course_info(102,"Java")

trans1=Transaction()
trans1.transaction_info("Stripe",8000)
trans2=Transaction()
trans2.transaction_info("Razorpay",10000)

