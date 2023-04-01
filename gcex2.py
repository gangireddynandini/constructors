import time,gc
class student:
    def __init__(self,sno,sname):
        print("im from pc")
        self.sno=sno
        self.sname=sname
        print("\t{}\t{}".format(self.sno,self.sname))
    def __del__(self):
        print("gc calls des")
        print("is gc is running:", gc.isenabled())


#main prgrm
print("[rgrm execution started")
print("is gc is running:",gc.isenabled())
s1=student(3,"df")
print("now we r no longer in maintaining s1 memory space")
time.sleep(3)
# gc.disable()
print("is gc is running:",gc.isenabled())
