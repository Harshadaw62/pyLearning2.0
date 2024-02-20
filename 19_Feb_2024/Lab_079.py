# Automation Tester Blueprint (Py System
# Class -Students,Courses, Payments - Razorpay, Stipe, Instamojo

# Object
# Student (A/B) - > Vivek, Shreeram, Vani
# Course (A/B) -> PyAtb, MTB, ATBJ, APIAT
# Payments (A/B) - Razorpay, Stipe, Instamojo


class Student:
    name = None
    phone_no = None

    def watch_recordings(self):
        print("Reco", self.name)

    def do_assignment(self):
        print("Watch", self.name, self.phone_no)

    def do_coding_q(self,addr):
        print("Code",addr)


shreeram = Student()
shreeram.name = "Shreeram"
shreeram.phone_no = 9876543211
shreeram.watch_recordings()
shreeram.do_assignment()
shreeram.do_coding_q("pune")

bikas = Student()
bikas.name = "Vikas"
bikas.phone_no = 8976452310
bikas.watch_recordings()
bikas.do_assignment()
bikas.do_coding_q("Mumbai")

vani = Student()
