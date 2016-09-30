import calendar
from datetime import datetime
from datetime import date

from googlecalendar import googlecalendar
#d = datetime(2016, 9, 27, 12+7, 46, 0)
#print (d.isoformat())

#d1 = datetime.now()
#print (d1.isoformat())
#c = d1.weekday()
#print (c)
#b = d1.replace(day=d1.day-c)
#print (b)
#print (d1)

class parse:

    def __init__ (self):
        now = datetime.now()
        #now = datetime(2016, 10, 7,12+7, 46, 0)
        weekday = now.weekday()
        self.dictionary = {}
        self.dictionary ["M"] = now.replace(day=now.day-weekday)
        self.dictionary ["T"] = now.replace(day=now.day-weekday+1)
        self.dictionary ["W"] = now.replace(day=now.day-weekday+2)
        self.dictionary ["R"] = now.replace(day=now.day-weekday+3)
        self.dictionary ["F"] = now.replace(day=now.day-weekday+4)

        self.calendar = googlecalendar()
        self.calendar.get_credentials()
        
        #print (dictionary)
    
    def get_weekdays (self, string):
        arr = []
        for x in range (0, len(string)):
            if (string [x] == 'M'):
                arr.append (self.dictionary['M'])
            elif (string [x] == 'T'):
                arr.append (self.dictionary['T'])
            elif (string [x] == 'W'):
                arr.append (self.dictionary['W'])
            elif (string [x] == 'R'):
                arr.append (self.dictionary['R'])
            elif (string [x] == 'F'):
                arr.append (self.dictionary['F'])
        return arr
    
    
    def split_string (self, string, character):
        index = string.find(character)
        start = string [0:index].strip()
        end = string [index+1:].strip()
        arr = []
        arr.append (start)
        arr.append (end)
        return arr
    
    def get_hour (self, string):
        # Can only take in one time
        time = self.split_string (string.strip(), " ")
        # time[1] is AM or PM
        # time[0] is the rest of the string
        hour_and_minute = self.split_string (time[0], ":")
        
        if (time[1].lower() == "pm"):
            return 12 + int (hour_and_minute[0])
        return int (hour_and_minute[0])
    
    
    def get_minute (self, string):
        time = self.split_string (string.strip(), " ")
        # time[1] is AM or PM
        # time[0] is the rest of the string
        hour_and_minute = self.split_string (time[0], ":")
        return int(hour_and_minute[1])
    
    def place_row_into_calendar (self, array):
        # array[0] is description
        # array[1] is time
        # array[2] is days of the week
        # array[3] is location

        start_and_end = self.split_string (array[1], "-")
        # start_and_end[0] is start
        # start_and_end[1] is end

        location = self.split_string (array[3], ":")
        # location [1] is the actual location
        
        days_of_week = self.get_weekdays(array[2])
        for day in days_of_week:
            start_day = day.replace(hour=self.get_hour(start_and_end[0]),minute=self.get_minute(start_and_end[0]),second=0,microsecond=0)
            end_day = day.replace(hour=self.get_hour(start_and_end[1]),minute=self.get_minute(start_and_end[1]),second=0,microsecond=0)
            self.calendar.add_event_ten_weeks(start_day.isoformat(), end_day.isoformat(), array[0], location[1])
            print ("added event between "+ start_day.isoformat() + " and " +end_day.isoformat())

    
    def place_array_in_calendar (self, array):
        for row in array:
            print ("placing new event")
            self.place_row_into_calendar (row)
    
#a = parse()

#testarray = [['C LIT    30 A - MAF WORKS-EUROP LIT', '10:00 AM-10:50 AM', 'T R', 'Location:Chemistry Building, Room 1179']]
#a.place_array_in_calendar (testarray)
#print (split_string ("   10 : 00 AM - 5 : 00 PM     ", "-"))
#print (a.get_hour ("  09:22 PM  "))
#print (a.get_minute ("   10:30 AM "))
#print (get_weekdays ("     T   W   F  "))

    
