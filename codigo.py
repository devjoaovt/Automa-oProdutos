# Passo a passo do programa:
# Passo 1: Entrar no sistema da  emrpesa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 ate acabar a lista

link_system = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' #link do sistema
import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(link_system)
pyautogui.press('enter')
#pausa para o sistema carregar corretamente
time.sleep(2)

#Fazer login
#clicar no campo de email
pyautogui.click(x=834, y=401)
pyautogui.write('emailaleatorio@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha aleatoria')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(2)

# Passo 3: Abrir a base de dados (importar o arquivo)

import pandas
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    #codigo
    pyautogui.click(x=822, y=300)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    #preço
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    #voltar para o inicio:
    pyautogui.scroll(5000)