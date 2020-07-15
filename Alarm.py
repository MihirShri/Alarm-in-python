"""
Author @ Mihir_Srivastava
Dated - 17-05-2020
File - Alarm
Aim - To make a beep sound of an alarm after the desired amount of time.
"""


# import necessary libraries
import time
# for producing sound
import winsound


# define a function for alarm
def alarm():
    try:
        # Input time from the user
        myTime = list(map(int, input("Enter time in hh mm ss format: ").split()))

        # If format is correct
        if len(myTime) == 3:
            # Convert the time entered in hh mm ss format to seconds
            total_seconds = myTime[0] * 60 * 60 + myTime[1] * 60 + myTime[2]

            # Nothing will happen for the input number of seconds
            time.sleep(total_seconds)

            # Give the frequency of your alarm
            frequency = 3500

            # Give the duration of your alarm
            duration = 2000

            # The function which produces beep sound of given frequency and duration
            winsound.Beep(frequency, duration)

        # If format is incorrect
        else:
            print("Enter time in correct format!!!")
            alarm()
    except Exception as e:
        print("This is an exception\n", e, "Please enter correct details!!!")
        alarm()


alarm()
