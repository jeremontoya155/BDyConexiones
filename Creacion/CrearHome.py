import os
import customtkinter as ctk
from tkinter import messagebox

# Lista de nombres de carpetas
carpetas = [
    "Sanchez Antoniolli 1",
    "Sanchez Antoniolli II",    
    "Sanchez Antoniolli III",
    "Sanchez Antoniolli IV",
    "Sanchez Antoniolli V",
    "Sanchez Antoniolli VI",
    "Sanchez Antoniolli VII",
    "Sanchez Antoniolli VIII",
    "Sanchez Antoniolli IX",
    "Sanchez Antoniolli X",
    "Sanchez Anoniolli XI",
    "Sanchez Antoniolli XII",
    "Sanchez Antoniolli XIV",
    "Sanchez Antoniolli XV",
    "Sanchez Antoniolli XVI",
    "Sanchez Antoniolli XVII",
    "SANCHEZ ANTONIOLLI XVIII",
    "Sanchez Antoniolli XIX",
    "Sanchez Antoniolli XX",
    "Sanchez Antoniolli XXI",
    "Sanchez Antoniolli 23",
    "SANCHEZ ANTONIOLLI 24",
    "Sanchez Antoniolli 25",
    "Sanchez Antoniolli 26",
    "Sanchez Carestia"
]

def check_folders():
    desktop_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    resultados_dir = os.path.join(desktop_dir, "resultados")
    
    all_exist = all(os.path.exists(os.path.join(resultados_dir, carpeta)) for carpeta in carpetas)
    if all_exist:
        create_button.configure(state="disabled", text="Carpetas ya existen", fg_color="red")
    else:
        create_button.configure(state="normal", text="Crear Carpetas", fg_color="green")

def create_folders():
    desktop_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    resultados_dir = os.path.join(desktop_dir, "resultados")
    if not os.path.exists(resultados_dir):
        os.makedirs(resultados_dir)
    
    already_exists = []
    for carpeta in carpetas:
        carpeta_path = os.path.join(resultados_dir, carpeta)
        if not os.path.exists(carpeta_path):
            os.makedirs(carpeta_path)
        else:
            already_exists.append(carpeta)
    
    if already_exists:
        messagebox.showwarning("Advertencia", f"Las siguientes carpetas ya existen: {', '.join(already_exists)}")
    else:
        messagebox.showinfo("Éxito", "Todas las carpetas han sido creadas.")
    
    check_folders()

def main():
    global create_button
    
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    root.title("Creador de Carpetas")
    root.geometry("400x200")
    root.resizable(False, False)

    label = ctk.CTkLabel(root, text="Pulse el botón para crear las carpetas", font=("Helvetica", 14))
    label.pack(pady=20)

    create_button = ctk.CTkButton(root, text="Crear Carpetas", font=("Helvetica", 14), command=create_folders)
    create_button.pack(pady=20)
    
    check_folders()
    
    root.mainloop()

if __name__ == "__main__":
    main()
