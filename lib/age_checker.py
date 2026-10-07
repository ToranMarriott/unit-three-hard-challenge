import datetime

def check_age(date):
    if date == "":
        raise Exception("No date of birth inputted")
    format = "%Y-%m-%d"
    try:
        bool(datetime.datetime.strptime(date, "%Y-%m-%d"))
    except:
        raise Exception("Date of birth incorrectly formatted (YYYY-MM-DD)")
    age = get_age(date)
    if age > 15:
        return "Access Granted!"
    else:
        return f"Access Denied, You are {age}, Access is restricted for under 16s!"

def get_age(date):
    today = datetime.date.today()
    age_in_days = (today - datetime.date.fromisoformat(date)).days
    age = age_in_days // 365.2425
    return int(age)
