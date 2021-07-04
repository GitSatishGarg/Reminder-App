import time
from plyer import notification

if __name__ == "__main__":   

    titleinput = input("What title whould you want to be reminded of? ")
    messageinput = input("What message whould you want to be reminded of? ")
    frequency = int(input("How frequent would yo like to be reminded? "))

    while True :
        notification.notify(
            title = titleinput,
            message = messageinput,
        )
        
        time.sleep(frequency),
