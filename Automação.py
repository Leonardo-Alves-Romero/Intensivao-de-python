# Automação de Sistemas e Processos com Python

### Desafio:

'''Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
O seu trabalho, como analista, é enviar um e-mail para epythonimpressionador@gmailcomle, assim que começar a trabalhar, com o total gasto, a quantidade de produtos compradas

E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado'''

import pyautogui as pg
import time
import pandas as pd
import pyperclip

# pyautogui.click -> Clique com o mouse
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Apertar uma tecla
# pyautogui.hotkey -> Apertar uma combinação de teclas

pg.PAUSE = 1

# 1- Entrar no sistema da empresa
pg.click(x=1070,y=1051)

time.sleep(5)
pg.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pg.press("enter")

# Pode ser que o navegador tenha que carregar
time.sleep(5)

# 2- Fazer login no sistema da empresa
# Clicar e escrever no espaço de login
pg.click(x=916, y=470)
pg.write("meu_login")

# Clicar e escrever no espaço da senha
pg.click(x=893, y=562)
pg.write("minha_senha")

# Clicar em acessar
pg.click(x=924, y=656)
time.sleep(3)

# 3- Exportar a base de dados
pg.click(x=222, y=373) #clica no arquivo
pg.click(x=951, y=598) #faz o download
pg.click(x=1774, y=19)

# 4- Calcular os indicadores
tabela = pd.read_csv(r"Compras.csv", sep=";")
print(tabela)
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

# 5- Enviar um e-mail para o chefeminha_senha
# Chamando o email
pg.press("win")
pg.write("email")
pg.press("enter")

time.sleep(5)

# Clicar no botão novo email
pg.click(x=153, y=127)

# Preencher as informações
pg.click(x=980, y=247)
pg.write("pythonimpressionador@gmailcom")

pg.click(x=882, y=301)
pyperclip.copy("Relatório de vendas")
pg.hotkey("ctrl", "v")

pg.press("tab")

texto = f'''
Prezados,
segue relatório de compras

Total gasto: R${total_gasto:,.2f}
Quantidade de Produtos:{quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar
Att., Leo python
'''
pyperclip.copy(texto)
pg.hotkey("ctrl", "v")

# Enviar
pg.click(x=1820, y=69)