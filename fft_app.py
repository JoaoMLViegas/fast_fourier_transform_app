import tkinter as tk
from fft import polinomial_multiplication as fft_mult

root = tk.Tk()
root.title("Polinomial Multiplication")
root.resizable(False, False)


def result_to_string(poly):
    string = ""
    for i in range(len(poly)):
        if i == 0:
            string += f"{poly[i]} + "
        else:
            string += f"{poly[i]}x^{i} + "

    # retornar resultado sem o "+" no final
    return string[0:-3]


def start_algorithm():
    pol1 = [int(Entry1_0.get()), int(Entry1_1.get()), int(Entry1_2.get()), int(Entry1_3.get()), int(Entry1_4.get())]
    pol2 = [int(Entry2_0.get()), int(Entry2_1.get()), int(Entry2_2.get()), int(Entry2_3.get())]
    EntryResult.config(state='normal')
    EntryResult.delete(0, tk.END)
    EntryResult.insert(0, result_to_string(fft_mult(pol1, pol2)))
    EntryResult.config(state='readonly')


Label1 = tk.Label(root, text="Enter the first polynomial")
Label1.grid(row=0, column=0, columnspan=12, padx=10, pady=10)

LabelSeparator = tk.Label(root, text="     ")
LabelSeparator.grid(row=1, column=0)

Entry1_0 = tk.Entry(root, width=10)
Entry1_0.insert(0, 0)
Entry1_0.grid(row=1, column=1)
Label1_0 = tk.Label(root, text="+")
Label1_0.grid(row=1, column=2)

Entry1_1 = tk.Entry(root, width=10)
Entry1_1.insert(0, 0)
Entry1_1.grid(row=1, column=3)
Label1_1 = tk.Label(root, text="x +")
Label1_1.grid(row=1, column=4)

Entry1_2 = tk.Entry(root, width=10)
Entry1_2.insert(0, 0)
Entry1_2.grid(row=1, column=5)
Label1_2 = tk.Label(root, text="x^2 +")
Label1_2.grid(row=1, column=6)

Entry1_3 = tk.Entry(root, width=10)
Entry1_3.insert(0, 0)
Entry1_3.grid(row=1, column=7)
Label1_3 = tk.Label(root, text="x^3 +")
Label1_3.grid(row=1, column=8)

Entry1_4 = tk.Entry(root, width=10)
Entry1_4.insert(0, 0)
Entry1_4.grid(row=1, column=9)
Label1_4 = tk.Label(root, text="x^4")
Label1_4.grid(row=1, column=10)

LabelSeparator = tk.Label(root, text="     ")
LabelSeparator.grid(row=1, column=11)


LabelSeparator = tk.Label(root, text="     ")
LabelSeparator.grid(row=2, column=0, columnspan=12)


Label2 = tk.Label(root, text="Enter the second polynomial")
Label2.grid(row=3, column=0, columnspan=12, padx=10, pady=10)

LabelSeparator = tk.Label(root, text="")
LabelSeparator.grid(row=4, column=0)

Entry2_0 = tk.Entry(root, width=10)
Entry2_0.insert(0, 0)
Entry2_0.grid(row=4, column=1)
Label2_0 = tk.Label(root, text="+")
Label2_0.grid(row=4, column=2)

Entry2_1 = tk.Entry(root, width=10)
Entry2_1.insert(0, 0)
Entry2_1.grid(row=4, column=3)
Label2_1 = tk.Label(root, text="x +")
Label2_1.grid(row=4, column=4)

Entry2_2 = tk.Entry(root, width=10)
Entry2_2.insert(0, 0)
Entry2_2.grid(row=4, column=5)
Label2_2 = tk.Label(root, text="x^2 +")
Label2_2.grid(row=4, column=6)

Entry2_3 = tk.Entry(root, width=10)
Entry2_3.insert(0, 0)
Entry2_3.grid(row=4, column=7)
Label2_3 = tk.Label(root, text="x^3")
Label2_3.grid(row=4, column=8)

LabelSeparator = tk.Label(root, text="DFT8 (7 total degrees)")
LabelSeparator.grid(row=4, column=9, columnspan=3)

Button = tk.Button(root, text="Multiply", command=start_algorithm)
Button.grid(row=5, column=0, columnspan=12, pady=20)

EntryResult = tk.Entry(root, width=50, state='readonly')
EntryResult.grid(row=6, column=0, columnspan=12, pady=10)

root.mainloop()
