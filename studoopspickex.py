
import sys,pickle
from student import student
class studpick:
    def savestud(self):
        with open("oopsstud.data","ab") as fp:
            while(True):
                sno=int(input('enter student no:'))
                sname=input("enter student name:")
                marks=int(input("enter student marks:"))
                s=student(sno,sname,marks)
                pickle.dump(s,fp)
                print("student data saved in a file")
                ch=input("do u want to insert one more rec:")
                if(ch.lower()=="no"):
                    print("thnx")
                    sys.exit()
sp=studpick()
sp.savestud()
student.dispstuddata()

