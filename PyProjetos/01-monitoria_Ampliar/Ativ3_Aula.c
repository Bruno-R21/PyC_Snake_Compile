/* Escreva um programa que receba duas notas de um aluno e calcule a média.
O programa deverá retornar se o aluno está aprovado (média >=6),
em recuperação (média <6 e >5) ou reprovado (média <=5). */

#include <stdio.h>
#include <locale.h>



int main() {
    setlocale(LC_ALL, "portuguese");
    float nota1, nota2, media; 

    printf("Informe a nota 1: ");
    scanf("%f", &nota1);
    printf("Informe a nota 2: ");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;

  if (media >= 6){
     printf("\nAprovado");   
  }
  else if (media <= 5){
    printf("\nReprovado");
  }
  else {
    printf("\nEm recuperação");
  }

  return 0;
}