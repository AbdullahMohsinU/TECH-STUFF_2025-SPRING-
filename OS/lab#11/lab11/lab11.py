import multiprocessing
def sharedM(v):
 v.value= 2.678
 
v = multiprocessing.Value('d',0.0)
p1 = multiprocessing.Process(target= sharedM,args=(v,))
p1.start ()
p1.join ()
print (v.value)
