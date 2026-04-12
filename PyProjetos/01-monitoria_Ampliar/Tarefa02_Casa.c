/*
Escreva um algotitmo que leia um número inteiro. O algoritmo deverá informar se este número é par ou ímpar e informar se é um número positivo ou negativo. Nesta atividade, considere o 0 (zero) como um número positivo e par.
 */

#include <stdio.h>
#include <locale.h>

int main(){
   setlocale(LC_ALL, "Portuguese");
   int numero;

   printf("Digite um número inteiro: ");
   scanf("%d", &numero);
   

   if (numero % 2 == 0) {
     printf("O número é PAR.\n");
     if (numero >= 0) {
        printf("O número é POSITIVO.\n"); 
     }
     else {
        printf("O número é NEGATIVO.\n");
     }
   }
   else {
     printf("O número é IMPAR.\n");
     if (numero >= 0) {
        printf("O número é POSITIVO.\n");
     }
     else {
        printf("O número é NEGATIVO.\n");
     }
   }

   return 0;
}