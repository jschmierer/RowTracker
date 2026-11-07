import time

class CustomWorkout():
    def __init__(self, t="", d=""):
        self.date = time.strftime("%m-%d-%Y %H:%M:%S", time.localtime())
        self.title = t
        self.details = d

    def recordWorkout(self):
        self.title = input("What is this workout called? ").strip()
        self.details = input("What are the details of the workout? ").strip()
        self.avgHr = int(input("What was your average heart rate? "))
        self.maxHr = int(input("What was your max heart rate? "))

    def printWorkout(self):
        print("Date: " + self.date)
        print("Average heart rate: " + str(self.avgHr) + "\tMax heart rate: " + str(self.maxHr))
        print("Title: " + self.title)
        print("Details: " + self.details)
