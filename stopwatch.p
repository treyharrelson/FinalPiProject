
timer = StringVar()
Label(root, textvariable=timer, width = 8,  font = 'Helvetica 14').place(x=420, y=120)
timer.set('00:00.00')

# Define the function for the timer
def stop_watch():
    start_time = time.time()
    running = True
    while running:
        elapsed_time = time.time() - start_time
        minute, second = (elapsed_time // 60, elapsed_time % 60)
        second = round(second, 2)
        minute =  int(minute)
        timer.set(f"{minute}:{second}")

        # update the time
        root.update()
        time.sleep(.01)


