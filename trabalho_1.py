#Automação e Simulação de Comportamento Humano (Evasão Simples).
#esse é um Script de Reconhecimento de Diretórios.
#feito por: Ana Carolina data:18/02/26
import random
import time

diretorios = ["/admin", "/config", "/backup", "/api", "/logs"]

print("--- INICIANDO RECONHECIMENTO DE DIRETÓRIOS ---")

for i in diretorios:
    #gera um tempo de espera aleatorio.
    tempo = random.uniform(1.5, 5.00)
    
    print(f"testando o  caminho: {i}")
    print(f"Aguardando {tempo:.2f} segundos para não ser bloqueado...")
    
    time.sleep(tempo)
    print("Reconhecimento concluido com sucesso!")
    
alvo_vulneravel = random.choice(diretorios)
print(f"RELATÓRIO: O diretório {alvo_vulneravel} deve ser investigado primeiro.")