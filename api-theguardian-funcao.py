import requests
import json
import pandas as pd

def exportar_csv(titulo, link, nome):
    df = pd.DataFrame({'Título' : titulo, 'Link' : link})
    df.to_csv("%s.csv" % nome, index=False, sep=";", encoding='utf-8-sig')
    # por padrão na exportação os dados vem separados por virgula, colocamos o sep com separador sendo ; para que o excel identifique os dados e separe em colunas
    print("Arquivo eexportado com sucesso para a pasta do projeto! ")

def buscar_noticias(dados):
    titulo = []
    link = []   
    for posicao in dados['response']['results']:
        titulo.append(posicao['webTitle'])
        link.append(posicao['webUrl'])
    if len(titulo) ==  0:
        print("Não foi encontrado nenhum post referente a artes. Tente mais tarde!" )
    else:
        exportar_csv(titulo, link, "noticias")

def buscar_sports(dados):
    titulo = []
    link = []   
    for posicao in dados['response']['results']:
        if posicao['pillarName'] == 'Sport':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) ==  0:
        print("Não foi encontrado nenhum post referente a artes. Tente mais tarde!" )
    else:
        exportar_csv(titulo, link, "Sport")

def buscar_News(dados):
    titulo = []
    link = []   
    for posicao in dados['response']['results']:
        if posicao['pillarName'] == 'News':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) ==  0:
        print("Não foi encontrado nenhum post referente a artes. Tente mais tarde!" )
    else:
        exportar_csv(titulo, link, "News")

def buscar_Arts(dados):
    titulo = []
    link = []   
    for posicao in dados['response']['results']:
        if posicao['pillarName'] == 'Arts':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) ==  0:
        print("Não foi encontrado nenhum post referente a artes. Tente mais tarde!" )
    else:
        exportar_csv(titulo, link, "Arts")

    

def main():
    url = "https://content.guardianapis.com/search?api-key=eac1ed6d-a7bb-4963-a129-65851a5e3483"
    response = requests.get(url)
    if response.status_code == 200:
        print("Acessando a base de dados do The Guardian")
        dados = response.json()
        escolha =  4
        while escolha != 0 :
            print("1 - Esportes")
            print("2 - Notícias")
            print("3 - Artes")
            print("4 - Todas")
            print("0 - para sair")
            try:
                escolha = int(input("Digite o número referente a noticia que você deseja baixar:"))
            except:
                print("Por favor digite apenas números")
            if escolha > 4 or escolha < 0:
                print("Por favor digite números entre 0 e 4")
            elif escolha == 1:
                buscar_sports(dados)
            elif escolha == 2:
                buscar_News(dados)
            elif escolha == 3:
                buscar_Arts(dados)
            elif escolha == 4:
                buscar_noticias(dados)
            elif escolha == 0:
                print("Obrigado por utilizar o programa")
    else:
        print("Não foi possível acessar a base de dados.")



if __name__ == "__main__":
    main()