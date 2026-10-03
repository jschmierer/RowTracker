from workout import Workout
from timedworkout import TimedWorkout
from distancedworkout import DistancedWorkout

# stores many workouts, in a list
class StatsDash():

    def __init__(self, workouts=[]):
        self.workouts = workouts

    def addWorkout(self):
        type = input("Timed or distance? [t/d] ")
        if type == "t":
            workout = TimedWorkout()
        else:
            workout = DistancedWorkout()
        workout.recordWorkout()
        self.workouts.append(workout)


    def printWorkout(self, i):
        self.workouts[i].printWorkout()


    def printLastWorkout(self):
        self.workouts[-1].printWorkout()

    def printAllWorkouts(self):
        for workout in self.workouts:
            workout.printWorkout()

    def printWorkoutTypes(self):
        printed = []
        for i in range(len(self.workouts)):
            workout = self.workouts[i]
            if isinstance(workout, TimedWorkout):
                x = 0
            else:
                x = 1
            toprint = ""
            if not workout.isVariable and len(workout.ints) > 1:
                toprint = str(len(workout.ints)) + " x " + str(workout.ints[0][x])
            else:
                for j in range(len(workout.ints)):
                    interval = workout.ints[j][x]
                    if j == len(workout.ints) - 1:
                        toprint += interval
                    else:
                        toprint += interval + ", "
            if toprint in printed:
                continue
            print("Type " + str(i+1) + ": " + toprint)
            printed.append(toprint)

    # show all types of workout so user can pick one
    # search through workout list to find all workouts of that type
    # select best one
    # print it
    def findBestWorkout(self):
        print("Which workout type would you like to find?")
        self.printWorkoutTypes()
        num = int(input("Enter workout type here: "))
        workout = self.workouts[num - 1]
        # best is first index of that workout type
        best = num - 1
        type = isinstance(workout, TimedWorkout)
        if type:
            x = 0
        else:
            x = 1
        # look through all other workouts
        for i in range(num, len(self.workouts)):
            otherworkout = self.workouts[i]
            # if it is the same type of workout as the one we're looking for (timed/distance)
            if isinstance(otherworkout, TimedWorkout) == type:
                # if it is the same time/distance as the one we're looking for
                if workout.avgInt[x] == otherworkout.avgInt[x]:
                    otherworkout.printWorkout()
                    print(otherworkout.avgInt)
                    print(Workout.timeFormat(otherworkout.avgInt[2], True))
                    print(Workout.timeFormat(workout.avgInt[2], True))
                    # if the split of this new one is better than split of current one
                    if Workout.timeFormat(otherworkout.avgInt[2], True) < Workout.timeFormat(workout.avgInt[2], True):
                        best = i
        bestworkout = self.workouts[best]
        print("Here's your PR for that workout:")
        bestworkout.printWorkout()

        

    