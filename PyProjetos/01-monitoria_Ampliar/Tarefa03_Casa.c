/*
    Com base em uma tabela de preços a seguir:
    1- Cachorro Quente R$ 4.00
    2- X-Salada R$ 4.50
    3- X-Bacon R$ 5.00
    4- Torrada Simples R$ 2.00
    5- Refrigerante R$ 1.50

    Escreva um programa que leia o código de um item e a quantidade deste item.
    A seguir, calcule e mostre o valor da conta a pagar
*/
#include <stdio.h> 
#include <locale.h>

int main() {
  setlocale(LC_ALL, "Portuguese");  
  int codigo, quantidade;
  float preco, total;

  printf("Cardápio de Lanches.\n");
  printf("[1] Cachorro Quente R$ 4.00\n");
  printf("[2] X-Salada R$ 4.50\n");
  printf("[3] X-Bacon R$ 5.00\n");
  printf("[4] Torrada Simples R$ 2.00\n");
  printf("[5] Refrigerante R$ 1.50]\n");
  printf("Informe o código escolhido: ");
  scanf("%d", &codigo);

  printf("\n");

  switch (codigo){
     case 1:
        preco = 4.00;
        printf("Iten escolhido: Cachorro Quente.\n");
        break;
     case 2:
        preco = 4.50;
        printf("Iten escolhido: X-Salada.\n");
        break;
     case 3:
        preco = 5.00;
        printf("Iten escolhido: X-Bacon.\n");
        break;   
     case 4:
        preco = 2.00;
        printf("Iten escolhido: Torrada Simples.\n");
        break;  
     case 5:
        preco = 1.50;
        printf("Iten escolhido: Torrada Simples.\n");
        break;  
     default:
        printf("Código inválido.\n");       
        return 0;
    } 
    printf("Digite a quantidade: ");
    scanf("%d", &quantidade);

    total = quantidade * preco; 
    printf("\nA quantidade foi: %d e total a pagar é R$%.2f", quantidade, total);

    return 0;
}