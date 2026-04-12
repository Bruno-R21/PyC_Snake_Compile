/*
    Leia 5 valores inteiros.
    Apresente então o maior valor lido e a posição (de 1 a 5) dentre os valores lidos em que ele foi encontrado.
*/

#include <stdio.h>
#include <locale.h>

int main(){
  setlocale(LC_ALL, "Portuguese");

  int numero, maior, posicao, i;
  i = 1;

  while (i <=5){
    printf("Digite um número: ");
    scanf("%d", &numero);

    if (i == 1){
        maior = numero;
        posicao = i;
    }
    else {
        if (numero > maior){
           maior = numero;
           posicao = i;
        }
    }
    i++;
  }
  printf("O maior número foi %d e está na posição %d.", maior, posicao);
      
    return 0;
}