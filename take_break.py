# Take a break every 2 hours
# Repeat 3 times
# Steps
# 1. wait 2 hours
# 2. open browser
# 3. run the link
import webbrowser
import time

totak_break = 3
break_count = 0
print("Current Time "+time.ctime())
while(break_count < totak_break):
    time.sleep(7200) # seconds
    webbrowser.open("https://www.youtube.com/watch?v=L1KHzzDs9vk&t=1006s")
    break_count = break_count + 1