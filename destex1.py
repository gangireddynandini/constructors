import sys
class student:
    def __init__(self,sno,sname):
        print("im from pc")
        self.sno=sno
        self.sname=sname
        print("\t{}\t{}".format(self.sno,self.sname))

    def __del__(self):
        global totmem
        print("gc calls __del__")
        print("at present memory space:{}".format(totmem))
        print("now memory space:",sys.getsizeof(self))
        totmem=totmem-sys.getsizeof(self)
        print("remaining memory space:{}".format(totmem))
#mainprogram
s1=student(10,"rs")
s2=student(20,"tr")
print(sys.getsizeof(s1))
print(sys.getsizeof(s2))
totmem=sys.getsizeof(s1)+sys.getsizeof(s2)
print("now memory space in main prgrm:",totmem)
print("prgrm execution ended")
