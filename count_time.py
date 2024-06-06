from datetime import datetime
import time
time1 = input(("Number of minute to sent: "))
time2 = int(time1)

T1 = datetime.now()

while True:
    T2 = datetime.now()
    time_diff = T2-T1
    print(time_diff)
    time.sleep(1)
    if (time_diff.total_seconds()/60) > time2 :
       # strptime
        break;
