/*
    Escreva um programa em C que leia 5 números inteiros armazenando-os em um vetor.
    O programa deverá escrever na tela os 5 números lidos.
*/

#include <stdio.h>
#include <locale.h>

int main(){
     setlocale(LC_ALL, "Portuguese"); 
     int numeros[5] = {0};
     int i;
    
     // entrada
     for(i = 0; i < 5; i++){
        printf("Digite um número inteiro: ");
        scanf("%d", &numeros[i]);
     } 

     // saída
     printf("\nNúmeros digitados: \n");
    
      for(i = 0; i < 5; i ++){
    printf("%d\n", numeros[i]);
      }

    return 0;
}
    /* 
       ?? Você NÃO pode imprimir um array inteiro com um único printf("%d", numeros);
       ?? 3. Como se imprime um array corretamente? 

        Você precisa pensar assim:
       ?? ?Se eu quero mostrar 5 números, eu preciso passar por todos eles (for).?

        Isso significa:

        ? usar um loop (de novo)
        ? agora para SAÍDA (print)
    */