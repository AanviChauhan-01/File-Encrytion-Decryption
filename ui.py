import tkinter as tk
import subprocess

def run_script():
    subprocess.run(["python", "encryption_script.py"])

window = tk.Tk()
window.title("File Encryption Tool")
window.geometry("300x200")

title = tk.Label(window, text="File Encryption Tool", font=("Arial",14))
title.pack(pady=20)

run_button = tk.Button(window, text="Run Encryption Script", command=run_script)
run_button.pack(pady=20)

window.mainloop()
