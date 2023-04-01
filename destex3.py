import time,sys
class student:
    def __init__(self,sno,sname):
        print("im from pc")
        self.sno=sno
        self.sname=sname
        print("\t {}\t{}".format(self.sno,self.sname))
        def __del__(self):
            print("gc calls dest")
#main prgrm
print("\n prgrm execution started")
s1=student(2,"hj")
s3=student(23,"gh")
print("now we r no longer in maintaining s1 memory")
time.sleep(5)
del s1
time.sleep(5)
s2=student(20,"tr")
print("now we r no longer in maintaining s2 memory")
print(sys.getsizeof(s2))
del s2
time.sleep(5)
print("prgrm execution ended")