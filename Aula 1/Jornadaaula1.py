# Bibliotecas
import pyautogui
import time
import pandas as pd

# pyautogui.click = clicar
# pyautogui.write = escrever
# pyautogui.press = aperta tecla
#pyautogui.hotkey = aperta atalho

# passo 1: Abrir navegador e entrar no sistema da empresa
link_sys = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "gumrodrigues07@gmail.com"
senha = "123ainN."
time.sleep(10)
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(1)
#pyautogui.press("tab", presses=7)
#pyautogui.press("enter")
pyautogui.click(x=884, y=388)
pyautogui.write(link_sys)
pyautogui.press("enter")
time.sleep(3)

# passo 2: Fazer login
pyautogui.press("tab")
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("enter")
time.sleep(3)
# passo 3: Abrir base de dados
tabela = pd.read_csv("produtos.csv")

# passo 4: Cadastrar produto

for linha in tabela.index:
    pyautogui.click(x=412, y=247)
    # Codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # Preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    # Cadastrar
    pyautogui.press("enter")
    # Voltar para o inicio da pagina
    pyautogui.scroll(10000)
    
# passo 5: Repetir passo 4 até acabar a lista
