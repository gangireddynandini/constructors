class student:
    def getstud(self):
        self.sno=20
        self.sname="nandu"
s=student()
print("content of s before inserting data",s.__dict__)
s.getstud()
print("content of s after inserting data",s.__dict__)