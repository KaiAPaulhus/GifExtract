import queue


def addToQueue(screen):
    string = queue.convertToVideoString(screen)
    if string is not None:
        result = screen.queue.addItem(string)
        if not result:
            #TODO: Properly handle error.
            print("Error adding to queue. Non-unique description")
        screen.queue.listJobs()


def executeQueueItem(screen):
    curritem = screen.tab_queue.ui.tree_queue.currentItem()
    print("curritem:", curritem)
    if curritem is not None:
        text = curritem.text(0)
        print(text)
        job = screen.queue.getJobByDescription(text)
        if job is not None:
            screen.ffmpeg.extractFrames(job)


def executeAllQueue(screen):
    for item in screen.queue.getJobs():
        screen.ffmpeg.extractFrames(item)