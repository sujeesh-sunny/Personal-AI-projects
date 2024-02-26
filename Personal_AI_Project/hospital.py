import self


class Hospital:
    def __init__(self, admin_name, doctor_name, sister_name, department):
        self.admin_name = admin_name
        self.doctor_name = doctor_name
        self.sister_name = sister_name
        self.department = department

    def get_names(self):
        self.admin_name = input("Enter admin name: ")
        self.doctor_name = input("Enter doctor name: ")
        self.sister_name = input("Enter sister name: ")
        self.department = input("Enter department name: ")

    def print_names(self):
        print("ADMIN NAME: ", self.admin_name)
        print("DOCTOR NAME: ", self.doctor_name)
        print("SISTER NAME: ", self.sister_name)
        print("DEPARTMENT: ", self.department)


class Patient(Hospital):
    def __init__(self, name, age, disease, ):
        self.name = name
        self.age = age
        self.disease = disease

    def get_patient_details(self):
        self.name = input("Enter patient name: ")
        self.age = input("Enter patient age: ")
        self.disease = input("Enter patient disease: ")

    def print_patient_details(self):
        print("PATIENT NAME: ", self.name)
        print("PATIENT AGE: ", self.age)
        print("PATIENT DISEASE: ", self.disease)


hospital = Hospital("", "", "", "")
hospital.get_names()
hospital.print_names()

patient = Patient("", "", "")
patient.get_patient_details()
patient.print_patient_details()
