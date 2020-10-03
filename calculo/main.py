from tkinter import *

def start():
    ##### Inicia a janela #####
    window = Tk()
    window['bg'] = "Dark Blue"

    ##### Cria um frame para trabalharmos em escala de pixels #####
    calcular = Frame(window)
    calcular.place(x=150, y=120, width=900, height=600)

    # Mostra o resultado da conta #
    visor = Label(calcular, text="0000000", bg="gray")
    visor.place(x=310, y=180, width=300, height=50)

    # Indicação de input ao usuário #
    entryl = Label(calcular, text="Resistores: ")
    entryl.place(x=200, y=250, width=100, height=50)

    # Input (Vai receber no formato: res+res2+res3...)
    entry = Entry(calcular)
    entry.place(x=310, y=250, width=300, height=50)
    
    ##### funcao para calcular os resistores em série #####
    def calcSerie():
        # Pega o input e divide os resistores pelo simbolo de soma #
        resistores = entry.get()
        valores = resistores.split('+')
        # calcula a resistencia equivalente de resistores em série #
        soma = 0
        for i in valores:
            soma += int(i)
        visor['text'] = str(soma) + "Ω"
        print(valores, soma)

    ##### funcao para calcular o mínimo múltiplo comum #####
    def mmc(nums):
        max_ = int(max(nums))
        i = 1
        while True:
            mult = max_ * i
            if all(mult%int(nr) == 0 for nr in nums):
                return mult
            i += 1
    
    ##### funcao para calcular os resistores em paralelo #####
    def calcParalelo():
        # Pega o input e divide os resistores pelo símbolo de soma #
        resistores = entry.get()
        valores = resistores.split('+')
        # recebe o mínimo múltiplo comum vindo da função mmc
        multiplo = mmc(valores)
        soma = 0
        
        # divide os numeros de cada resistor pelo minimo múltiplo comum e soma
        for i in valores:
            soma += multiplo / int(i)
        
        # divide a soma pelo mmc e retorna no visor a potência em ohms
        result = multiplo / soma
        visor['text'] = str(result) + "Ω"

    # Botão para calcular os resistores em série
    serie = Button(calcular, text="Série", bg="red", command=calcSerie)
    serie.place(x=340, y=310, width=100, height=40)

    # Botão para calcular os resistores em paralelo
    paralelo = Button(calcular, text="Paralelo", bg="red", command=calcParalelo)
    paralelo.place(x=480, y=310, width=100, height=40)

    window.geometry("1200x800+400+100")
    window.title("Lei de ohm")
    window.mainloop()

if __name__ == '__main__':
    start()
