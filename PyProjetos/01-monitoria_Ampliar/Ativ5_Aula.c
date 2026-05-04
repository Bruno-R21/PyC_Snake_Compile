/* 
Abaixo segue o código criado na Atv4.
Refatore o código para atender a seguinte regra de negócio: Quando o cliente informar um código inválido, o programa deverá retornar ao menu solicitando que insira novamente a opção.
*/

#include <stdio.h>
#include <locale.h>

int main()
{
   setlocale(LC_ALL, "Portuguese");
   int opcao;

   do
   {
      printf("\nDigite 1 para Coca-cola.");
      printf("\nDigite 2 para Guaraná.");
      printf("\nDigite 3 para Fanta.");
      printf("\nInforme a sua opção de refrigerante: ");
      scanf("%d", &opcao);

      switch (opcao)
      {
      case 1:
         printf("\nÓtima escolha! \nNada como uma Coca-cola bem gelada.");
         break;
      case 2:
         printf("\nMandou bem! \nGuaraná, um sabor brasileiro.");
         break;
      case 3:
         printf("\nPerfeito! \nFanta é sabor e diversão.");
         break;         
      default:
            printf("\nOpção inválida.");
      }
   } while (opcao < 1 || opcao > 3);

   printf("\nCompra finalizada! \nAproveite seu refrigerante.");

   return 0;
}   