from tkinter import *
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

#functions
def convert_video_to_audio(video_file_path, audio_file_path):
    try:
        video_clip = VideoFileClip(video_file_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_file_path)
        audio_clip.close()
        video_clip.close()
        messagebox.showinfo("Success", f"Audio extracted and saved to {audio_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_video_file():
    video_file_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4;*.avi;*.mkv;*.mov")]
    )
    if video_file_path:
        video_file_entry.delete(0, END)
        video_file_entry.insert(0, video_file_path)

def save_audio_file():
    audio_file_path = filedialog.asksaveasfilename(
        title="Save Audio File",
        defaultextension=".mp3",
        filetypes=[("Audio Files", "*.mp3;*.wav;*.flac;*.aac")]
    )
    if audio_file_path:
        audio_file_entry.delete(0, END)
        audio_file_entry.insert(0, audio_file_path)

def start_conversion():
    video_file_path = video_file_entry.get()
    audio_file_path = audio_file_entry.get()
    if video_file_path and audio_file_path:
        convert_video_to_audio(video_file_path, audio_file_path)
    else:
        messagebox.showwarning("Input Required", "Please select both video and audio file paths.")

# Create the main application window
root = Tk()
root.title("Video to Audio Converter")
root.configure(bg="light pink")

#icon
root.iconbitmap("music.ico")


# Create and place widgets
video_file_label = Label(root,bg="light pink", text="Video File:")
video_file_label.grid(row=0, column=0, padx=10, pady=10)

video_file_entry = Entry(root, width=50)
video_file_entry.grid(row=0, column=1, padx=10, pady=10)

video_file_button = Button(root, text="Browse", command=select_video_file)
video_file_button.grid(row=0, column=2, padx=10, pady=10)

audio_file_label = Label(root,bg="light pink", text="Audio File:")
audio_file_label.grid(row=1, column=0, padx=10, pady=10)

audio_file_entry = Entry(root, width=50)
audio_file_entry.grid(row=1, column=1, padx=10, pady=10)

audio_file_button = Button(root, text="Save As", command=save_audio_file)
audio_file_button.grid(row=1, column=2, padx=10, pady=10)

convert_button = Button(root, text="Convert", command=start_conversion)
convert_button.grid(row=2, column=0, columnspan=3, pady=20)

# Start the Tkinter event loop
root.mainloop()