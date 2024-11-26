import random
import time
def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and" ,endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print("Random date = ", getRandomDate("31/1/2024", "1/8/2024"))
