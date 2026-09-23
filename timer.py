import time
import winsound

def get_time():
    t = int(input("Enter the number of seconds to wait: "))
    return t

def timer(t):
    for x in (range(t,0,-1)):
        secs = x % 60
        mins = int(x / 60) % 60
        hrs = int(x / 3600)
        print(f"{hrs:02}:{mins:02}:{secs:02}")
        time.sleep(1) # Wait for 1 second
    print("TIME'S UP!")
    winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)  # Play alarm sound

def main():
    t = get_time()
    timer(t)

main()