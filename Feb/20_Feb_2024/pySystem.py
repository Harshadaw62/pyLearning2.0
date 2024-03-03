class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name

class Payment:
    def __init__(self, method):
        self.method = method

# Creating objects for students
vivek = Student("Vivek")
shreeram = Student("Shreeram")
vani = Student("Vani")

# Creating objects for courses
py_atb = Course("PyAtb")
mtb = Course("MTB")
atbj = Course("ATBJ")
apiat = Course("APIAT")

# Creating objects for payments
razorpay = Payment("Razorpay")
stripe = Payment("Stripe")
instamojo = Payment("Instamojo")

# Example usage
print("Student:", vivek.name)
print("Course:", py_atb.name)
print("Payment method:", instamojo.method)