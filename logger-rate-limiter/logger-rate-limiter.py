class Logger:

    def __init__(self):
        self.di = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.di:
            if self.di[message]>timestamp:
                return False
            else:
                self.di[message]=timestamp+10
        else:
            self.di[message]=timestamp+10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)