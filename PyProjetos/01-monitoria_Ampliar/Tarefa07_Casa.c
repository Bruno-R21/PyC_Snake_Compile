/*
    Leia dois valores inteiros X e Y.
    A seguir, calcule e mostre a soma dos números ímpares entre eles (não incluindo os próprios X e Y, se forem ímpares).

    Exemplo:
    X = 5
    Y = 15
    Soma = 7 + 9 + 11 + 13
    Saída = 40
*/

#include <stdio.h>
#include <locale.h>

int main(){
  setlocale(LC_ALL, "Portuguese");
  int i, x, y, limite, maior, menor, soma;
  soma = 0;
  
  printf("Informe o primeiro número: ");
  scanf("%d", &x);
  printf("Informe o segundo número: ");
  scanf("%d", &y);
  printf("\n");

  if (x > y){
    maior = x;
    menor = y;
  }
  else {
    maior = y;
    menor = x;
  }
  i = menor + 1;
  limite = maior - 1;

  while (i <= limite){
    if (i % 2 == 1){
      soma = soma + i; 
    }
    i++;
  }

  
  printf("O maior é %d e o menor é %d", maior, menor);
  printf("\nA soma dos números ímpares entre eles é %d", soma);

  return 0;
}


