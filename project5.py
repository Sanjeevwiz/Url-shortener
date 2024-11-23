import tkinter as tk
from tkinter import messagebox
import requests

# Function to shorten the URL
def shorten_url():
    original_url = url_entry.get()
    if not original_url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    
    api_url = "https://api.tinyurl.com/create"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # Replace YOUR_API_KEY with TinyURL API key
    data = {"url": original_url}

    try:
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 201:
            shortened_url = response.json().get("data").get("tiny_url")
            result_label.config(text=f"Shortened URL: {shortened_url}", fg="green")
        else:
            result_label.config(text=f"Error: {response.json().get('errors')[0].get('message')}", fg="red")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

# GUI Setup
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")
root.resizable(False, False)

# Input Field
tk.Label(root, text="Enter URL to shorten:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)

# Shorten Button
shorten_button = tk.Button(root, text="Shorten URL", font=("Arial", 12), command=shorten_url)
shorten_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()

