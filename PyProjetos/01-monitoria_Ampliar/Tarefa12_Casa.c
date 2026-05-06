/*
    Um estagiário decidiu começar a investir sua bolsa e precisa de um programa para simular seus rendimentos.
    Nos juros compostos, o juro de cada mês é calculado sobre o montante acumulado do mês anterior (o famoso "juros sobre juros").
    Fórmula matemática de juros compostos: M = C (1+i)^t, onde M é o Valor final, C é o valor inicial, i é a taxa de juros
    e t é o tempo (^t lê-se "elevado à t").

    Escreva um programa que calculo o valor final para este estagiário.
*/
#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");

    // Variáveis do programa.
    float capital, taxa_juros, valor_atual, valor_final ;
    float imposto, lucro_bruto, lucro_liquido, percentual;
    int tempo;

    // Solicita os dados de entrada para o usuário.  
    printf("\nInforme o valor inicial (capital) que deseja investir: R$ ");
    scanf("%f", &capital);
    printf("Informe a taxa de juros mensal em (%%): ");
    scanf("%f", &taxa_juros);
    printf("Informe o tempo de duração do investimento em (meses): ");
    scanf("%d", &tempo);
 
    // Convertendo porcentagem para decimal.
    taxa_juros = taxa_juros / 100; 
    // Inicia a variável 'valor_atual' com o valor da variável 'capital'. 
    valor_atual = capital; 
    
    // Calculando o crescimento mês a mês.
    for (int i = 1; i <= tempo; i++) { 

        valor_atual = valor_atual * (1 + taxa_juros); // Juros compostos.
        printf("\nResultado do mês %d: R$ %.2f", i, valor_atual); // Mostra o resultado de cada mês.
        
    }

    lucro_bruto = (valor_atual - capital); // Calcula o lucro bruto.
    imposto = lucro_bruto * 0.15; // Calcula o imposto de renda de 15% sobre o lucro.
    percentual = (lucro_bruto / capital) * 100; // Calcula o percentaual de crescimento.

    // Exibe os dados do investimento.
    printf("\n");
    printf("\n*************** Dados do investimento ***************\n");
    printf("\nO valor inicial (capital) foi de: R$ %.2f", capital);
    printf("\nO lucro líquido com o investimento (Já descontado o IR) teve o valor de: R$ %.2f", lucro_bruto - imposto); 
    printf("\nO imposto de renda retido teve o valor de R$ %.2f", imposto);
    printf("\nO percentual de crescimento do investimento foi de: %.2f%%", percentual);
    printf("\nO valor final liquido é de R$ %.2f", valor_atual - imposto);
    return 0;
}
