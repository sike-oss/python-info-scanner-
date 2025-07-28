import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr_gui():
    name = entry_name.get()
    age = entry_age.get()
    city = entry_city.get()
    mobile = entry_mobile.get()
    aadhaar = entry_aadhaar.get()
    address = entry_address.get()

    if not all([name, age, city, mobile, aadhaar, address]):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    user_data = (
        f"👤 Name: {name}\n"
        f"🎂 Age: {age}\n"
        f"🏙️ City: {city}\n"
        f"📱 Mobile: {mobile}\n"
        f"🆔 Aadhaar no: {aadhaar}\n"
        f"🏠 Address: {address}"
    )

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"{name}_QR.png"
    img.save(filename)

    # Show QR code in GUI
    img_pil = Image.open(filename)
    img_pil = img_pil.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_pil)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    messagebox.showinfo("Success", f"QR Code saved as {filename}\nScan with your phone camera to see the details.")

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.configure(bg="#f5f5dc")  # Beige background

fields = [
    ("Name", "entry_name"),
    ("Age", "entry_age"),
    ("City", "entry_city"),
    ("Mobile", "entry_mobile"),
    ("Aadhaar", "entry_aadhaar"),
    ("Address", "entry_address"),
]

entries = {}
for idx, (label_text, var_name) in enumerate(fields):
    label = tk.Label(root, text=label_text, bg="#f5f5dc")
    label.grid(row=idx, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(root, width=30, bg="white")
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries[var_name] = entry

entry_name = entries["entry_name"]
entry_age = entries["entry_age"]
entry_city = entries["entry_city"]
entry_mobile = entries["entry_mobile"]
entry_aadhaar = entries["entry_aadhaar"]
entry_address = entries["entry_address"]

generate_btn = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr_gui,
    bg="cyan",
    activebackground="#00e5ee"
)
generate_btn.grid(row=len(fields), column=0, columnspan=2, pady=10)

qr_label = tk.Label(root, bg="#f5f5dc")
qr_label.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

root.mainloop()
