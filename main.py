import time
from datetime import datetime, timedelta
import pygame

def playAudio():
    pygame.mixer.init()
    pygame.mixer.music.load("audioFiles/audio1.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.music.load("audioFiles/audio2.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.music.load("audioFiles/audio3.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.quit()
    

if __name__ == "__main__":
    # Get the current time
    now = datetime.now()

    # Define 8 AM on the current day
    eight_am = now.replace(hour=8, minute=0, second=0, microsecond=0)

    # If the current time is after 8 AM, set the next 8 AM to tomorrow
    if now > eight_am:
        eight_am += timedelta(days=1)

    # Calculate the time difference between now and 8 AM
    time_until_eight_am = (eight_am - now).total_seconds()

    # Convert time difference to hours and minutes
    hours = int(time_until_eight_am // 3600)
    minutes = int((time_until_eight_am % 3600) // 60)

    # Display the time until 8 AM
    print(f"Sleeping for {hours} hours and {minutes} minutes...")

    # Sleep until 8 AM
    time.sleep(time_until_eight_am)

    # Run the function foo()
    playAudio()