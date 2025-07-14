import time
class LeakyBucket:
    def __init__(self,queue_size,processing_rate):
        self.queue_size = queue_size
        self.processing_rate = processing_rate
        self.current_queue = 0
        self.last_request = time.time()
    
    def allow_request(self):
        now = time.time()
        leaked = int(self.processing_rate*(now-self.last_request))
        if leaked > 0:
            self.current_queue = max(0,self.current_queue-leaked)
            self.last_request = now
        if self.current_queue < self.queue_size:
            self.current_queue+=1
            return True
        else:
            return False

        
start_time = time.time()
obj = LeakyBucket(1,0)
for i in range(10):
    print(obj.allow_request())
    time.sleep(1)
    print(time.time()-start_time)
