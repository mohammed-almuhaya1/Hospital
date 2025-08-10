class Patient_Affairs:
    patient_number = 1
    def __init__(self, **kwargs):
        self.patient_num = Patient_Affairs.patient_number
        self.name = kwargs.get("name", "Nothing")
        self.age = kwargs.get("age", "Nothing")
        self.patient_sex = kwargs.get("patient_sex", "Nothing")
        self.type_of_disease = kwargs.get("type_of_disease", "Nothing")
        self.address = kwargs.get("address", "Nothing")
        self.num = kwargs.get("num", "Nothing")
        Patient_Affairs.patient_number += 1
    
class DRA:
    # def ifs(self):
    def __init__(self, **kwargs):
        self.Patient = kwargs.get('Patient_Affair', Patient_Affairs())
        # self.type_of_disease = kwargs.get('type_of_disease', 'NA')

    def Orthopedic_doctor(self):
        symptoms = []
        i = ''
        while True:
            i = input("Enter symptoms of the disease: ")
            if i == 'stop':
                break
            symptoms.append(i)
        Arthritis = {"الم في المفاصل", "تورم المفاصل","الم في الظهر","فقدان الطول"}
        Bone_Tumors = {"الم في العظام", "كسر غير مبرر", "كتلة يمكن الشعور بها"}
        Osteonecrosi = {"فقدان القدرة على الحركة","العرج", "تصلب المفاصل"}
        if all(item in Arthritis for item in symptoms):
            print("Please do the following tests: DEXA, CBC")
            Examination_types = ["DEXA", "CBC"]
            lab = laboratore(Patient_Affair = self.Patient, Examination_types = Examination_types)
            # results.Examination_types = ["DEXA", "CBC"]
            result = lab.DEXA()
            if result["result"] == "negative":
                print("yes")
        
        if all(item in Bone_Tumors for item in symptoms):
            print("hello world")

        if all(item in Osteonecrosi for item in symptoms):
            print("hello world")

        else :
            print("you don't have bone disease!!")
    # if self.type_of_disease == "mm":
    #     Orthopedic_doctor()


    # if self.type_of_disease == "mw":
    def internal_medicine_doctor():
        symptoms = {}
        while i != "stop" :
            i = input("Enter symptoms of the disease: ")
            symptoms.add(i)
        stomach_ulcer = {"الم في البطن", "حرقة في المعدة", "انتفاخات", "غثيان وقي", "فقدان الشهية", "تغير في لون البراز"}
        hepatitis = {"اصفرار العيون", "التعب والارهاق الشديد", "الم في البطن خاصة في الجزء العلوي الايمن", "البول الداكن", "البراز الفاتح", "الحمى", "الم المفاصل"}
        stomach_germ = {"فقدان الوزن الغير مبرر", "الشعور ب الانتفاخ والتجشؤ", "البراز الاسود","البراز الدموي", "التقيؤ الدموي", "صعوبة في البلع"}
        if all(item in stomach_ulcer for item in symptoms):
            print("hello world")

        if all(item in hepatitis for item in symptoms):
            print("hello world")

        if all(item in stomach_germ for item in symptoms):
            print("hello world")

        else :
            print("you don't have bone disease!!")
    # internal_medicine_doctor()

    # if self.type_of_disease == "mq":
    def pediatrician():
        symptoms = {}
        while i != "stop" :
            i = input("Enter symptoms of the disease: ")
            symptoms.add(i)
        Arthritis = {"الم في المفاصل", "تورم المفاصل", "تصلب المفاصل"}
        Bone_Tumors = {"الم في العظام", "كسر غير مبرر", "كتلة يمكن الشعور بها"}
        Osteonecrosi = {"فقدان القدرة على الحركة", "العرج"}
        if all(item in Arthritis for item in symptoms):
            print("hello world")

        if all(item in Bone_Tumors for item in symptoms):
            print("hello world")

        if all(item in Osteonecrosi for item in symptoms):
            print("hello world")

        else :
            print("you don't have bone disease!!")
    # pediatrician()

    # if self.type_of_disease == "ms":
    def dentist():
        symptoms = {}
        while i != "stop" :
            i = input("Enter symptoms of the disease: ")
            symptoms.add(i)
        Arthritis = {"الم في المفاصل", "تورم المفاصل", "تصلب المفاصل"}
        Bone_Tumors = {"الم في العظام", "كسر غير مبرر", "كتلة يمكن الشعور بها"}
        Osteonecrosi = {"الم في المفصل", "تصلب في المفصل", "فقدان القدرة على الحركة"}
        if all(item in Arthritis for item in symptoms):
            print("hello world")

        if all(item in Bone_Tumors for item in symptoms):
            print("hello world")

        if all(item in Osteonecrosi for item in symptoms):
            print("hello world")

        else :
            print("you don't have bone disease!!")
    # dentist()

    def choose_doctor(self):
        if self.Patient.type_of_disease == 'mm':
            self.Orthopedic_doctor()
        if self.Patient.type_of_disease == 'mw':
            self.internal_medicine_doctor()
        if self.Patient.type_of_disease == 'mq':
            self.pediatrician()
        if self.Patient.type_of_disease == 'ms':
            self.dentist()

class laboratore:
    def __init__(self, **kwargs):
        self.Patient = kwargs.get('Patient_Affair', Patient_Affairs())
        self.Examination_types = kwargs.get('Examination_types', [])
    # Examination_types = []
    # if "DEXA" in Examination_types:
    def DEXA(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")
            
    # if "blood test" in Examination_types:
    def blood_test(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "CBC" in Examination_types:
    def CBC(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "ALB" in Examination_types:
    def ALB(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "ESR" in Examination_types:
    def ESR(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "GGT" in Examination_types:
    def GGT(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "ALP" in Examination_types:
    def ALP(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "AST" in Examination_types:
    def AST(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "ALT" in Examination_types:
    def ALT(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

    # if "examine feces" in Examination_types:
    def examine_feces(self):
        result = ""
        # Patient_Affairs.__init__(self, name, age, patient_sex)
        while result != "positive" or result != "negative":
            result = input("Enter the examination percentage: ")
            if result == "negative":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"negative"}
                return self.the_condition
            elif result == "positive":
                self.the_condition = {"name":self.Patient.name, "age":self.Patient.age, "sex":self.Patient.patient_sex, "result":"positive"}
                return self.the_condition
            else :
                print("Erro:")

if __name__ == "__main__":
    n =input("enter your name: ")
    m =input("enter your age: ")
    o =input("enter your sex: ")
    p =input("enter your type_of_disease: ")
    q =input("enter your address: ")
    r =input("enter your num: ")

    patient = Patient_Affairs(name = n, age = m, patient_sex = o, type_of_disease = p, address = q, num = r)
    # laboratore(Patient_Affair = patient)
    dra = DRA(Patient_Affair = patient)
    dra.choose_doctor()