import queue


def addToQueue(screen):
    string = queue.convertToString(screen)
    if string is not None:
        result = screen.queue.addItem(string)
        if not result:
            #TODO: Properly handle error.
            print("Error adding to queue. Non-unique description")
        screen.queue.listJobs()


def executeQueueItem(screen):
    curritem = screen.ui.tree_queue.currentItem()
    if curritem is not None:
        text = curritem.text(1)
        job = screen.queue.getJobByDescription(text)
        if job is not None:
            screen.ffmpeg.extractFrames(job)


def executeAllQueue(screen):
    for item in screen.queue.getJobs():
        screen.ffmpeg.extractFrames(item)