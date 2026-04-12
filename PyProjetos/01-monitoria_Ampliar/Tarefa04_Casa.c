/*
    Leia um valor inteiro N, tal que 1 < N < 1000.
    A seguir, mostre a tabuada multiplicação de 1 a 10 deste número.

    Exemplo:
    1 x N = N
    2 x N = 2N
    ....até 10 x N = 10N.
*/
 
#include <stdio.h>
#include <locale.h>

int main (){
  setlocale(LC_ALL, "Portuguese");
  int numero, i;

  printf("Digite um número inteiro: ");
  scanf("%d", &numero);


  if (numero > 1 && numero < 1000){
    i = 1;

     while (i <= 10){
        printf("%d x %d = %d\n", numero, i, numero * i);
        i++;
     }
  } 
  else {
    printf("Valor inválido!\n");    
  }
  
   return 0;
}