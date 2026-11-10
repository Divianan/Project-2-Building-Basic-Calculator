import tkinter as tk
from tkinter import ttk, messagebox
import math

# =====================================================
# CONFIG
# =====================================================

BG = "#202124"
DISPLAY_BG = "#2D2E30"
NUM_BG = "#3C4043"
OP_BG = "#5F6368"
EQUAL_BG = "#1A73E8"
TEXT = "white"

# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()
root.title("CalcXpert")
root.geometry("650x550")
root.configure(bg=BG)

style = ttk.Style()
style.theme_use("clam")

# =====================================================
# GLOBALS
# =====================================================

expression = ""
memory = 0
angle_mode = "DEG"

# =====================================================
# NOTEBOOK
# =====================================================

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

standard_tab = tk.Frame(notebook, bg=BG)
scientific_tab = tk.Frame(notebook, bg=BG)
currency_tab = tk.Frame(notebook, bg=BG)

notebook.add(standard_tab, text="Standard")
notebook.add(scientific_tab, text="Scientific")
notebook.add(currency_tab, text="Currency")

# =====================================================
# STANDARD CALCULATOR
# =====================================================

std_expression = ""
std_display_var = tk.StringVar()

def std_update():
    std_display_var.set(std_expression)

def std_press(val):
    global std_expression
    std_expression += str(val)
    std_update()

def std_clear():
    global std_expression
    std_expression = ""
    std_update()

def std_back():
    global std_expression
    std_expression = std_expression[:-1]
    std_update()

def std_equal():
    global std_expression
    try:
        std_expression = str(eval(std_expression))
        std_update()
    except:
        messagebox.showerror("Error", "Invalid Expression")

std_display = tk.Entry(
    standard_tab,
    textvariable=std_display_var,
    font=("Segoe UI", 30, "bold"),
    justify="right",
    bg=DISPLAY_BG,
    fg="white",
    relief="flat"
)

std_display.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=10,
    pady=10
)

for r in range(7):
    standard_tab.grid_rowconfigure(r, weight=1)

for c in range(4):
    standard_tab.grid_columnconfigure(c, weight=1)

std_btns = [

    ("C",1,0,std_clear),
    ("⌫",1,1,std_back),
    ("(",1,2,lambda: std_press("(")),
    (")",1,3,lambda: std_press(")")),

    ("7",2,0,lambda: std_press("7")),
    ("8",2,1,lambda: std_press("8")),
    ("9",2,2,lambda: std_press("9")),
    ("/",2,3,lambda: std_press("/")),

    ("4",3,0,lambda: std_press("4")),
    ("5",3,1,lambda: std_press("5")),
    ("6",3,2,lambda: std_press("6")),
    ("*",3,3,lambda: std_press("*")),

    ("1",4,0,lambda: std_press("1")),
    ("2",4,1,lambda: std_press("2")),
    ("3",4,2,lambda: std_press("3")),
    ("-",4,3,lambda: std_press("-")),

    ("0",5,0,lambda: std_press("0")),
    (".",5,1,lambda: std_press(".")),
    ("=",5,2,std_equal),
    ("+",5,3,lambda: std_press("+"))
]

for text,row,col,cmd in std_btns:

    color = NUM_BG

    if text in ["+","-","*","/"]:
        color = OP_BG

    if text == "=":
        color = EQUAL_BG

    if text in ["C","⌫"]:
        color = "#B3261E"

    tk.Button(
        standard_tab,
        text=text,
        command=cmd,
        bg=color,
        fg="white",
        font=("Segoe UI",14,"bold"),
        relief="flat"
    ).grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=3,
        pady=3
    )

# =====================================================
# SCIENTIFIC FRAME
# =====================================================

main_frame = tk.Frame(scientific_tab, bg=BG)
main_frame.pack(fill="both", expand=True)

calc_frame = tk.Frame(main_frame, bg=BG)
calc_frame.pack(side="left", fill="both", expand=True)

history_frame = tk.Frame(
    main_frame,
    bg=DISPLAY_BG,
    width=280
)

