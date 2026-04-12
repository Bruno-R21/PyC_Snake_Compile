/*
Escreva um algoritmo que leia 2 números inteiros. Calcule o produto (multiplicação) desses números e apresente o resultado.
*/

#include <stdio.h>
#include <locale.h>

int main() {
   setlocale(LC_ALL, "Portuguese"); 
   int numero1, numero2, resultado;
   
   printf("Digite o primeiro número inteiro: ");
   scanf("%d", &numero1);
   printf("Digite o segundo numero inteiro: ");
   scanf("%d", &numero2);

   resultado = numero1 * numero2;

   printf("\nO resultado da multiplicação entre %d e %d é: %d", numero1, numero2, resultado);

    return 0;
}