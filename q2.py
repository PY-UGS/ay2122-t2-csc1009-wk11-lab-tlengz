class clockTime:
    def __init__(self):
        self.hrs = 0
        self.mins = 0
        self.sec = 0
    
    def setHours(self, hrs):
        self.hrs = hrs
    
    def setMinutes(self, mins):
        self.mins = mins
    
    def setSec(self, sec):
        self.sec = sec
    
    def setTime(self, hrs, mins, sec):
        self.setHours(hrs)
        self.setMinutes(mins)
        self.setSec(sec)
    
    def showTime(self):
        time = str(self.hrs + ":" + self.mins + ":" + self.sec)
        return time

time = clockTime()
hours = input('hrs:')
time.setHours(hours)
mins = input('mins:')
time.setMinutes(mins)
sec = input('sec:')
time.setSec(sec)

print("Time now: " + time.showTime())