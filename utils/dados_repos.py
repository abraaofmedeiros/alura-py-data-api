import requests
import pandas as pd

import base64

class DadosRepositorios:

    def __init__(self, owner, token): 
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }
        self.repos_list = self.__lista_repositorios()
    
    def __lista_repositorios(self):
        repos_list = []
        url = f"{self.api_base_url}/users/{self.owner}/repos"
        page_num = 1
        
        while True:
            try:
                url_page = f"{url}?page={page_num}"
                response = requests.get(url_page, headers=self.headers)

                page_repos = response.json()

                if len(page_repos) == 0:
                    break

                repos_list.extend(page_repos)
            except:
                repos_list.append(None)

            page_num += 1
        
        print("Listagem de repositórios realizada com sucesso!")

        return repos_list
    
    def criar_df_nomes_linguagens_repos(self):
        filtered_repos = [
            {"name": repo["name"], "language": repo["language"]}
            for repo in self.repos_list
            if "name" in repo and "language" in repo
            ]

        return pd.DataFrame(filtered_repos)
    
    @classmethod
    def df_to_csv(cls, df, path):
        df.to_csv(path)

        print(f"Arquivo {path} criado com sucesso!")

class Repositorio:
    def __init__(self, username, token, repository_name, description, private=False): 
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }
        self.name = repository_name
        self.description = description
        self.private = private
        self.__create_repository()

    def __create_repository(self):
        data = {
            'name': self.name,
            'description': self.description,
            'private': self.private
        }

        url = f"{self.api_base_url}/user/repos"

        try:
            response = requests.post(url, json=data, headers=self.headers)

            print(f"Status code criação do repositório: {response.status_code}")     

        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão ou requisição: {e}")

    def upload_file(self, path, filename, message):
        try:
            with open(path, 'rb') as file:
                file_content = file.read()
                encoded_content = base64.b64encode(file_content)
        except FileNotFoundError:
            print(f"Arquivo local '{path}' não encontrado.")
            return None

        data = {
            "message": message,
            "content": encoded_content.decode('utf-8')
        }

        url = f'{self.api_base_url}/repos/{self.username}/{self.name}/contents/{filename}'

        response = requests.put(url, json=data, headers=self.headers)
        print(f"Status code upload arquivo {filename}: {response.status_code}")

        return None