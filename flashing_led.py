import RPi.GPIO as GPIO
from time import sleep
"""
Small GPIO programm to flash a LED on a breadboard; the user has to choose HOW MANY BLINKS and for HOW LONG (secondes).

Petit programme GPIO faisant clignoter un DEL sur une platine d'experimentation (breadboard). L'utilisateur doit choisir
LE NOMBRE DE CLIGNOTIS et LA DUREE (secondes).
"""
def main():
    #GPIO Settings
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    #Main programm
    looping = True
    while looping == True:
        nbr_blinks = get_int("How many blinks")
        sleep_between_blinks = get_float("How long the sleep between the blinks")

        for i in range(1, nbr_blinks):
            GPIO.output(11, 1)
            sleep(sleep_between_blinks)
            GPIO.output(11, 0)
            sleep(sleep_between_blinks)

        looping = int(input("Do you want to continue (1 = Yes, 0 == No)"))

    #Cleaning up GPIO
    GPIO.cleanup()

def get_int(question):
    While True:
        try:
            return int(input(question))
        except ValueError:
            print("Please enter an integer")

def get_flaot(question):
    while True:
        try:
            return float(question))
        except ValuError:
            print("Please enter a number")

main()