history_frame.pack(
    side="right",
    fill="y",
    padx=3,
    pady=3
)

# =====================================================
# DISPLAY
# =====================================================

display_var = tk.StringVar()

display = tk.Entry(
    calc_frame,
    textvariable=display_var,
    justify="right",
    font=("Segoe UI",30,"bold"),
    bg=DISPLAY_BG,
    fg="white",
    relief="flat",
    bd=0,
    insertbackground="white"
)

display.grid(
    row=0,
    column=0,
    columnspan=9,
    sticky="nsew",
    padx=8,
    pady=8
)

# =====================================================
# GRID
# =====================================================

for r in range(10):
    calc_frame.grid_rowconfigure(r, weight=1)

for c in range(9):
    calc_frame.grid_columnconfigure(c, weight=1)

# =====================================================
# FUNCTIONS
# =====================================================

def update_display():
    display_var.set(expression)

def press(value):
    global expression
    expression += str(value)
    update_display()

def clear():
    global expression
    expression = ""
    update_display()

def backspace():
    global expression
    expression = expression[:-1]
    update_display()

def add_history(text):
    history_box.insert(tk.END, text)
    history_box.see(tk.END)

def equal():
    global expression

    try:
        result = str(eval(expression))

        add_history(
            f"{expression} = {result}"
        )

        expression = result
        update_display()

    except:
        messagebox.showerror(
            "Calculator",
            "Invalid Expression"
        )

# =====================================================
# MEMORY
# =====================================================

def memory_add():
    global memory

    try:
        memory += float(eval(expression))
    except:
        pass

def memory_sub():
    global memory

    try:
        memory -= float(eval(expression))
    except:
        pass

def memory_recall():
    global expression
    expression = str(memory)
    update_display()

def memory_clear():
    global memory
    memory = 0

# =====================================================
# DEG RAD
# =====================================================

def set_deg():
    global angle_mode

    angle_mode = "DEG"

    deg_btn.config(bg=EQUAL_BG)
    rad_btn.config(bg=NUM_BG)

def set_rad():
    global angle_mode

    angle_mode = "RAD"

    rad_btn.config(bg=EQUAL_BG)
    deg_btn.config(bg=NUM_BG)

# =====================================================
# SCIENTIFIC OPERATIONS
# =====================================================

def calculate_single(func):
    global expression

    try:

        value = float(eval(expression))

        if func == "sin":
            if angle_mode == "DEG":
                value = math.radians(value)
            result = math.sin(value)

        elif func == "cos":
            if angle_mode == "DEG":
                value = math.radians(value)
            result = math.cos(value)

        elif func == "tan":
            if angle_mode == "DEG":
                value = math.radians(value)
            result = math.tan(value)

        elif func == "sqrt":
            result = math.sqrt(value)

        elif func == "square":
            result = value ** 2

        elif func == "cube":
            result = value ** 3

        elif func == "inverse":
            result = 1 / value

        elif func == "log":
            result = math.log10(value)

        elif func == "ln":
            result = math.log(value)

        elif func == "factorial":
            result = math.factorial(int(value))

        elif func == "10power":
            result = 10 ** value

        elif func == "percent":
            result = value / 100

        expression = str(result)
        update_display()

    except:
        messagebox.showerror(
            "Calculator",
            "Invalid Operation"
        )

def power():
    press("**")

def insert_pi():
    press(str(math.pi))

def insert_e():
    press(str(math.e))

# =====================================================
# BUTTON HELPER
# =====================================================

def create_button(
        parent,
        text,
        row,
        col,
        cmd,
        bg=NUM_BG
):

    btn = tk.Button(
        parent,
        text=text,
        command=cmd,
        bg=bg,
        fg="white",
        font=("Segoe UI",11,"bold"),
        relief="flat"
    )

    btn.grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=3,
        pady=3
    )

    return btn

# =====================================================
# MEMORY BAR
# =====================================================

create_button(calc_frame,"MC",1,0,memory_clear)
create_button(calc_frame,"MR",1,1,memory_recall)
create_button(calc_frame,"M+",1,2,memory_add)
create_button(calc_frame,"M-",1,3,memory_sub)

