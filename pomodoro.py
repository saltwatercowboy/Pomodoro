import time
import os

def pomodoro():
        count = 0
        if 0 != 1:
                while True:
                        os.system("say time to work")
                        print('Pomodoro work time!')
                        time.sleep(1500) 
                        count +=1
                        
                        if count % 3:
                                os.system("say 5 minute break")
                                print('Pomodoro 5 minute break!')
                                time.sleep(300) 
                                
                        else:
                                os.system("say 15 minute break")
                                print('Pomodoro chill time!')
                                time.sleep(900)                         
                
            
pomodoro()
