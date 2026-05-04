/* Escreva um algoritmo em C que solicite ao usuário dois números inteiros e depois mostre o resultado da soma entre eles.*/

#include <stdio.h> //StanDard Input Output . Header
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    
    int numero, numero2, resultado;
    numero = 10;
    
    printf("Informe um n�mero: ");
    scanf("%d", &numero2);
    
    resultado = numero + numero2;
    printf("\nO Resultado da soma: %d + %d � = a: %d", numero, numero2, resultado);    

    return 0;
}
 