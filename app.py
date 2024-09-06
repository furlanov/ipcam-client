from PIL import Image, ImageTk
from dotenv import load_dotenv
from io import BytesIO
import tkinter as tk
import requests
import os

load_dotenv()
url = os.getenv("url")
username = os.getenv("username")
password = os.getenv("password")

window = tk.Tk()
window.title("SCam")
window.geometry("320x170")
window.resizable(True, True)

image_label = tk.Label(window)
image_label.pack(fill=tk.BOTH, expand=True)

def update_camera_feed():
    try:
        response = requests.get(url, auth=(username, password), stream=True)
        response.raise_for_status()
        
        image = Image.open(BytesIO(response.content))
        
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        resized_image = image.resize((window_width, window_height))
        
        tk_image = ImageTk.PhotoImage(resized_image)
        
        image_label.config(image=tk_image)
        image_label.image = tk_image
    except Exception as e:
        print("Error:", e)
    
    window.after(500, update_camera_feed)

update_camera_feed()

window.mainloop()
