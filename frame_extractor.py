import cv2
import tkinter as tk
from tkinter import filedialog
import random
import os


def select_file():
    global video_path
    video_path = filedialog.askopenfilename(title="Seleziona il file video", filetypes=[("Video files", "*.mp4")])
    file_label.config(text=video_path)


def select_folder():
    global save_path
    save_path = filedialog.askdirectory(title="Seleziona la cartella di destinazione")
    folder_label.config(text=save_path)


def process_video(num_frames):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if not num_frames or num_frames > frame_count:
        num_frames = frame_count

    frame_files = [f for f in os.listdir(save_path) if f.startswith("frame_") and f.endswith(".jpg")]
    existing_frame_numbers = [int(f.split("_")[1].split(".")[0]) for f in frame_files]

    if existing_frame_numbers:
        frame_counter = max(existing_frame_numbers) + 1
    else:
        frame_counter = 1

    selected_frames = random.sample(range(1, frame_count + 1), num_frames)
    selected_frames.sort()

    for i in selected_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i - 1)
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = save_path + "/frame_" + str(frame_counter) + ".jpg"
        cv2.imwrite(frame_name, frame)
        frame_counter += 1

    cap.release()
    cv2.destroyAllWindows()
    result_label.config(text=f"Estrazione di {num_frames} frame completata!")


def extract_frames():
    num_frames = num_frames_entry.get()
    if not num_frames.isdigit():
        num_frames = None
    else:
        num_frames = int(num_frames)
    process_video(num_frames)


# Creazione della GUI
root = tk.Tk()
root.title("Estrai Frame da Video")

# Pulsanti e etichette
file_label = tk.Label(root, text="Seleziona il file video:")
file_label.pack()

file_button = tk.Button(root, text="Scegli File", command=select_file)
file_button.pack()

folder_label = tk.Label(root, text="Seleziona la cartella di destinazione:")
folder_label.pack()

folder_button = tk.Button(root, text="Scegli Cartella", command=select_folder)
folder_button.pack()

num_frames_label = tk.Label(root, text="Numero di frame da estrarre (lascia vuoto per tutti):")
num_frames_label.pack()

num_frames_entry = tk.Entry(root)
num_frames_entry.pack()

extract_button = tk.Button(root, text="Estrai Frame", command=extract_frames)
extract_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
