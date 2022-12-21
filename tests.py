import time

import winsound
for i in range(5):
    winsound.Beep(500,250)
import winsound
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

from datetime import datetime, timedelta

now=datetime.now()
new=now+timedelta(seconds=5)
print(new)
print(new.time())
print(f'{new:%H:%M:%S}')

time.sleep(5)

winsound.Beep(500,100)
print(now,new)
if 1==1:
    winsound.Beep(500,2000)