class Logger:

    def __init__(self):
        self.last_print = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_print:
            if timestamp-self.last_print[message]<10:
                return False
        self.last_print[message] = timestamp
        return True
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
