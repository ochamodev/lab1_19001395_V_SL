
import calendar

def findDay(year, month, day):
    
    dayNumber = calendar.weekday(year, month, day)
     
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
     
    return days[dayNumber]