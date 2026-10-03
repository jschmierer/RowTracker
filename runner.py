from timedworkout import TimedWorkout
from distancedworkout import DistancedWorkout
from statsdash import StatsDash
from user import User

user = User("jschmierer", "password10", 17, "Jakob Schmierer")

#user.sd.addWorkout()
#user.sd.printAllWorkouts()

sd = StatsDash([TimedWorkout([("15:00", 4000, "1:40")]), DistancedWorkout([("45:00", 10000, "2:15"), ("50:00", 10000, "2:30")]), TimedWorkout([("15:00", 4300, "1:44.7")]),  TimedWorkout([("1:20:00", 21818, "1:50"), ("1:40:00", 26087, "1:55"), ("2:00:00", 30000, "2:00")], True), TimedWorkout([("15:00", 4700, "1:35.7")])])
#sd.addWorkout()
sd.printAllWorkouts()
sd.findBestWorkout()
