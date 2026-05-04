/* Escreva um programa que receba duas notas de um aluno e calcule a média.
O programa deverá retornar se o aluno está aprovado (média >=6),
em recuperação (média <6 e >5) ou reprovado (média <=5). */

#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "portuguese");
    float nota1, nota2, media; 
    char *mensagem; //Fiz uso de um ponteiro

    printf("\nInforme a nota 1: ");
    scanf("%f", &nota1);
    printf("\nInforme a nota 2: ");
    scanf("%f", &nota2);

    media = (nota1+nota2) / 2;

  if (media >= 6.0) {
     mensagem = "Aprovado";   
  }
  else if (media <= 5.0) {
    mensagem = "Reprovado";
  }
  else {
    mensagem = "Em recuperação";
  }
 printf("\nA sua média foi de %.2f \nVocê está %s!", media, mensagem);

  return 0;
}