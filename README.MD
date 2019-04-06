![TheGuardian](img_theguardian.jpg)



# Noticias "The Guardian"
>Script criado com o intuito de consumir a API do site de noticias The Guardian e dar ao usuário a possibiidade de escolher as noticias por seção ou mostrar todas elas, sendo as opções:
  - 1 Esportes
  - 2 Noticias
  - 3 Artes
  - 4 Todas as noticias
  - 0 Sair do script

### Funções 

```sh
exportar_csv(titulo, link, nome)
buscar_noticias(dados)
buscar_sports(dados)
buscar_news(dados)
buscar_arts(dados)
```

### Comandos do GIT
```sh
$ git status
$ git add .
$ git commit -m "texto"
$ git pull --rebase origin master
$ git push origin master
```

API utilizada: [THE_GUARDIAN](https://open-platform.theguardian.com/)

### Funcionamento do script
```sh
$ git clone https://github.com/andersonevangelista/news-theguardian.git
$ cd news-theguardian
```
```sh
$ pip install requests
```
```sh
pip install json
```
```sh
pip install pandas
```
```sh
pip python api-theguardian-funcao.py
```
### Arquivo gerado
![Aplicação](arquivos_gerados.png)


### Desenvolvedor

 - Anderson Evangelista 




License
----
*Free Software!*