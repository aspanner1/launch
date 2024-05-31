class Student: 
    
    @classmethod
    def get_school(cls):
        return "Stanford"
    
    def __init__(self, name, school):
        self._name = name 
        self._school = school 
        
    @property 
    def name(self):
        return self._name
        
    @property 
    def school(self):
        return self._school
        
student_1 = Student("Greg", "Stanford")
student_2 = Student("Susan", "Stanford")

print(student_1.name)
print(student_2.school)

print(student_1.get_school())
    