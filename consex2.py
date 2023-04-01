class student:
    def __init__(self,sno,sname):
        self.sno=sno
        self.name=sname
s=student(10,"nandini")
print("initial content os s=",s.__dict__)
s1=student(20,"tr")
print("initial content of s1=",s1.__dict__)
s2=student(30,"hr")
print("initial content of s2=",s2.__dict__)
