import os
from dotenv import load_dotenv

def load_config(path_env="conf.env"):
    """
    Carrega variáveis de ambiente a partir de um arquivo .env.

    Args:
        caminho_env (str): Caminho para o arquivo .env (padrão: '.env')

    Raises:
        FileNotFoundError: Se o arquivo .env não for encontrado.
    """
    try:
        if not os.path.exists(path_env):
            raise FileNotFoundError(f"❌ Arquivo '{path_env}' não encontrado.")

        carregado = load_dotenv(dotenv_path=path_env)

        if not carregado:
            raise ValueError(f"⚠️ Nenhuma variável foi carregada de '{path_env}'.")

        print(f"✅ Variáveis de ambiente carregadas de '{path_env}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"🚨 Erro inesperado: {e}")
