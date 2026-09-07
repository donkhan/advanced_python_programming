import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("File Download Demo")
root.geometry("400x180")

TOTAL_SIZE = 100
downloaded = 0
running = False
job = None


def download_chunk():
    global downloaded, running, job
    if not running:
        return
    downloaded += 2        # Download 2%
    progress["value"] = downloaded
    lbl.config(text=f"Downloaded {downloaded}%")
    if downloaded >= TOTAL_SIZE:
        lbl.config(text="Download Complete")
        running = False
        return
    time.sleep(0.05)
    job = root.after(1, download_chunk)


def download_chunk_hog_event_loop():
    global downloaded

    while downloaded < TOTAL_SIZE:
        downloaded += 1
        time.sleep(0.05)
        progress["value"] = downloaded
        lbl.config(text=f"Downloaded {downloaded}%")
    lbl.config(text="Download Complete")


def start_download():
    global downloaded, running
    if running:
        return
    downloaded = 0
    running = True
    progress["value"] = 0
    lbl.config(text="Starting Download...")
    # download_chunk()
    download_chunk_hog_event_loop()


def stop_download():
    global running
    running = False
    if job:
        root.after_cancel(job)
    lbl.config(text="Download Stopped")


progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate",
    maximum=100
)
progress.pack(pady=20)

lbl = tk.Label(root, text="Ready")
lbl.pack()
tk.Button(root, text="Start", command=start_download).pack(side="left", padx=40, pady=20)
tk.Button(root, text="Stop", command=stop_download).pack(side="right", padx=40, pady=20)
root.mainloop()