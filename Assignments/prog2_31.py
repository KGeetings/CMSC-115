timeSeconds = input("Enter a number between 1 and 86,400: ")

timeSecondsInt = int(timeSeconds)

hours = timeSecondsInt // 3600

minutes = (timeSecondsInt - (hours * 3600)) // 60

seconds = (timeSecondsInt) - (hours * 3600) - (minutes * 60)

print(timeSecondsInt, "is", hours, "hours,", minutes, "minutes, and", seconds, "seconds")
