import time

class Tokenbucket:
    def __init__(self,capacity,refill_rate):
        self.capacity = capacity
        self.refill = refill_rate
        self.token = capacity
        self.last_time_filled = time.time()
    
    def allow_request(self):
        now = time.time()
        time_elapsed = now - self.last_time_filled
        refill = (self.refill*time_elapsed)
        
        if refill>=self.refill:
            self.token = min(self.capacity,self.token+int(refill))
            self.last_time_filled += refill / self.refill
        if self.token>=1:
            self.token-=1
            return True
        
        else:
            return False

