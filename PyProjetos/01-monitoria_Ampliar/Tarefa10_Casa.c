/*
    Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo.
    Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.
    Escreva um programa que leia um número e diga se ele é primo ou não.
*/

#include <stdio.h>
#include <locale.h>

int main(){
   setlocale(LC_ALL, "Portuguese"); 
   int i, numero;
   int ePrimo = 1;

   printf("Informe um número inteiro: ");
   scanf("%d", &numero);

    if (numero <= 1){
      printf("O número %d NÃO é primo.", numero);
      return 0;     
   } 
   
    for (i = 2; i * i <= numero; i++){
      if (numero % i == 0){
        ePrimo = 0;
        break;
     }
   }
    if (ePrimo){
        printf("\nO número %d é primo.", numero);
    } else {
        printf("\nO número %d NÃO é primo.", numero);
    }

    return 0;
}