deg_btn = create_button(
    calc_frame,"DEG",1,4,set_deg,EQUAL_BG
)

rad_btn = create_button(
    calc_frame,"RAD",1,5,set_rad
)

create_button(
    calc_frame,
    "C",
    1,
    6,
    clear,
    "#B3261E"
)

# =====================================================
# SCIENTIFIC BUTTONS
# =====================================================

create_button(calc_frame,"sin",2,0,
lambda: calculate_single("sin"),OP_BG)

create_button(calc_frame,"cos",2,1,
lambda: calculate_single("cos"),OP_BG)

create_button(calc_frame,"tan",2,2,
lambda: calculate_single("tan"),OP_BG)

create_button(calc_frame,"√",2,3,
lambda: calculate_single("sqrt"),OP_BG)

create_button(calc_frame,"x²",2,4,
lambda: calculate_single("square"),OP_BG)

create_button(calc_frame,"x³",2,5,
lambda: calculate_single("cube"),OP_BG)

create_button(calc_frame,"log",3,0,
lambda: calculate_single("log"),OP_BG)

create_button(calc_frame,"ln",3,1,
lambda: calculate_single("ln"),OP_BG)

create_button(calc_frame,"n!",3,2,
lambda: calculate_single("factorial"),OP_BG)

create_button(calc_frame,"10ˣ",3,3,
lambda: calculate_single("10power"),OP_BG)

create_button(calc_frame,"%",3,4,
lambda: calculate_single("percent"),OP_BG)

create_button(calc_frame,"xʸ",3,5,
power,OP_BG)

create_button(calc_frame,"1/x",4,5,
lambda: calculate_single("inverse"),OP_BG)

create_button(calc_frame,"π",5,5,
insert_pi,OP_BG)

create_button(calc_frame,"e",6,5,
insert_e,OP_BG)

# =====================================================
# NUMBER PAD
# =====================================================

buttons = [
("7",4,0),("8",4,1),("9",4,2),("/",4,3),
("4",5,0),("5",5,1),("6",5,2),("*",5,3),
("1",6,0),("2",6,1),("3",6,2),("-",6,3),
("0",7,0),(".",7,1),("(",7,2),(")",7,3)
]

for txt,row,col in buttons:
    create_button(
        calc_frame,
        txt,
        row,
        col,
        lambda x=txt: press(x)
    )

create_button(
    calc_frame,
    "⌫",
    4,
    4,
    backspace,
    "#F9AB00"
)

create_button(
    calc_frame,
    "+",
    5,
    4,
    lambda: press("+"),
    OP_BG
)

create_button(
    calc_frame,
    "=",
    6,
    4,
    equal,
    EQUAL_BG
)

# =====================================================
# HISTORY
# =====================================================

tk.Label(
    history_frame,
    text="History",
    bg=DISPLAY_BG,
    fg="white",
    font=("Segoe UI",15,"bold")
).pack(fill="x", pady=8)

history_box = tk.Listbox(
    history_frame,
    bg=BG,
    fg="white",
    font=("Consolas",10)
)

history_box.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=5
)

# =====================================================
# HISTORY RECALL
# =====================================================

def recall_history(event):

    global expression

    selection = history_box.curselection()

    if selection:

        item = history_box.get(selection[0])

        if "=" in item:

            expression = item.split("=")[1].strip()
            update_display()


history_box.bind(
    "<Double-Button-1>",
    recall_history
)

tk.Button(
    history_frame,
    text="Clear History",
    bg="#B3261E",
    fg="white",
    relief="flat",
    command=lambda: history_box.delete(0, tk.END)
).pack(
    fill="x",
    padx=5,
    pady=5
)

# =====================================================
# KEYBOARD SUPPORT
# =====================================================

def std_key_press(event):

    if notebook.index(notebook.select()) != 0:
        return

    char = event.char
    key = event.keysym

    if char in "0123456789+-*/().":
        std_press(char)

    elif key in ("Return", "KP_Enter"):
        std_equal()

    elif key == "BackSpace":
        std_back()

    elif key == "Escape":
        std_clear()


