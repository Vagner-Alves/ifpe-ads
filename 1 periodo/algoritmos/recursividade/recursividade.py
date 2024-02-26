# listar arquivos em uma pasta

import os

arquivos_extraidos = []

def pegar_arquivos(pasta):
    lista_arquivos = os.listdir(pasta)

    # se tiver txt e vendas na pasta vamos pegar esse arquivo
    for arquivo in lista_arquivos:
        if ".txt" in arquivo and "vendas" in arquivo:
            # pegar apenas o nome do mes
            nome_mes = arquivo.split()[-1].replace(".txt","")
            arquivos_extraidos.append(nome_mes)
        elif ".txt" not in arquivo:
            # recursividade
            pegar_arquivos(f'{pasta}/{arquivo}')

pegar_arquivos('arquivos')

print(arquivos_extraidos)

# espaço ocupado por todos os arquivos

