from timedworkout import TimedWorkout
from distancedworkout import DistancedWorkout
from statsdash import StatsDash
from user import User

user = User("jschmierer", "password10", 17, "Jakob Schmierer")

#user.sd.addWorkout()
#user.sd.printAllWorkouts()

sd = StatsDash([TimedWorkout([("15:00", 4500, "1:53")]), DistancedWorkout([("45:00", 10000, "2:15"), ("50:00", 10000, "2:30")]), TimedWorkout([("1:20:00", 21818, "1:50"), ("1:40:00", 26087, "1:55"), ("2:00:00", 30000, "2:00")], True)])
sd.printAllWorkouts()
sd.findBestWorkoutType()

