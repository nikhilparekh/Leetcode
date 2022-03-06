class UndergroundSystem:

    def __init__(self):
        self.ins = {}
        self.out = {}
        self.avg = {}
        self.trips = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ins[id] = [stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_time = self.ins[id][1]
        if self.ins[id][0]+"-"+stationName in self.out:
            self.out[self.ins[id][0]+"-"+stationName]+=(t-in_time)
        else:
            self.out[self.ins[id][0]+"-"+stationName] = t-in_time
        if  self.ins[id][0]+"-"+stationName in self.trips:
            self.trips[self.ins[id][0]+"-"+stationName]+=1
        else:
            self.trips[self.ins[id][0]+"-"+stationName]=1
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # if (startStation+"-"+endStation) in self.avg:
        #     return self.avg[startStation+"-"+endStation]
        return self.out[startStation+"-"+endStation]/self.trips[startStation+"-"+endStation]
                
                
            
    

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)