def sci_key_press(event):

    if notebook.index(notebook.select()) != 1:
        return

    char = event.char
    key = event.keysym

    if char in "0123456789+-*/().":
        press(char)

    elif key in ("Return", "KP_Enter"):
        equal()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()

    elif char.lower() == "s":
        calculate_single("sin")

    elif char.lower() == "c":
        calculate_single("cos")

    elif char.lower() == "t":
        calculate_single("tan")

    elif char.lower() == "l":
        calculate_single("log")

    elif char.lower() == "n":
        calculate_single("ln")

    elif char.lower() == "p":
        insert_pi()

    elif char.lower() == "e":
        insert_e()

    elif char.lower() == "q":
        calculate_single("square")

    elif char.lower() == "u":
        calculate_single("cube")

    elif char.lower() == "r":
        calculate_single("sqrt")

    elif char.lower() == "i":
        calculate_single("inverse")


root.bind("<Key>", std_key_press)
root.bind("<Key>", sci_key_press, add="+")
# =====================================================
# CURRENCY CONVERTER
# =====================================================

currency_rates = {
    "USD": 1.0,
    "INR": 83.50,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 151.20,
    "AUD": 1.52,
    "CAD": 1.36
}

tk.Label(
    currency_tab,
    text="Currency Converter",
    bg=BG,
    fg="white",
    font=("Segoe UI", 24, "bold")
).pack(pady=20)

amount_var = tk.StringVar()
currency_result = tk.StringVar()

currencies = list(currency_rates.keys())

from_currency = tk.StringVar(value="USD")
to_currency = tk.StringVar(value="INR")

amount_entry = tk.Entry(
    currency_tab,
    textvariable=amount_var,
    font=("Segoe UI", 18),
    justify="center"
)
amount_entry.pack(pady=10)


ttk.Label(
    currency_tab,
    text="From"
).pack()

from_box = ttk.Combobox(
    currency_tab,
    textvariable=from_currency,
    values=currencies,
    state="readonly",
    width=15
)
from_box.pack(pady=5)


ttk.Label(
    currency_tab,
    text="To"
).pack()

to_box = ttk.Combobox(
    currency_tab,
    textvariable=to_currency,
    values=currencies,
    state="readonly",
    width=15
)
to_box.pack(pady=5)
def convert_currency():

    try:

        amount = float(amount_var.get())

        source = from_currency.get()
        target = to_currency.get()

        usd_value = amount / currency_rates[source]
        converted = usd_value * currency_rates[target]

        currency_result.set(
            f"{amount:.2f} {source} = {converted:.2f} {target}"
        )

    except:

        messagebox.showerror(
            "Currency Converter",
            "Enter a valid amount"
        )


def swap_currency():

    source = from_currency.get()
    target = to_currency.get()

    from_currency.set(target)
    to_currency.set(source)

    if amount_var.get():
        convert_currency()

tk.Button(
    currency_tab,
    text="Convert",
    command=convert_currency,
    bg=EQUAL_BG,
    fg="white",
    font=("Segoe UI", 14, "bold"),
    relief="flat"
).pack(pady=10)

tk.Button(
    currency_tab,
    text="⇄ Swap",
    command=swap_currency,
    bg=OP_BG,
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat"
).pack(pady=5)

tk.Label(
    currency_tab,
    textvariable=currency_result,
    bg=BG,
    fg="#1A73E8",
    font=("Segoe UI", 20, "bold")
).pack(pady=20)

# =====================================================
# CURRENCY KEYBOARD SUPPORT
# =====================================================

def currency_key_press(event):

    if notebook.index(notebook.select()) != 2:
        return

    key = event.keysym

    if key in ("Return", "KP_Enter"):
        convert_currency()

    elif key == "Escape":

        amount_var.set("")
        currency_result.set("")

    elif event.state & 0x4 and key.lower() == "s":

        swap_currency()


root.bind("<Key>", currency_key_press, add="+")

# =====================================================
# RUN
# =====================================================

root.mainloop()