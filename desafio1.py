#Edilson Armazenando as informações daexecução:
projeto = "PayNext Fintech"
modulo = "Gateway de Pagamento (Pix e Cartão)"
responsavel = "Marina Silva"
data_execucao = "10/11/2026"

# Edilson: armazenando os resultados dos testes.

testes_aprovados = 48
testes_reprovados = 6
testes_nao_executados = 6

# Edilson: exibindo o título do relatório

print("=" * 45)
print("RELATÓRIO DE EXECUÇÃO DE TESTES")
print("=" * 45)
print(" ")

# Edilson: Apresenta os dados da execução.

print(f"Projeto: {projeto}")
print(f"Módulo: {modulo}")
print(f"Responsável: {responsavel}")
print(f"Data da execução: {data_execucao}")

# Edilson: finalizando a inicialização.
print(" ")
print("=" * 45)
print("INICIALIZAÇÃO CONCLUÍDA")
print("=" * 45)

# Gabriel: Apresenta os resultados dos testes executados.

print("")
print("=" * 45)
print("RESULTADOS REGISTRADOS")
print("=" * 45)
print("")

print(f"Testes aprovados: {testes_aprovados}")
print(f"Testes reprovados: {testes_reprovados}")
print(f"Testes não executados: {testes_nao_executados}")

# Gabriel: Finaliza o registro dos resultados.

print("")
print("=" * 45)
print("REGISTRO CONCLUÍDO")
print("=" * 45)


# Edilson: Calcula a quantidade total de testes.

total_testes = testes_aprovados + testes_reprovados + testes_nao_executados

# Edilson: Calcula a quantidade de testes executados.

testes_executados = testes_aprovados + testes_reprovados

# Edilson: Calcula as taxas percentuais dos testes.

taxa_aprovacao = (testes_aprovados / testes_executados) * 100
taxa_reprovacao = (testes_reprovados / testes_executados) * 100
taxa_nao_executados = (testes_nao_executados / total_testes) * 100

# Edilson: Apresenta as métricas da execução.

print("")
print("=" * 45)
print("MÉTRICAS DA EXECUÇÃO")
print("=" * 45)
print("")

print(f"Total de testes: {total_testes}")
print(f"Testes executados: {testes_executados}")
print("")

print(f"Taxa de aprovação: {taxa_aprovacao:.2f}%")
print(f"Taxa de reprovação: {taxa_reprovacao:.2f}%")
print(f"Taxa de não executados: {taxa_nao_executados:.2f}%")

# Edilson: Finaliza os cálculos das métricas.

print("")
print("=" * 45)
print("CÁLCULOS CONCLUÍDOS")
print("=" * 45)
