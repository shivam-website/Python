from datetime import datetime

now = datetime.now()
print("Current time:", now)
print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))
