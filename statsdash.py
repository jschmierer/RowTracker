from timedworkout import TimedWorkout
from distancedworkout import DistancedWorkout

# stores many workouts, in a list
class StatsDash():

    def __init__(self, workouts=[]):
        self.workouts = workouts
        self.bestTimedWorkout = TimedWorkout([("5:00", 1500, "30:00")])
        self.bestDistancedWorkout = DistancedWorkout([("5:00", 1500, "30:00")])

    def addWorkout(self):
        type = input("Timed or distance? [t/d] ")
        if type == "t":
            workout = TimedWorkout()
        else:
            workout = DistancedWorkout()
        workout.recordWorkout()
        self.workouts.append(workout)


    def printLastWorkout(self):
        self.workouts[-1].printWorkout()


    def printAllWorkouts(self):
        for workout in self.workouts:
            workout.printWorkout()


    def printWorkoutTypes(self):
        for i in range(len(self.workouts)):
            workout = self.workouts[i]
            print("Type " + str(i+1) + ": ",end="")
            if isinstance(workout, TimedWorkout):
                x = 0
            else:
                x = 1
            if not workout.isVariable and len(workout.ints) > 1:
                print(str(len(workout.ints)) + " x " + str(workout.ints[0][x]))
            else:
                for i in range(len(workout.ints)):
                    if i == len(workout.ints) - 1:
                        print(workout.ints[i][x])
                    else:
                        print(workout.ints[i][x], end=", ")

    