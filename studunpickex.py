import pickle
class studunpick:
    def readrec(self):
        with open("filstu","rb") as fp:
            print("\tsno\tsname\tmarks")
            onj=pickle.load(fp)
            for val in onj:
                print(val)
s=studunpick()
s.readrec()