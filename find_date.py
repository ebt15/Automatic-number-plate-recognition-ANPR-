from datetime import date, datetime


# Function to find the date and time
def date_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = date.today()
    return current_date, current_time
