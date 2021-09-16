import datetime


def get_hour(time_seconds):
    time_string = str(time_seconds)
    if "." in str(time_seconds):
        find_dot = time_string.find('.')
        rm_char_after_dot = time_string[:int(find_dot)]
        return int(rm_char_after_dot)


def seconds_to_hour(time_received):
    final_time = str(datetime.timedelta(seconds=get_hour(time_received)))
    if final_time.startswith("0"):
        return "approx. " + str(datetime.timedelta(seconds=get_hour(time_received))) + " minutes"
    else:
        return "approx. " + str(datetime.timedelta(seconds=get_hour(time_received))) + " hours"


def convert(time):
    pos = ['s', 'm', 'h', 'd']
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]
