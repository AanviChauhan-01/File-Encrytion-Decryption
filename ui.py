import tkinter as tk
from tkinter import messagebox
import encryptdecrypt as enc

def encrypt():
    key = enc.generate_key()
    enc.save_key(key)
    enc.encrypt_file("my_file.txt", key)
    messagebox.showinfo("Success", "File Encrypted!")

def decrypt():
    key = enc.load_key()
    enc.decrypt_file("my_file.txt.enc", key)
    messagebox.showinfo("Success", "File Decrypted!")

window = tk.Tk()
window.title("File Encryption Tool")
window.geometry("300x200")

title = tk.Label(window, text="File Encryption Tool", font=("Arial",14))
title.pack(pady=10)

encrypt_btn = tk.Button(window, text="Encrypt File", command=encrypt)
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(window, text="Decrypt File", command=decrypt)
decrypt_btn.pack(pady=10)

window.mainloop()
