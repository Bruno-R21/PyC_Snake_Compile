/*
    Escreva um algoritmo em C que leia o nome de uma pessoa.
    O programa deverá escrever na tela "Bem Vindo [nome da pessoa]".
*/

#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "Portuguese");
    char nome[50];

    printf("Informe o seu primeiro nome: ");
    scanf("%49[^\n]s", nome);

    printf("\nOlá %s, seja bem-vindo!", nome);

    return 0;
} 