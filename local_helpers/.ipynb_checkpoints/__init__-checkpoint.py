morning_hours = [*range(6, 12)]
afternoon_hours = [*range(12, 18)]
evening = [*range(18, 23)]
night = [23] + [*range(0, 6)]

def get_pnt_day_with_pnt_week(dt):
    time_of_week = "week" if dt.weekday() < 5 else "weekend"
    hour = dt.hour

    if hour in morning_hours:
        return "morning_" + time_of_week
    elif hour in afternoon_hours:
        return "afternoon_" + time_of_week
    elif hour in evening:
        return "evening_" + time_of_week
    elif hour in night:
        return "night_" + time_of_week