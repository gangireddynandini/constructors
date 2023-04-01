import time,sys
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
s1=student(2,"hj")
s2=s1
s3=s2
print("no longer to maintain s1 memory")
s1=None
print("no longer to maintain s2 memory")
del s2
print(sys.getsizeof(s3))
time.sleep(5)
print("\n prgrm exwcution ended")
time.sleep(5)