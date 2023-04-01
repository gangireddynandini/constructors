class student:
    def __init__(self,sno,sname):
        self.sno=sno
        self.sname=sname
        print("\t{}\t{}".format(self.sno,self.sname))
#main
print("prgrm execution started")
s1=student(10,"rs")
s2=student(20,"TR")
print("prgrm execution ended")
