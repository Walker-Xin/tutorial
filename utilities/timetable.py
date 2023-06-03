import pandas as pd
from ics import Event, Calendar, DisplayAlarm
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import sys, os
import requests


def get_timetable(url):
    r = requests.get(url)

    # extract the table as text and replace <br /> with \n
    table = r.content.replace(b'<br />', b'\\n')
    timetable = pd.read_html(table)[0]

    return timetable


c = Calendar() # Calendar
length = timedelta(hours = 1)

# if len(sys.argv) >= 2:
#     path = sys.argv[1]
# else:
#     path = str(input('Key in the path of timetable file:'))
#     assert os.path.isfile(path)

timetable = get_timetable('https://www3.physics.ox.ac.uk/lectures/timetableprint.aspx?term=Trinity&year=2023&course=1physics')

date = input('Key in the date of Monday of 1st week of the term (DD/MM/YYYY):') # Initial day input
date = date.split('/')
date_i = datetime(int(date[2]), int(date[1]), int(date[0]), 9, 0, tzinfo=ZoneInfo("Europe/London"))

answer = input('Should alarms be included? (Y/n)') or 'Y'

if answer == 'Y' or 'y':
    alarm_switch = True
elif answer == 'N' or 'n':
    alarm_switch = False
else:
    raise Exception('Please provide a valid input!')

prac_date = input('Are the practicals on Thursday or Friday? (THURS/Fri/No)') or 'Thurs'

if prac_date.lower() not in ['thurs', 'fri', 'no']:
    raise Exception('Please provide a valid input!')

for i in range(len(list(timetable.columns))):
    timetable.loc[timetable[i].str.contains('Practicals', na=False), i] = 'nan'

lines = timetable.shape[0]
events = []
for i in range(1, lines-1):
    date = date_i + timedelta(days = divmod(i-6, 5)[0]*7 + divmod(i-6, 5)[1])
    row = timetable.iloc[i]
    for k in [2, 3, 4, 5]:
        e = Event()

        if str(row[k]) != 'nan':
            name = str(row[k])
            time = timedelta(hours=(k-2))

            e.name = name
            e.begin = date + time
            e.duration = length
            
            if alarm_switch:
                if k == 2:
                    e.alarms = [DisplayAlarm(trigger=timedelta(minutes=-15))]
                else:
                    e.alarms = [DisplayAlarm(trigger=timedelta(minutes=0))]
            else:
                pass

            if len(events) == 0:
                events.append(e)
            else:
                prev = events[-1]
                if e.name == prev.name and str(e.begin)[:10] == str(prev.begin)[:10]:
                    prev.duration += length
                else:
                    events.append(e)
        else:
            pass

    afternoon = row[6]

    if str(afternoon) != 'None' and str(afternoon) != 'nan':
        for item in (row[6]).split('\\n'):
            e = Event()
            result = item.split(' ', 3)
            delta_begin = datetime.strptime(result[0], '%H.%M')
            delta_end = datetime.strptime(result[2], '%H.%M')
            begin = date + timedelta(hours=delta_begin.hour-9, minutes=delta_begin.minute)
            end = date + timedelta(hours=delta_end.hour-9, minutes=delta_end.minute)
            name = result[-1]

            e.name = name
            e.begin = begin
            e.end = end
            if alarm_switch:
                e.alarms = [DisplayAlarm(trigger=timedelta(minutes=-15))]
            else:
                pass
            events.append(e)
    else:
        pass

if prac_date == 'Thurs':
    dates = [date_i + timedelta(hours=1, days=3 + 7*i) for i in range(8)]
    for date in dates:
        e = Event()
        e.name = 'Practical'
        e.begin = date
        e.duration = timedelta(hours=7)
        if alarm_switch:
            e.alarms = [DisplayAlarm(trigger=timedelta(minutes=-15))]
        else:
            pass
        events.append(e)
elif prac_date == 'Fri':
    dates = [date_i + timedelta(hours=1, days=4 + 7*i) for i in range(8)]
    for date in dates:
        e = Event()
        e.name = 'Practical'
        e.begin = date
        e.duration = timedelta(hours=7)
        if alarm_switch:
            e.alarms = [DisplayAlarm(trigger=timedelta(minutes=-15))]
        else:
            pass
        events.append(e)
else:
    pass

for event in events:
    c.events.add(event)

with open('my.ics', 'w') as f:
    f.write(str(c))
