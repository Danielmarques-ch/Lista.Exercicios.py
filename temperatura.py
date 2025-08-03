#### 4.Em quais meses a média de temperatura foi maior do que a média nacional?
meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

media_nacional = sum(temperaturas) / len(temperaturas) #Encontrando a media nacional
print('A média nacional é de {:,}'. format(media_nacional))
meses_maior_media = [] #Criando lista auxiliar

for i, mes in enumerate(meses):
        if temperaturas[i] > media_nacional:
            print(f"{mes}: {temperaturas[i]} graus")