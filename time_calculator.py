def add_time(start, duration, starting_day=None):
    # Days of the week array for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Splitting the start time and converting to 24-hour format
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    if period == "PM":
        start_hour += 12

    # Splitting the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Adding duration to start time
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    # Adjusting minutes and hours
    if end_minute >= 60:
        end_hour += end_minute // 60
        end_minute %= 60
    days_passed = end_hour // 24
    end_hour %= 24

    # Converting back to 12-hour format
    period = "AM" if end_hour < 12 else "PM"
    end_hour = end_hour if 1 <= end_hour <= 12 else end_hour - 12 if end_hour > 12 else 12

    # Formatting the new time
    new_time = f"{end_hour}:{end_minute:02d} {period}"

    # Determining the day of the week, if necessary
    if starting_day:
        day_index = (days_of_week.index(starting_day.capitalize()) + days_passed) % 7
        new_time += f", {days_of_week[day_index]}"

    # Adding information about the number of days passed
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
