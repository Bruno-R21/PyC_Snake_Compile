/*
    Escreva um programa que que imprima todas as tabuadas de multiplicação de 1 a 9.

    Exemplo:
    1x1 = 1
    1x2 = 2
    ....
    Até 9x9 = 81
*/

#include <stdio.h>
#include <locale.h>

int main() {
  setlocale(LC_ALL, "Portuguese");

  int numero = 1, i;

  while (numero <= 9){
    i = 1;
    while (i <=9){ 
      printf("%d x %d = %d\n", numero, i, numero * i);
      i++;
    } 
    printf("=============\n"); 
    numero++;
  } 

  return 0;
}