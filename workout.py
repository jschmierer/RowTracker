from abc import ABC, abstractmethod
import time

class Workout(ABC):

    def __init__(self):
        self.date = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime())

    @abstractmethod
    def recordWorkout(self):
        pass

    def calcAverage(self, ints):
        timeSum = 0
        distSum = 0
        for i in ints:
            timeSum += self.timeFormat(i[0], True)
            distSum += i[1]
        avgSplit = round(timeSum / distSum * 500, 1)
        return (self.timeFormat(timeSum, False), distSum, self.timeFormat(avgSplit, False))


    # true: 15:00 to 900, false: 900 to 15:00
    def timeFormat(self, time, direction):
        """True: 15:00 to 900, False: 900 to 15:00"""
        if direction:
            if time.count(':') == 2:
                colpos1 = time.index(':')
                colpos2 = time.index(':', colpos1+1)
                total = float(time[colpos2+1:])
                total += int(time[colpos1+1:colpos2]) * 60
                total += int(time[:colpos1]) * 3600
            else:
                colpos = time.index(':')
                total = float(time[colpos+1:])
                total += int(time[:colpos]) * 60
            return total
        hours = time // 3600
        time -= hours * 3600
        minutes = int(time / 60)
        seconds = round(time % 60, 1)
        if minutes < 10:
            minutes = "0" + str(minutes)
        if seconds < 10:
            seconds = "0" + str(seconds)
        if hours <= 0:
            return str(minutes) + ":" + str(seconds)
        return str(hours) + ":" + str(minutes) + ":" + str(seconds)


    def printWorkout(self):
        print("Date: " + self.date)
        if len(self.ints) > 1:
            print("Overall \t" + self.intervalToString(self.avgInt))
        for k in range(len(self.ints)):
            if len(self.ints) > 1:
                print("Interval " + str(k + 1), end="\t")
            print(self.intervalToString(self.ints[k]))