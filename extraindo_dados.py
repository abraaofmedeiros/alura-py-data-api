from utils.dados_repos import DadosRepositorios, Repositorio
from utils.load_config import *

# Configurações Iniciais
load_config()
access_token = os.getenv("ACCESS_TOKEN")
username = os.getenv("USERNAME")

# Extraindo dados
print("Iniciando Extração: Amazon")
amazon_rep = DadosRepositorios('amzn', access_token)
lings_amazon = amazon_rep.criar_df_nomes_linguagens_repos()
path_amazon = 'dados/amazon.csv'
DadosRepositorios.df_to_csv(lings_amazon, path_amazon)

print("Iniciando Extração: Netflix")
netflix_rep = DadosRepositorios('netflix', access_token)
lings_netflix = netflix_rep.criar_df_nomes_linguagens_repos()
path_netflix = 'dados/netflix.csv'
DadosRepositorios.df_to_csv(lings_netflix, path_netflix)

print("Iniciando Extração: Spotify")
spotify_rep = DadosRepositorios('spotify', access_token)
lings_spotify = spotify_rep.criar_df_nomes_linguagens_repos()
path_spotify = 'dados/spotify.csv'
DadosRepositorios.df_to_csv(lings_spotify, path_spotify)

# Loading 
repository_name = 'linguagens_utilizadas'
description = 'Repositório com as linguagens de programação da Amazon'

new_rep = Repositorio(username, access_token, repository_name, description)

new_rep.upload_file(path_amazon, 'amazon.csv', 'Adicionando dados Amazon')
new_rep.upload_file(path_netflix, 'netlifx.csv', 'Adicionando dados Netflix')
new_rep.upload_file(path_spotify, 'spotify.csv', 'Adicionando dados Spotify')