import random

pontuacao = 0

def cargo(pontos):
    if pontos >= 100:
        return "Diretor do Banco"
    elif pontos >= 50:
        return "Gerente"
    elif pontos >= 20:
        return "Assistente"
    else:
        return "Estagiário"


for rodada in range(1, 6):
    print(f"\n=== Rodada {rodada} ===")

    valor = random.randint(1000, 50000)
    salario = random.randint(1000, 8000)
    anos = random.randint(1, 10)

    meses = anos * 12
    prestacao = valor / meses
    limite = salario * 0.30

    print(f"Casa: R${valor}")
    print(f"Salário: R${salario}")
    print(f"Anos: {anos}")
    print(f"Prestação: R${prestacao:.2f}")

    resp = input("Aprovar? (S/N): ").upper()
    correto = prestacao <= limite

    if (resp == "S" and correto) or (resp == "N" and not correto):
        pontuacao += 10
        print("Decisão correta!")
    else:
        pontuacao -= 5
        print("Decisão errada!")

    print(f"Pontuação: {pontuacao}")
    print(f"Cargo atual: {cargo(pontuacao)}")

print("\n=== Fim do jogo ===")
print(f"Pontuação final: {pontuacao}")
print(f"Cargo final: {cargo(pontuacao)}")