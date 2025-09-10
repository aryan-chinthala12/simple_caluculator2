import tkinter as tk

def Add_Numbers():
    result.set(int(num1.get()) + int(num2.get()))
def Sub_Numbers():
    result.set(int(num1.get()) - int(num2.get()))
def Mul_Numbers():
    result.set(int(num1.get()) * int(num2.get()))
def Div_Numbers():
    result.set(int(num1.get()) / int(num2.get()))

root = tk.Tk()
root.title("Simple Caluculator")

#inputs
tk.Label(root, text="Number1:").grid(row=0, column=1, padx=5, pady=5)
num1=tk.Entry(root)
num1.grid(row=0, column=2, padx=5, pady=5)


tk.Label(root, text="Number2:").grid(row=1, column=1, padx=5, pady=5)
num2=tk.Entry(root)
num2.grid(row=1, column=2, padx=5, pady=5)

#buttons side by side
tk.Button(root, text="+", width=5, command=Add_Numbers).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="-", width=5, command=Sub_Numbers).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="*", width=5, command=Mul_Numbers).grid(row=2, column=2, padx=5, pady=5)
tk.Button(root, text="%", width=5, command=Div_Numbers).grid(row=2, column=3, padx=5, pady=5)

#result label
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).grid(row=3, column=0, columnspan=4, pady=10) 

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
