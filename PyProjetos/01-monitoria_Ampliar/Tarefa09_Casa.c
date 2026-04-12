/*
Uma loja está com uma promoção de descontos progressivos baseados no valor total da compra:
- Compras acima de R$500,00 recebem 20% de desconto.
- Compras de R$200,00 até R$500,00, recebem 10% de desconto.- Compras abaixo de R$200,00 recebem apenas 5% de desconto.
Escreva um programa que leia o valor da compra, calcule o desconto e mostre o valor final a pagar.
*/

#include <stdio.h>
#include <locale.h>

int main(){
   setlocale(LC_ALL, "Portuguese");
   float valor_compra, desconto, valor_final;

   printf("Informe o valor total da compra: R$");
   scanf("%f", &valor_compra);

   if (valor_compra < 0){
    printf("\nValor inválido!");
    return 0;
   }

   if (valor_compra > 500){
     desconto = (valor_compra * 0.2);
   } else if (valor_compra >= 200 && valor_compra <= 500){
     desconto = (valor_compra * 0.1);
   } else {
     desconto = (valor_compra * 0.05);
   }  
   
    valor_final = (valor_compra - desconto);
    printf("\nO valor final a pagar foi de: R$%.2f", valor_final);
    printf("\nO desconto foi no valor de: R$%.2f", desconto);    

    return 0;
}