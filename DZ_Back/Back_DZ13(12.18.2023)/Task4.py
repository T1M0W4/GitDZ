def format_time(hours, minutes=None, seconds=None):
    if minutes is None:
        minutes = 0
    if seconds is None:
        seconds = 0

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


print(format_time(5, 30, 45)) 
print(format_time(2, 15))      
print(format_time(10))