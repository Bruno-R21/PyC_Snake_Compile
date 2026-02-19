import tkinter as tk
import random

pontuacao = 0
prestacao = 0
limite = 0

def novo_desafio():
    global valor, salario, anos, prestacao, limite

    valor = random.randint(1000, 50000)
    salario = random.randint(1000, 8000)
    anos = random.randint(1, 10)

    meses = anos * 12
    prestacao = valor / meses
    limite = salario * 0.30

    texto.set(
        f"Valor da casa: R${valor}\n"
        f"Salário: R${salario}\n"
        f"Anos: {anos}\n"
        f"Prestação: R${prestacao:.2f}\n\n"
        "Aprovar empréstimo?"
    )

def responder(resposta):
    global pontuacao, prestacao, limite

    correto = prestacao <= limite

    if (resposta == "S" and correto) or (resposta == "N" and not correto):
        pontuacao += 10
        resultado.set("Decisão correta! +10 pontos")
    else:
        pontuacao -= 5
        resultado.set("Decisão errada! -5 pontos")

    pontos.set(f"Pontuação: {pontuacao}")
    janela.after(2000, novo_desafio)


janela = tk.Tk()
janela.title("Gerente do Banco")
janela.geometry("350x350")

texto = tk.StringVar()
resultado = tk.StringVar()
pontos = tk.StringVar(value="Pontuação: 0")

label = tk.Label(janela, textvariable=texto, font=("Arial", 12))
label.pack(pady=10)

btn_aprovar = tk.Button(janela, text="Aprovar", command=lambda: responder("S"))
btn_aprovar.pack(pady=5)

btn_negar = tk.Button(janela, text="Negar", command=lambda: responder("N"))
btn_negar.pack(pady=5)

label_resultado = tk.Label(janela, textvariable=resultado, fg="blue")
label_resultado.pack(pady=10)

label_pontos = tk.Label(janela, textvariable=pontos, font=("Arial", 12))
label_pontos.pack(pady=5)

novo_desafio()
janela.mainloop()