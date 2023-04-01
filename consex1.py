class student:
    def __init__(self):
        self.sno=10
        self.name="andu"
s=student()
print("initial content os s=",s.__dict__)
s1=student()
print("initial content of s1=",s1.__dict__)
s2=student()
print("initial content of s2=",s2.__dict__)
