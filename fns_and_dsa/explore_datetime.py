import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()

    print('Current date and time:', current_date.strftime("%Y-%m-%d %H:%M:%S"))

    days_to_add = int(input('Enter the number of days to add to the current date: '))

    future_date = current_date + datetime.timedelta(days=days_to_add)

    return future_date.strftime("%Y-%m-%d")

future =display_current_datetime()
print('Future date:',future)