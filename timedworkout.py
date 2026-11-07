from workout import Workout

class TimedWorkout(Workout):

    # intervals should be in a list, with elements tuples as ("time", distance, "split", "rest")
    def __init__(self, i=[], v=False):
        super().__init__()
        self.ints = i
        self.isVariable = v
        self.avgHr = 0
        self.maxHr = 0
        if len(i) > 1:
            self.avgInt = self.calcAverage(self.ints)
        else:
            self.avgInt = None

    # workout structure will be ("time", distance, "split", "rest")   
    def recordWorkout(self):
        print("** STEP 1: Create the workout **")
        tlist = []
        flag = True
        n = input("How many intervals? [enter if none] ").strip()
        if not n:
            n = 1
        else:
            n = int(n)
            v = input("Variable intervals? [y/n] ").strip()
            if v == "y":
                self.isVariable = True
                flag = False
                for i in range(n):
                    temp = input("Time for interval " + str(i+1) + "? ")
                    if i < n - 1:
                        temp2 = input("Rest for interval " + str(i+1) + "? ")
                    else:
                        temp2 = 0
                    tlist.append((temp, temp2))
        if flag:
            if n > 1:
                temp = input("Time per interval? ")
                temp2 = input("Rest per interval? ")
                temp = (temp, temp2)
            else:
                temp = input("Time? ")
            for i in range(n):
                tlist.append(temp)

        print("\n** STEP 2: Record your time **")
        for i in range(len(tlist)):
            if n == 1:
                split = input("Enter split (per 500m): ")
            else:
                split = input("Enter split (per 500m) for interval " + str(i + 1) + ": ")
            dist = self.findDist(tlist[i][0], split)
            interval = (tlist[i][0], dist, split)
            if len(tlist[i]) > 1:
                interval = (tlist[i][0], dist, split, tlist[i][1])
            self.ints.append(interval)
        print()
        self.avgHr = int(input("Enter average heart rate: "))
        self.maxHr = int(input("Enter max heart rate: "))

        self.avgInt = self.calcAverage(self.ints)
        #print(self.avgInt)

    def findDist(self, time, split):
        time = self.timeFormat(time, True)
        split = self.timeFormat(split, True)
        dist = int(time / split * 500)
        return dist

    def intervalToString(self, int):
        time = int[0]
        split = int[2]
        dist = str(int[1])
        return "Time: " + time + "\tSplit: " + split + "/500m\tDistance: " + str(dist) + "m"

    def intervalToData(self, int):
        time = self.timeFormat(int[0], True)
        split = self.timeFormat(int[2], True)
        return (time, split)
