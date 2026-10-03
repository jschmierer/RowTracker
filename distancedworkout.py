from workout import Workout

class DistancedWorkout(Workout):

    # intervals should be in a list, with elements tuples as ("distance", "split")
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

    # workout structure will be ("time", distance, "split")   
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
                    temp = int(input("Distance for interval " + str(i+1) + "? "))
                    tlist.append(temp)
        if flag:
            if n > 1:
                temp = int(input("Distance per interval? "))
            else:
                temp = int(input("Distance? "))
            for i in range(n):
                tlist.append(temp)

        print("\n** STEP 2: Record your time **")
        for i in range(len(tlist)):
            if n == 1:
                split = input("Enter split (per 500m): ")
            else:
                split = input("Enter split (per 500m) for interval " + str(i + 1) + ": ")
            time = self.findTime(tlist[i], split)
            self.ints.append((time, tlist[i], split))
        print()
        self.avgHr = int(input("Enter average heart rate: "))
        self.maxHr = int(input("Enter max heart rate: "))

        self.avgInt = self.calcAverage(self.ints)

    def findTime(self, dist, split):
        split = self.timeFormat(split, True)
        time = round(split * (dist/500), 1)
        time = self.timeFormat(time, False)
        return time

    def intervalToString(self, int):
        time = int[0]
        split = int[2]
        dist = str(int[1])
        return "Time: " + time + "\tSplit: " + split + "/500m\tDistance: " + str(dist) + "m"

    def intervalToData(self, k):
        time = self.timeFormat(self.ints[k], True)
        split = self.timeFormat(self.ints[k], True)
        return (time, split)