import pickle
class studunpick:
    def readrecords(self):
        with open("oopsstud.data","rb") as fp:
            print("-"*30)
            print("\tsno\tname\tmarks")
            print("_"*30)
            while(True):
                try:
                    obj=pickle.load(fp)
                    obj.dispstuddata()

                except EOFError:
                    print("_"*30)
                    break

s=studunpick()
s.readrecords()
