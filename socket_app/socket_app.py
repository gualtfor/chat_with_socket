import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import os
from dotenv import load_dotenv
from client import Client

load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
GREY = os.getenv('GREY')
MEDIUM_GREY = os.getenv('MEDIUM_GREY')
BLUE = os.getenv('BLUE')
WHITE = os.getenv(' WHITE')
FONT_FAMILY = os.getenv('FONT_FAMILY')
FONT_SIZE = os.getenv('FONT_SIZE')
BUTTON_SIZE = os.getenv('BUTTON_SIZE')
SMALL_FONT_SIZE = os.getenv('SMALL_FONT_SIZE')

class sandbox(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root.geometry("620x600")
        root.title("Messenger Client")
        self.tables = [ 'empleados', 'departamento', 'profesion', 'expediente', 'aviones', 'sedes' ]
        self.operations = [ 'Select', 'Insert', 'Update', 'Delete' ]
        root.resizable(True, True)
        
        # Create Canvas and Scrollbar
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Create a frame inside the canvas to hold widgets
        self.main_frame = ttk.Frame(self.canvas)
        self.client = Client()

        self.top_frame = tk.Frame(self.main_frame, width=600, height=100, bg=MEDIUM_GREY)
        self.top_frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        self.top_table = tk.Frame(self.main_frame, width=600, height=100, bg=GREY)
        self.top_table.grid(row=1, column=0, sticky=tk.NSEW)
        
        self.top_operation = tk.Frame(self.main_frame, width=600, height=100, bg=GREY)
        self.top_operation.grid(row=2, column=0, sticky=tk.NSEW)

        self.label_data = tk.Frame(self.main_frame, width=600, height=50, bg=GREY)
        self.label_data.grid(row=3, column=0, sticky=tk.NSEW)
        
        self.text_data = tk.Frame(self.main_frame, width=600, height=25, bg=MEDIUM_GREY)
        self.text_data.grid(row=4, column=0, sticky=tk.NSEW)
        
        self.label_condition = tk.Frame(self.main_frame, width=600, height=50, bg=GREY)
        self.label_condition.grid(row=5, column=0, sticky=tk.NSEW)
        
        self.text_condition = tk.Frame(self.main_frame, width=600, height=150, bg=MEDIUM_GREY)
        self.text_condition.grid(row=6, column=0, sticky=tk.NSEW)
        
        self.label_result = tk.Frame(self.main_frame, width=600, height=100, bg=GREY)
        self.label_result.grid(row=7, column=0, sticky=tk.NSEW)

        self.text_result = tk.Frame(self.main_frame, width=600, height=100, bg=MEDIUM_GREY)
        self.text_result.grid(row=8, column=0, sticky=tk.NSEW)
        
        self.bottom_frame = tk.Frame(self.main_frame, width=600, height=100, bg=GREY)
        self.bottom_frame.grid(row=9, column=0, sticky=tk.NSEW)

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)
        root.grid_rowconfigure(3, weight=1)
        root.grid_rowconfigure(4, weight=1)
        root.grid_rowconfigure(5, weight=1)
        root.grid_rowconfigure(6, weight=1)
        root.grid_rowconfigure(7, weight=1)
        root.grid_rowconfigure(8, weight=1)
        root.grid_rowconfigure(9, weight=1)
        
        # Place the canvas and scrollbar
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add the main frame to the canvas
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        
        self.populate_widgets()
        
        # Update scroll region dynamically
        self.main_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Pack the entire widget
        self.pack(fill=tk.BOTH, expand=True)
        
    def populate_widgets(self):
        self.username_label = tk.Label(self.top_frame, text="Ingrese su usuario:", font=(FONT_FAMILY, FONT_SIZE), bg=MEDIUM_GREY, fg=WHITE)
        self.username_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=3)

        self.username_textbox = tk.Entry(self.top_frame, font=(FONT_FAMILY, FONT_SIZE), bg=WHITE, fg=WHITE, width=23)
        self.username_textbox.grid(row=0, column=1, sticky="nsew", padx=3, pady=20)

        self.username_button = tk.Button(self.top_frame, text="Unirse", font=(FONT_FAMILY, BUTTON_SIZE), bg=BLUE, fg=WHITE, command=self.connect)
        self.username_button.grid(row=0, column=2, sticky="nsew", padx=5, pady=20)
        
        self.name_table = tk.Label(self.top_table, text="Seleccione la tabla:", font=(FONT_FAMILY, FONT_SIZE), bg=GREY, fg=WHITE)
        self.name_table.grid(row=1, column=0, sticky="nsew", padx=5, pady=20)
        
        self.list_tables = ttk.Combobox(self.top_table, values=self.tables, font=(FONT_FAMILY, FONT_SIZE), width=22)
        self.list_tables.grid(row=1, column=1, sticky="nsew", padx=5, pady=20)
        self.list_tables.set(self.tables[0])
        self.list_tables['state'] = 'readonly'
        
        self.name_operation = tk.Label(self.top_operation, text="Seleccione la operacion:", font=(FONT_FAMILY, FONT_SIZE), bg=GREY, fg=WHITE)
        self.name_operation.grid(row=2, column=0, sticky="nsew", padx=5, pady=20)
        
        self.selected_option = tk.StringVar(value="select")
        self.radiobuttons = []
        for index, option in enumerate(self.operations):
            radiobutton_option = ttk.Radiobutton(self.top_operation, text=option, value=option.lower(), variable=self.selected_option).grid(row=2, column=index+1, sticky="w", padx=5, pady=20)
            self.radiobuttons.append(radiobutton_option)

        self.enter_data = tk.Label(self.label_data, text="Ingrese los datos:", font=(FONT_FAMILY, FONT_SIZE), bg=GREY, fg=WHITE)
        self.enter_data.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        self.username_textbox_data = tk.Entry(self.text_data, font=(FONT_FAMILY, FONT_SIZE), bg=WHITE, fg=WHITE, width=45)
        self.username_textbox_data.grid(row=4, sticky="nsew", padx=5, pady=3, ipady=50)
        
        self.enter_condition = tk.Label(self.label_condition, text="Ingrese las condiciones:", font=(FONT_FAMILY, FONT_SIZE), bg=GREY, fg=WHITE)
        self.enter_condition.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

        self.username_textbox_cond = tk.Entry(self.text_condition, font=(FONT_FAMILY, FONT_SIZE), bg=WHITE, fg=WHITE, width=45)
        self.username_textbox_cond.grid(row=6, column=0, sticky="nsew", padx=5, pady=3, ipady=50)

        self.enter_condition = tk.Label(self.label_result, text="Resultados:", font=(FONT_FAMILY, FONT_SIZE), bg=GREY, fg=WHITE)
        self.enter_condition.grid(row=7, column=0, sticky="nsew", padx=5, pady=5)
        
        self.message_box = scrolledtext.ScrolledText(self.text_result, font=(FONT_FAMILY, SMALL_FONT_SIZE), bg=MEDIUM_GREY, fg=WHITE, width=65, height=10)
        self.message_box.pack(side=tk.TOP)
        self.message_box.config(state=tk.DISABLED)
        
        self.message_button = tk.Button(self.bottom_frame, text="Enviar", font=(FONT_FAMILY, BUTTON_SIZE), bg=BLUE, fg=WHITE, command=self.enviar_comando)
        self.message_button.pack(side=tk.RIGHT, padx=10)
    
    def run(self):
        root.mainloop()
        
    def connect(self) -> None:
        user = self.username_textbox.get()
        if user :
            self.client.connect(HOST,PORT, self.username_textbox, self.username_button, self.message_box)
        else:
            messagebox.showerror("Usuario invalido", "El usuario no puede estar vacio")
            
    def enviar_comando(self):
        table = self.list_tables.get()
        operation = self.selected_option.get()
        datos = self.username_textbox_data.get()
        condiciones = self.username_textbox_cond.get()
        if datos:
            self.client.procesar_comando(table, operation, datos, condiciones)
            self.username_textbox_data.delete(0, tk.END)
            self.username_textbox_cond.delete(0, tk.END)
        else:
            messagebox.showerror("Mensaje vacio", "No puedes enviar un mensaje vacio.")
        
if __name__ == '__main__':
    root = tk.Tk()
    home= sandbox(root)
    home.run()
    