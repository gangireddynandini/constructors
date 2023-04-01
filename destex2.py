import time,sys
class student:
    def __init__(self,sno,sname):
        print("im from pc")
        self.sno=sno
        self.sname=sname
        print("\t {}\t{}".format(self.sno,self.sname))
        #def __del__(self):
            #print("gc calls dest")
#main prgrm
print("\n prgrm execution started")
s1=student(10,"hj")
print(sys.getsizeof(s1))
print("now we r no longer in maintaining s1 memory")
time.sleep(5)
s1=None
print(sys.getsizeof(s1))
time.sleep(5)
s2=student(20,"tr")
print(sys.getsizeof(s2))
print("prgrm execution ended")
s2=None
print(sys.getsizeof(s1))


