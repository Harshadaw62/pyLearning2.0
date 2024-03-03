class Mul_param:
    addr = None  # Class Variable

    def print_information(self, first_name, last_name, age):
        a = 10  # Local Variable
        print("Your name is ", first_name, last_name, age)
        print(self.addr)


obj_ref = Mul_param()
obj_ref.addr="Pune"
obj_ref.print_information("Amit", "Sharma", 68)