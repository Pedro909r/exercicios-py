nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas inseridas é: {media:.2f}")

total_horas = int(input("Digite a quantidade total de horas: "))
dias = total_horas // 24
horas_restantes = total_horas % 24
print(f"{total_horas} horas equivalem a {dias} dia(s) e {horas_restantes} hora(s).")

cigarros_por_dia = int(input())
anos_fumando = int(input())

total_cigarros = cigarros_por_dia * 365 * anos_fumando
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (60 * 24)

print(f"Ao fumar por {anos_fumando} anos, você perdeu aproximadamente {dias_perdidos:.0f} dias de vida.")
