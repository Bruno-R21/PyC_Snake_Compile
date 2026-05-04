/*
Escreva um algoritimo que simule uma m?quina de vendas de lata de refrigerante.
Se o cliente digitar 1, a m?quina dever? soltar uma Coca-cola.
Se o cliente digitar 2, a m?quina dever? soltar um guaran?.
Se o cliente digitar 3, a m?quina dever? uma fanta.E se o cliente digitar um valor diferente dos anteriores*/

#include <stdio.h>
#include <locale.h>

int main()
{
   setlocale(LC_ALL, "Portuguese");
   int opcao;

   printf("\nDigite 1 para Coca-cola.");
   printf("\nDigite 2 para Guaraná.");
   printf("\nDigite 3 para Fanta.");
   printf("\nInforme a sua opção de refrigerante: ");
   scanf("%d", &opcao);

   switch (opcao)
   {
   case 1:
      printf("\nNada como uma Coca-cola bem gelada.");
      break;
   case 2:
      printf("\nGuaraná, um sabor brasileiro.");
      break;
   case 3:
      printf("\nFanta é sabor e diversão.");
      break;
   default:
      printf("\nOpção inválida.");
   }
 
   return 0;
}