import pywhatkit
import random

def sender(number,message):
    pywhatkit.sendwhatmsg_instantly(number,
                                    message,
                                    wait_time=15+random.randint(1,4),
                                    tab_close=True,
                                    close_time=2+random.randint(1,3))
