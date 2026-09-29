import pandas as pd
import time
import pyautogui as pg

pg.PAUSE = 0.5 #pausa de 0.5 segundo entre cada comando

sistema = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' #sistema de cadastro de produtos criado para o curso de Python da Hashtag Treinamentos
email = 'voce@hashtag.com' #email fictíciode login do sistema
senha = 'sua_senha' #senha fictícia de login do sistema
tabela = pd.read_csv('produtos.csv') #abrir a base de dados com os produtos
print(tabela) #imprimir a tabela de produtos para verificar se está correta

#inicia o processo de login no sistema

pg.press('win') #abrir o inicar para abrir o navegador
pg.write('firefox') #escrever o nome do navegador
pg.press('enter') #pressionar enter para abrir o navegador
time.sleep(1) #esperar 1 segundo para o site carregar
pg.write(sistema) #escrever o site do sistema
pg.press('enter') #pressionar enter para acessar o site
time.sleep(1) #esperar 1 segundo para o site carregar
pg.click(x=614, y=468) #clicar na tela para marcar a posição do campo de login
pg.write(email) #escrever o email
pg.press('tab') #pressionar tab para ir para o campo da senha
pg.write(senha) #escrever a senha
pg.press('tab') #pressionar tab para ir para o botão de login
pg.press('enter') #pressionar enter para fazer login
time.sleep(3) #esperar 3 segundos para o site carregar

#inicia o cadastramento de produtos.   

for linha in tabela.index: #para cada linha da tabela de produtos
    codigo = str(tabela.loc[linha, 'codigo']) #pegar o código do produto da linha atual
    marca = str(tabela.loc[linha, 'marca']) #pegar a marca do produto da linha atual
    tipo = str(tabela.loc[linha, 'tipo']) #pegar o tipo do produto da linha atual
    categoria = str(tabela.loc[linha, 'categoria']) #pegar a categoria do produto da linha atual
    preco = str(tabela.loc[linha, 'preco_unitario']) #pegar o preço unitário do produto da linha atual
    custo = str(tabela.loc[linha, 'custo']) #pegar o custo do produto da linha atual
    obs = str(tabela.loc[linha, 'obs']) #pegar as observações do produto da linha atual
    pg.click(x=647, y=319) #clicar na tela para marcar a posição do campo Código de Produto
    pg.write(codigo) #escrever o código do produto
    pg.press('tab') #pressionar tab para ir para o campo Marca do Produto
    pg.write(marca) #escrever a marca do produto
    pg.press('tab') #pressionar tab para ir para o campo Tipo do Produto
    pg.write(tipo) #escrever o tipo do produto
    pg.press('tab') #pressionar tab para ir para o campo Categoria do Produto
    pg.write(categoria) #escrever a categoria do produto
    pg.press('tab') #pressionar tab para ir para o campo Preço do Produto
    pg.write(preco) #escrever o preço do produto
    pg.press('tab') #pressionar tab para ir para o campo Custo do Produto
    pg.write(custo) #escrever o custo do produto
    pg.press('tab') #pressionar tab para ir para o campo Observações
    if obs != 'nan': #se houver observações
        pg.write(obs) #inclui a observação do produto
    pg.press('tab') #pressionar tab para ir para o botão de cadastrar
    pg.press('enter') #pressionar enter para cadastrar o produto
    time.sleep(1) #esperar 1 segundo para o cadastro ser concluído
    pg.scroll(5000) #rolar a tela para cima para cadastrar o próximo produto

