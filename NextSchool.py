import tkinter as tk
from tkinter import colorchooser, ttk
import webview

class NextSchoolApp:
    def __init__(self, master):
        self.master = master
        self.master.title("NextSchool")
        self.master.attributes('-fullscreen', True) 
        self.master.configure(bg="#e1ecf4")  

        style = ttk.Style()
        style.configure(
            "TButton",
            padding=10,
            font=("Helvetica", 16),
            background="white", 
            foreground="black",   
            relief="flat"
        )
        style.map("TButton", background=[("active", "#f0f0f0")],  
                  foreground=[("active", "black")]) 

        self.main_frame = tk.Frame(master, bg="#e1ecf4", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')

        self.welcome_label = tk.Label(
            self.main_frame,
            text="Καλώς ήρθατε στην εφαρμογή NextSchool!",
            font=("Helvetica", 28, "bold"),
            bg="#e1ecf4",
            fg="#007acc"
        )
        self.welcome_label.pack(pady=(20, 10))

        self.description_label = tk.Label(
            self.main_frame,
            text="Η εφαρμογή NextSchool σας προσφέρει εύκολη πρόσβαση σε διαδραστικά σχολικά βιβλία, "
                 "την πλατφόρμα eClass και το εκπαιδευτικό περιεχόμενο του Φωτόδεντρου.",
            font=("Helvetica", 18),
            bg="#e1ecf4",
            fg="#4a4a4a",
            wraplength=800
        )
        self.description_label.pack(pady=(10, 20))

        self.eclass_button = ttk.Button(
            self.main_frame,
            text="eClass",
            style="TButton",
            command=lambda: self.open_webview('eClass', 'https://eclass.sch.gr/')
        )
        self.eclass_button.pack(pady=(5, 10))

        self.ebooks_button = ttk.Button(
            self.main_frame,
            text="Διαδραστικά Βιβλία",
            style="TButton",
            command=lambda: self.open_webview('Διαδραστικά Βιβλία', 'http://ebooks.edu.gr/ebooks/')
        )
        self.ebooks_button.pack(pady=(5, 10))

        self.photodentro_button = ttk.Button(
            self.main_frame,
            text="Φωτόδεντρο",
            style="TButton",
            command=lambda: self.open_webview('Φωτόδεντρο', 'https://photodentro.edu.gr/')
        )
        self.photodentro_button.pack(pady=(5, 10))

        self.whiteboard_button = ttk.Button(
            self.main_frame,
            text="Whiteboard",
            style="TButton",
            command=self.open_whiteboard
        )
        self.whiteboard_button.pack(pady=(5, 20))

        self.exit_button = ttk.Button(
            self.main_frame,
            text="Έξοδος",
            style="TButton",
            command=self.exit_fullscreen
        )
        self.exit_button.pack(pady=20)

        self.footer_label = tk.Label(
            self.main_frame,
            text="Η εφαρμογή δημιουργήθηκε για εκπαιδευτικούς σκοπούς. "
                 "Τα δικαιώματα των πλατφόρμων ανήκουν στο ΠΣΔ. Τhis application was created by Andreas Agouridis",
            font=("Helvetica", 12),
            bg="#e1ecf4",
            fg="#4a4a4a"
        )
        self.footer_label.pack(side=tk.BOTTOM, pady=(10, 0))

        self.webview_window = None 

    def open_webview(self, title, url):

        if self.webview_window:
            self.webview_window.destroy()
        
        self.webview_window = webview.create_window(title, url, width=1024, height=768)
        webview.start()

    def open_whiteboard(self):
        whiteboard = tk.Toplevel(self.master)
        whiteboard.title("Whiteboard")
        whiteboard.geometry("800x600")
        whiteboard.configure(bg="white")

        self.canvas = tk.Canvas(whiteboard, bg="white", width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        self.line_color = "black"

        color_button = tk.Button(whiteboard, text="Επιλογή Χρώματος", command=self.choose_color, bg="#007acc", fg="white", font=("Helvetica", 12, "bold"))
        color_button.pack(pady=10)

        clear_button = tk.Button(whiteboard, text="Καθαρισμός", command=self.clear_canvas, bg="#e33e3e", fg="white", font=("Helvetica", 12, "bold"))
        clear_button.pack(pady=10)

        self.canvas.bind("<B1-Motion>", self.paint)  

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.line_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_line(x1, y1, x2, y2, fill=self.line_color, width=3)

    def exit_fullscreen(self):
        if self.webview_window:
            self.webview_window.destroy()
            self.webview_window = None

        self.master.attributes('-fullscreen', False)  
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NextSchoolApp(root)
    root.mainloop()
