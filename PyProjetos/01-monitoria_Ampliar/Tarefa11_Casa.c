/*
    O grêmio estudantil de uma escola está realizando uma eleição e precisa de um sistema para contabilizar os votos.
    Existem três candidatos concorrendo. Escreva um programa que simule o funcionamento de uma urna eletrônica.

    Há um total de 10 alunos eleitores. O programa deve ler os votos dos alunos continuamente até que todos tenham respondido.
    As opções de voto são:
    1 - Voto para a Chapa Alfa
    2 - Voto para a Chapa Beta
    3 - Voto para a Chapa Ômega
    4 - Voto em Branco
    5 - Voto Nulo

    Se o usuário digitar qualquer número diferente de 0 a 5, o programa deve exibir a mensagem "Voto Invalido"
    e exigir que o aluno escolha um número válido. Quando a votação for encerrada, o programa deve exibir o relatório completo de
    quantos votos cada chapa teve e determinar qual chapa foi a vencedora (a que teve mais votos).

    Para simplificar e não haver necessidade de tratar um empate, vamos considerar um mundo perfeito onde não existem empates.
*/

#include <stdio.h>
#include <locale.h>

int main(){
   setlocale(LC_ALL, "Portuguese");
   int i, codigo, alfa = 0, beta = 0, omega = 0, branco = 0, nulo = 0;

   printf("+++++++++++++++++ Eleição grêmio estudantil +++++++++++++++++\n");
   printf("[1] Voto para a Chapa Alfa.\n"
          "[2] Voto para a Chapa Beta.\n"
          "[3] Voto para a Chapa Ômega.\n"
          "[4] Voto em Branco.\n"
          "[5] Voto Nulo.\n");
   printf("\n");
    
   for (i = 1; i <= 10; i++){      
        printf("Digite o seu voto: ");      
        scanf("%d", &codigo);
        
        while (codigo < 1 || codigo > 5){
            printf("Voto inválido!\n Digite o seu voto: ");
            scanf("%d", &codigo);
        }                   
    
        switch (codigo){
        case 1:
        alfa = alfa + 1;
        break;
        case 2:
        beta = beta + 1;
        break;
        case 3: 
        omega = omega + 1;
        break;
        case 4:
        branco = branco + 1;
        break;
        case 5:
        nulo = nulo + 1;
        break;
                
      }  
    }
    
    printf("\nA chapa ALFA teve um total de %d voto(s).\n", alfa);
    printf("A chapa BETA teve um total de %d voto(s).\n", beta);
    printf("A chapa OMEGA teve um total de %d voto(s).\n", omega); 
    printf("Tivemos um total de %d voto(s) em BRANCO.\n", branco);
    printf("Tivemos um total de %d voto(s) NULO.\n", nulo);

    if (alfa > beta && alfa > omega){
        printf("\nA chapa vencedora foi: ALFA");
    } else if (beta > alfa && beta > omega){
        printf("\nA chapa vencedora foi: BETA");
    } else {
        printf("\nA chapa vencedora foi: OMEGA");
    }
    
    return 0;
}