#programa feito para que o computador envie uma mensagem pra ia sozinho, e ela ira me requisitar uma ficha descrevendo meu trabalho.
#feito por: Ana carolina data:13/02/26
import pyautogui as pg
import pyperclip as pc
import time

#
print("--- [TERMINAL DE CONTRATOS CYBER] ---")
print("Verificando tickets de segurança pendentes...")
#mensagem para a ia(gemini)

comando_job = (
    "Gemini, atue como meu Gerente de Segurança (Lead Pentester). "
    "Envie uma 'Ordem de Serviço' que envolva uma das seguintes áreas: "
    "Automação de tarefas, Reconhecimento de Alvos (OSINT), "
    "Análise de Vulnerabilidades simples ou Lógica de Scripts de Ataque. "
    "Apresente como um cenário de mundo real de uma empresa contratante. "
    "Trate-me como uma Pentester júnior em treinamento."
    )
#execução
print("Abra o chat com a ia, você tem 5s.....")
time.sleep(5)

pc.copy(comando_job)
pg.hotkey('ctrl', 'v')
pg.press('enter')

print("📡 Ordem de serviço solicitada. Aguarde o Briefing...")