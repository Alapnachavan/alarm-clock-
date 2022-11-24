# # import datetime
# from playsound import playsound
# playsound()
# print('playing sound using playsound')




# import required module
import datetime
from playsound import playsound

# for playing note.wav file
# playsound('/home/alpana/Downloads/alarm')
Alarmhour=int(input("Enter hour: "))
Alarmmin=int(input("Enter the min: "))
AlarmAm=input("am/pm: ")

if AlarmAm=="pm":
    Alarmhour+=12
# elif AlarmAm=="am":
    # Alarmhour-=12

while True:
    if Alarmhour==datetime.datetime.now().hour and Alarmmin==datetime.datetime.now().minute:
        print('GOOD MORNING!!!!! WAKE UP WAKE UP.....')
        print("playing....")
        playsound('/home/alpana/Downloads/alpana ringtone')
        # print('playing sound using playsound')
        break


import datetime
from playsound import playsound

# for playing note.wav file
# playsound('/home/alpana/Downloads/alarm')
Alarmhour=int(input("Enter hour: "))
Alarmmin=int(input("Enter the min: "))
AlarmAm=input("am/pm: ")

if AlarmAm=="pm":
    Alarmhour+=12
# elif AlarmAm=="am":
    # Alarmhour-=12

while True:
    if Alarmhour==datetime.datetime.now().hour and Alarmmin==datetime.datetime.now().minute:
        print('GOOD MORNING!!!!! WAKE UP WAKE UP.....')
        print("playing....")
        playsound('/home/alpana/Downloads/alpana ringtone')
        # print('playing sound using playsound')
        break

