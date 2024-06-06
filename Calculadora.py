import tkinter as tk


def click_boto(numero):
    global operador
    operador = operador + str(numero)
    input_text.set(operador)


def resultat():
    global operador
    try:
        opera = str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("Error")
        operador = ""


def clear():
    global operador
    operador = ("")
    input_text.set("0")


root = tk.Tk()
root.title("Calculadora")
root.geometry("400x500")
finestra = root

finestra.configure(background="#2F4F4F")
color_boto = "gray77"
ample_boto = 7
altura_boto = 2
color_text = "#000080"
font = ("Courier", 14, 'bold')

input_text = tk.StringVar()
operador = ""

pantalla = tk.Entry(finestra, font=('arial', 20, 'bold'), width=22, textvariable=input_text,
                    bd=20, insertwidth=4, bg="#E6E6FA", justify="right")
pantalla.place(x=10, y=60)

tk.Button(finestra, text="1", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(1)).place(x=17, y=180)
tk.Button(finestra, text="2", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(2)).place(x=107, y=180)
tk.Button(finestra, text="3", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(3)).place(x=197, y=180)
tk.Button(finestra, text="4", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(4)).place(x=17, y=245)
tk.Button(finestra, text="5", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(5)).place(x=107, y=245)
tk.Button(finestra, text="6", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(6)).place(x=197, y=245)
tk.Button(finestra, text="7", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(7)).place(x=17, y=310)
tk.Button(finestra, text="8", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(8)).place(x=107, y=310)
tk.Button(finestra, text="9", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(9)).place(x=197, y=310)
tk.Button(finestra, text="0", bg=color_boto, fg=color_text, font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto(0)).place(x=107, y=375)
tk.Button(finestra, text="C", bg="#8B0000", fg="#FFFFFF", font=font, width=ample_boto, height=altura_boto, command=clear).place(x=17, y=375)
tk.Button(finestra, text="+", bg=color_boto, fg="#000000", font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto("+")).place(x=297, y=180)
tk.Button(finestra, text="=", bg=color_boto, fg="#006400", font=font, width=ample_boto, height=altura_boto, command=resultat).place(x=197,y=375)
tk.Button(finestra, text="-", bg=color_boto, fg="#000000", font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto("-")).place(x=297, y=245)
tk.Button(finestra, text="*", bg=color_boto, fg="#000000", font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto("*")).place(x=297, y=310)
tk.Button(finestra, text="/", bg=color_boto, fg="#000000", font=font, width=ample_boto, height=altura_boto, command=lambda: click_boto("/")).place(x=297, y=375)

clear()
root.mainloop()