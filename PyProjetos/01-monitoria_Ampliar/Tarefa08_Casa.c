/*
    A empresa Contoso resolveu conceder um aumento de 10%% ao salário aos seus funcionários.
    Escreva um programa que leia o salário atual de um funcionário.
    O programa deve calcular e exibir o valor do aumento e o novo salário.
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    float salario, aumento, novo_salario;

    printf("Informe o salário atual do funcionário: R$");
    scanf("%f", &salario);

    aumento = (salario * 0.1);
    novo_salario = salario + aumento;

    printf("\nO aumento de 10%% no salário resultou em um valor de: R$%.2f", aumento);
    printf("\nO valor do novo salário do funcionário ficou em: R$%.2f", novo_salario);

    return 0;
}