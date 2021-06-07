from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()

# DD/MM/YYYY format
d1 = today.strftime("%d/%m/%Y")
t1 = now.strftime("%H:%M:%S")

print("Date: ", d1)
print("Time: ", t1)