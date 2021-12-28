import time
import subprocess

# this project requires a virtual evironment
# to create a virtual environment: python3 -m venv alarm-clock
# to use the virtual env: source alarm-clock/bin/activate
# to install a module: pip install modulename

alarm_time = input("Alarm Timr>>> ")
sound = "alarm_sound.wav"
repitions = 4

while True:
    date = time.ctime()
    current_time = date[11:16]

    if current_time == alarm_time:

        for i in range(repitions):
            print(i)
            print("---")
            print("first")
            subprocess.call(["afplay", sound])
            time.sleep(5)
            print("second")
            subprocess.call(["afplay", sound])
        break    
