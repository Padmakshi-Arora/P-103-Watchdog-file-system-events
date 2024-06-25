import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/HP/Downloads"

#event handler class

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Hmm, {event.src_path} has been modified!")

    def on_moved(self, event):
        print(f"Uh oh! {event.src_path} has been moved somewhere else!")

#initialize event handler class
event_handler = FileEventHandler()

#initialize observer
observer = Observer()

#schedule the observer
observer.schedule(event_handler, from_dir, recursive=True)

#start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()


