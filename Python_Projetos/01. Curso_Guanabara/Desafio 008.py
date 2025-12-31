# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Digite um valor em metros:')
medida = float(input())

km = (medida / 1000)
hm = (medida / 100)
dam = (medida / 10)
dm = (medida * 10)
cm = (medida * 100)
mm = (medida * 1000)


print('A quantidade digitada foi de {} metros: \nConvertendo em Quilômetros, o valor será: {} \nConvertendo em Hectômetros, o valor será:{} \nConvertendo em Decâmetros, o valor será: {} \nConvertendo em Decímetros, o valor será: {:.0f} \nConvertendo em Centímetros, o valor será: {:.0f} \nConvertendo em Milímetros, o valor será: {:.0f}'.format(medida, km, hm, dam, dm, cm, mm))

