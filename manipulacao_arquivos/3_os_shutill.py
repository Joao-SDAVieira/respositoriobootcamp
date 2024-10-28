import os 
import shutil
from pathlib import Path

'''Com o path do pathlib e possivel acessar o diretorio acima do arquivo que o código está rodando, sem
precisar especificar o caminho no momento de trabalhar com um tipo de arquivo txt, csv etc'''
ROOT_PATH = Path(__file__).parent

"""usando o mkdir para criar um diretório, juntamente com o root_path para pegar o caminho relativo
obs: esse comando só pode ser usado uma vez"""
# os.mkdir(ROOT_PATH / 'novo_diretorio')

"""abrindo o arquivo usando o ROOT_PATH criado, sem precisar puxar todo o caminho a mao"""
# arquivo = open(ROOT_PATH / 'novo_arquivo.txt', 'w')

# arquivo.close()


"""Renomeando o arquivo ainda usando o os e o ROOT_PATH"""
# os.rename(ROOT_PATH / 'novo_arquivo.txt', ROOT_PATH / 'alterado.txt')

"""Removendo o arquivo usando os e ROOT_PATH. OBS: só poe ser usado uma vez"""
# os.remove(ROOT_PATH / 'alterado.txt')


"""criando um novo arquivo e movendo ele"""

arquivo = open(ROOT_PATH / 'arquivo_remover.txt', 'w')

arquivo.close()

shutil.move(ROOT_PATH / 'arquivo_remover.txt', ROOT_PATH / 'novo_diretorio' / 'novo.txt')

