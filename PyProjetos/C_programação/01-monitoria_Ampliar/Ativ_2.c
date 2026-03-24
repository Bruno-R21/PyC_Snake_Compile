/* 
Escreva um programa em C que receba o salário de 2 devs e calcule a média.
*/

#include <stdio.h>
#include <locale.h>

int main () {
    setlocale(LC_ALL, "Portuguese");
    
    float salario1, salario2, media;
    printf("Informe o primeiro salário: ");
    scanf( "%f" , &salario1);

    printf("Informe o segundo salário: ");
    scanf( "%f", &salario2);

    media = (salario1 + salario2) / 2;

    printf("A média é: %2.f", media);
    
    return 0;
}