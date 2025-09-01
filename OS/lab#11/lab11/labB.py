import multiprocessing

def processA(v):
    v.value = 23
    print("Process one has changed shared value:", v.value)

def processB(v):
    v.value = 50
    print("Process two has changed shared value:", v.value)

if __name__ == "__main__":
    v = multiprocessing.Value("i", 0)  
    
    p1 = multiprocessing.Process(target=processA, args=(v,))
    p2 = multiprocessing.Process(target=processB, args=(v,))
    
    p1.start()
    p1.join()
    
    p2.start()
    p2.join()
