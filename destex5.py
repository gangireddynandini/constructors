import time
class student:
    def __init__(self,sno,sname):
        print("im from pc")
        self.sno=sno
        self.sname=sname
        print("\t{}\t{}".format(self.sno,self.sname))
    def __del__(self):
        print("gc calls des")
#main prgrm
print("prgrm execution start")
s1=student(1,"gh")
s2=s1
s3=s2
print(id(s1),id(s2),id(s3))
time.sleep(5)
print("\n prgrm exwcution ended")
time.sleep(5)