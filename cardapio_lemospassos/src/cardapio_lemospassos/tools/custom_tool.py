from crewai.tools import BaseTool, tool
from crewai_tools import FileWriterTool, FileReadTool
from typing import Type
import pandas as pd
import numpy as np

from pydantic import BaseModel, Field


# excel_data = FileReadTool(file_path='')

file_read_tool = FileReadTool(
    file_path='cardapio_principal.md',
    description='A tool to read the job description example file.'
)

file_writer_tool = FileWriterTool(filename="cardapio_principal.md", directory="./output", overwrite="True")


@tool
def ler_regras_edital_principal() -> str:
    """Esta ferramente acessa as restrições de edital para a montagem de cardápio principal"""
    df = pd.read_excel(
        '/workspaces/python3-poetry-pyenv/python-projects/cardapio_lemospassos/src/cardapio_lemospassos/files/Gramagens Presidios_proteina_principal_V2.xlsx')
    return df.head(1000).to_string()


@tool
def ler_pratos_proteina_principal() -> str:
    """Esta ferramenta acessa os pratos disponíveis para serem usados na montagem de cardápio de proteína principal"""
    df = pd.read_excel(
        '/workspaces/python3-poetry-pyenv/python-projects/cardapio_lemospassos/src/cardapio_lemospassos/files/pratos_proteina_principal_v5.xlsx')
    df = df.iloc[np.random.permutation(len(df))]
    return df.head(1000).to_string()

@tool
def ler_regras_edital_opcao() -> str:
    """Esta ferramente acessa as restrições de edital para montagem de opções de proteínas"""
    df = pd.read_excel(
        '/workspaces/python3-poetry-pyenv/python-projects/cardapio_lemospassos/src/cardapio_lemospassos/files/Gramagens Presidios_opcap_proteica_v2.xlsx')
    return df.head(1000).to_string()

@tool
def ler_pratos_proteina_opcao() -> str:
    """Esta ferramenta acessa os pratos disponíveis para serem usados na montagem de cardápio de opções"""
    df = pd.read_excel(
        '/workspaces/python3-poetry-pyenv/python-projects/cardapio_lemospassos/src/cardapio_lemospassos/files/pratos_proteina_opcao_v8.xlsx')
    df = df.iloc[np.random.permutation(len(df))]
    return df.head(1000).to_string()