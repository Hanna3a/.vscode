#Filtro de Firewall de IP 
#final da minha primeira prova
#data: 10/02/26 Feito por: Ana Carolina
ips_bloqueados = ["192.168.1.50", "10.0.0.15", "172.16.254.1"]
# 192.168.x.x é um padrão muito comum em redes domésticas.
#10.0.x.x costuma ser usado em grandes redes de empresas.
#172.16.x.x também é um endereço de rede privada
while True:
    entrada = input("Digite seu seu IP para entrar na rede, ou digite 'sair' para encerrar o programa.")
    if entrada == "sair":
        print("Saindo do sistema...")
        break
    if entrada in ips_bloqueados:
        print("ACESSO NEGADO!")
    else:
        print("Acesso permitido. Bem-vindo.")