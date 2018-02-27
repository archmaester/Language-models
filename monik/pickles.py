import pickle as pickle
import dill

class pickles:
    def pickling(p1):
        fp = open(p1.filename,'w')
        pickle.dump(p1.object1,fp)
        fp.close()
        
    def unpickling(p1):
        fp1 = open(p1.filename, 'r')
        p1.object1 =  pickle.load(fp1)
        fp1.close()
        return p1.object1 
    def picklingdill(p1):
        pdict1 = dill.dumps(p1.object1)
        fp = open(p1.filename,'w')
        pickle.dump(pdict1,fp)
        fp.close()

    def unpicklingdill(p1):
        fp = open(p1.filename,'r')
        pdict2 = pickle.load(fp)
        fp.close()
        object1 = dill.loads(pdict2)
        return object1
    