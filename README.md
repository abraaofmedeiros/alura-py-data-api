# Projeto Python e APIs: Conhecendo a biblioteca Requests

Este projeto foi desenvolvido como parte do curso **Python e APIs: conhecendo a biblioteca Requests** da Alura. Ele demonstra a utilização da biblioteca `requests` para interagir com a API do GitHub, extraindo dados de repositórios e criando novos repositórios.

---

## Funcionalidade

O projeto é dividido em duas etapas principais:

1.  A classe `DadosRepositorios` realiza uma consulta à API do GitHub para obter informações sobre os repositórios de um usuário. Em seguida, ele extrai o nome de cada repositório e suas linguagens de programação, salvando essas informações em um arquivo CSV.
2.  A classe `Repositorio` utiliza as informações extraídas para criar um novo repositório no GitHub e fazer upload de arquivos para ele, conforme especificado na função `upload_file`.

---

## Como Executar o Projeto

Para executar o projeto localmente, siga os passos abaixo:

### 1. Clonar o Repositório

Abra o terminal e execute o seguinte comando para clonar o projeto:

```bash
git clone [https://github.com/abraaofmedeiros/alura-py-data-api.git](https://github.com/abraaofmedeiros/alura-py-data-api.git)
````

### 2\. Criar e Ativar o Ambiente Virtual (Opcional)

É uma boa prática utilizar um ambiente virtual para isolar as dependências do projeto.

```bash
# Criar o ambiente virtual (venv)
python -m venv venv

# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
```

### 3\. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4\. Configurar as Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto e preencha-o com suas credenciais do GitHub. Essas variáveis serão lidas pela biblioteca `python-dotenv`.

```ini
ACCESS_TOKEN="seu token do github"
USERNAME="seu username do github"
```

> **Observação:** O `ACCESS_TOKEN` é um Personal Access Token do GitHub com permissões necessárias para ler informações de repositórios e criar novos. Para saber como gerar um, consulte a [documentação do GitHub](https://www.google.com/search?q=https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

### 5\. Executar o Script

Para iniciar o projeto, execute o script principal:

```bash
python extraindo_dados.py
```

O script irá extrair os dados, criar o arquivo CSV e, em seguida, interagir com a API do GitHub para criar um novo repositório e fazer o upload dos arquivos.

-----

## Tecnologias Utilizadas

  * **Python**: Linguagem de programação principal.
  * **Requests**: Biblioteca para fazer requisições HTTP à API do GitHub.
  * **python-dotenv**: Para carregar variáveis de ambiente a partir do arquivo `.env`.
  * **pandas**: Para manipulação e criação do arquivo CSV (se aplicável).

-----

## Autor

  * **Abraão F. Medeiros** - [Github](https://www.google.com/search?q=https://github.com/abraaofmedeiros) | [LinkedIn](https://www.google.com/search?q=https://www.linkedin.com/in/abraao-f-medeiros/)

<!-- end list -->

```
```