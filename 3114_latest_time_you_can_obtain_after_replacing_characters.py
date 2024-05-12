def findLatestTime(s: str) -> str:
    '''Фух =))'''
    hour, minutes = s.split(':')
    if hour.isdigit():
        pass
    elif hour == '??' and minutes.count('?') == 2:
        hour, minutes = '11', '59'
    elif hour == '??' and minutes.count('?') == 1:
        hour = '11'
    elif hour == '??' and int(minutes) > 0:
        hour = '11'
    elif hour == '??' and int(minutes) == 0:
        hour = '11'
    elif hour[0] == '0':
        hour = '09'
    elif hour[0] == '1' and minutes.count('?') == 2:
        hour, minutes = '11', '59'
    elif hour[0] == '1':
        hour = '11'
    elif hour[1] == '2' and minutes != '??':
        hour = '0' + hour[1]
    elif hour[1] < '2':
        hour = '1' + hour[1]
    else:
        hour = '0' + hour[1]

    if minutes.isdigit():
        pass
    elif minutes == '??' and int(hour) < 12:
        minutes = '59'
    elif minutes == '??' and int(hour) == 12:
        minutes = '00'
    elif minutes[0] == '?':
        minutes = '5' + minutes[1]
    else:
        minutes = minutes[0] + '9'

    return f'{hour}:{minutes}'
