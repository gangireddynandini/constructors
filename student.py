
class student:
    def __init__(self,sno,sname,marks):
            self.sno=sno
            self.sname=sname
            self.marks=marks

    def dispstuddata(self):
        print("\t{}\t{}\t{}".format(self.sno,self.sname,self.marks))

