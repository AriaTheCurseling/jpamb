#!/usr/bin/env python3
import sys

class Odds:
    internal: float
    
    def __init__(self):
        self.internal = 1
        
    def __init__(self, odds):
        self.internal = odds
        
    @staticmethod
    def fromChance(chance):
        return Odds(chance / (1 - chance))
    
    @staticmethod
    def fromPercentage(percent):
        return Odds(percent / (100 - percent))
    
    @staticmethod
    def fromOdds(odds):
        return Odds(odds)
        
    def asChance(self):
        return 1 - 1 / (1 + self.internal)
    
    def asPercent(self):
        return 100 - 100 / (1 + self.internal)
    
    def asOdds(self):
        return self.internal
    
    def __str__(self):
        if self.internal >= 1:
            return f"Odds are {self.internal} to 1"
        elif self.internal > 0:
            return f"Odds are 1 to {1/self.internal}"
        else:
            return "Odds are 0 to 1"
        
    def __mul__(self, other):
        if other is Odds:
            return Odds(self.internal * other.internal)
        elif other is float or int or bool:
            return Odds(self.internal * other)
        
        raise Exception(f"Unexpected datatype ({type(other)}) in Odds multiplication")
    
    def __truediv__(self, other):
        if other is Odds:
            return Odds(self.internal / other.internal)
        elif other is float or int or bool:
            return Odds(self.internal / other)
        
        raise Exception(f"Unexpected datatype ({type(other)}) in Odds multiplication")

class multiOdds(dict):
    def sum(self):
        sum = 0
        
        for value in self.values():
            sum += value
        
        return sum
    
    def asPercent(self):
        sum = self.sum()
        percentages = dict()
        
        for (key, value) in self.items():
            percentages.setdefault(key, value / sum * 100)
        
        return percentages
        
# ignored for now
method_name = sys.argv[1].lower().replace(" ","")

assertionError = "assertion error"
noError = "ok"
programHalts = "*"
zeroDivionsError = "divide by zero"
outOfBounds = "out of bounds"

odds = multiOdds({assertionError: 1.0, noError: 100.0, programHalts: 1.0,  zeroDivionsError: 1.0, outOfBounds: 1.0})

# assertionOdds = Odds.fromPercentage(0)
# okOdds = Odds.fromPercentage(100)
# divideByZeroOdds = Odds.fromPercentage(0)
# whileTrueOdds = Odds.fromPercentage(0)
# outOfBoundsOdds = Odds.fromPercentage(0)

if "assert" in method_name:
    odds[assertionError] += 200
    
# if "divide" in method_name:
#     divideByZeroOdds *= 12
    
# if "error" in method_name:
#     okOdds /= 10000
    
# sum = 1
# (okOdds.asChance()**2 + assertionOdds.asChance()**2 + divideByZeroOdds.asChance()**2 + whileTrueOdds.asChance()**2 + outOfBoundsOdds.asChance()**2)**0.5

for (key, value) in odds.asPercent().items():
    print(f"{key};{value}%")