from tkinter import *

cor1 = "#1e1f1e"  # preto
cor2 = '#feffff'  # branco
cor3 = '#38576b'  # azul
cor4 = '#eceff1'  # acizentado
cor5 = '#FFAB40'  # laranja

tela = Tk()
tela.title('Calculadora')
tela.geometry('235x320')
tela.config(bg=cor1)

# frames
frame_tela = Frame(tela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(tela, width=235, height=320)
frame_corpo.grid(row=1, column=0)

# global variable
valores = ''


# função
def num_calcular(num):
    global valores
    # if num == '0':
    #     valores = ''.zfill(1)
    # else:
    valores = valores + str(num)
    numeros.set(valores)


def limparTela():
    global valores
    valores = ''
    numeros.set('')


def calculos():
    global valores
    try:
        result = eval(valores)
        numeros.set(str(result))
        valores = ''
    except:
        numeros.set('ERRO')


# label
numeros = StringVar()

app_label = Label(frame_tela, textvariable=numeros, width=16, height=2, padx=0, relief=FLAT, anchor="e", justify=LEFT,
                  font='Ivy 18', bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# botoes
b1 = Button(frame_corpo, text='C', width=11, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=limparTela)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, text='%', width=5, height=2, bg=cor2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE,
            command=lambda: num_calcular('%'))
b2.place(x=118, y=0)
b3 = Button(frame_corpo, text='/', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('/'))
b3.place(x=180, y=0)

n1 = Button(frame_corpo, text='1', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE,
            command=lambda: num_calcular('1'))
n1.place(x=0, y=55)
n2 = Button(frame_corpo, text='2', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('2'))
n2.place(x=59, y=55)
n3 = Button(frame_corpo, text='3', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('3'))
n3.place(x=118, y=55)
n4 = Button(frame_corpo, text='*', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('*'))
n4.place(x=180, y=55)

n5 = Button(frame_corpo, text='4', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE,
            command=lambda: num_calcular('4'))
n5.place(x=0, y=110)
n5 = Button(frame_corpo, text='5', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('5'))
n5.place(x=59, y=110)
n6 = Button(frame_corpo, text='6', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('6'))
n6.place(x=118, y=110)

n8 = Button(frame_corpo, text='-', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('-'))
n8.place(x=180, y=110)

n9 = Button(frame_corpo, text='7', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
            overrelief=RIDGE, command=lambda: num_calcular('7'))
n9.place(x=0, y=165)
n10 = Button(frame_corpo, text='8', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: num_calcular('8'))
n10.place(x=59, y=165)
n11 = Button(frame_corpo, text='9', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: num_calcular('9'))
n11.place(x=118, y=165)
n12 = Button(frame_corpo, text='+', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: num_calcular('+'))
n12.place(x=180, y=165)
n13 = Button(frame_corpo, text='0o', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: num_calcular('0'))
n13.place(x=59, y=218)
n13 = Button(frame_corpo, text='.', width=5, height=2, bg=cor4, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: num_calcular('.'))
n13.place(x=118, y=218)
n14 = Button(frame_corpo, text='=', width=5, height=2, bg=cor5, fg=cor2, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=calculos)
n14.place(x=180, y=218)

tela.mainloop()
