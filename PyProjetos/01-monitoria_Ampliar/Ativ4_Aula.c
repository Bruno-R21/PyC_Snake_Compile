/*
Escreva um algoritimo que simule uma máquina de vendas de lata de refrigerante.
Se o cliente digitar 1, a máquina deverá soltar uma Coca-cola.
Se o cliente digitar 2, a máquina deverá soltar um guaraná.
Se o cliente digitar 3, a máquina deverá uma fanta.E se o cliente digitar um valor diferente dos anteriores*/

#include <stdio.h>
#include <locale.h>

int main() { 
    setlocale(LC_ALL, "Portuguese");  
    int opcao;

    printf("\nDigite 1 para Coca-cola.");
    printf("\nDigite 2 para Guaraná.");
    printf("\nDigite 3 para Fanta.");
    printf("\nInforme a sua opção: ");  
    scanf("%d", &opcao);

    switch (opcao){
      case 1:
         printf("\nCoca-cola.");
         break;
      case 2: 
         printf("\nGuaraná.");
         break;
      case 3: 
         printf("\nFanta.");
         break;    
      default:
         printf("\nOpção inválida.");
    }

    return 0;
}