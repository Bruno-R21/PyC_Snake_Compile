/* 
Escreva um programa em C que receba o sal?rio de 2 devs e calcule a m?dia.
*/

#include <stdio.h>
#include <locale.h>

int main () {
    setlocale(LC_ALL, "Portuguese");
    
    float salario1, salario2, media;
    printf("Informe o primeiro sal?rio: "); //Solicitando dados de entrada para o usuário.
    scanf( "%f" , &salario1);

    printf("Informe o segundo sal?rio: ");
    scanf( "%f", &salario2);

    media = (salario1 + salario2) / 2; //Calculando a média

    printf("A m?dia ?: %2.f", media);
    
    return 0;
}