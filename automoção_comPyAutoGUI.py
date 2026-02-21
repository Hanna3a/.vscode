#automoção de mensagens, para enviar muitas mensagens ao mesmo tempo
#feito por: Ana Carolina data:11/02/26
import pyautogui as pg
import pyperclip as pc
import time

quantidade = int(input("Quantas vezes vc quer enviar o joinha?"))
mensagem = input("Qual mensagem você quer enviar com o joinha? (Ex: Valeu!):")

mensagem_com_emoji = f" {mensagem} ❤️"

# Copia o emoji para a memória do computador (Ctrl+C invisível)
pc.copy(mensagem_com_emoji)

# tempo pra clicar na janela de algum app de mensagem antes de começar.
print("Contagem regressiva: 10 segundos para você clicar no chat! ")
time.sleep(10)

for i in range(quantidade):
#Cola o emoji usando o atalho de teclado
    pg.hotkey('ctrl', 'v')
#Aperta Enter para enviar
    pg.press("enter")
    time.sleep(1)

print("automoção finalizada com sucesso!")