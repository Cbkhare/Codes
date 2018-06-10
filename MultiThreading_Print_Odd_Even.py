import threading

class MyThread(object):

    def __init__(self, event1, event2):
        self.event1 = event1
        self.event2 = event2

    def run(self,i,e,jump):

        for i in range(i,e,jump):
            print(i)
            self.event1.set()
            self.event2.clear()
            self.event2.wait()
        self.event1.set()




if __name__=="__main__":

    event1 = threading.Event()
    event2 = threading.Event()
    mt = MyThread(event1, event2)
    tm = MyThread(event2,event1)
    t1 = threading.Thread(target=mt.run, args=(0,100,2))
    t2 = threading.Thread(target=tm.run, args=(1,100,2))

    t1.start()
    t2.start()
    t1.join()
    t2.join()