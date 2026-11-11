# ETAPA 1 — INICIALIZAÇÃO DO PROJETO
# Squad 1: Fintech (Processamento de Pagamentos)

# Armazenamento das informações em variáveis utilizando o mock fornecido
projeto = "PayNext Fintech"
modulo = "Gateway de Pagamentos (Pix e Cartão)"
responsavel = "Mariana Silva"
data_execucao = "10/11/2026"
testes_aprovados = 48
testes_reprovados = 6
testes_nao_executados = 6

# Exibição organizada do relatório no terminal utilizando f-strings
print("=" * 40)
print("RELATÓRIO DE EXECUÇÃO DE TESTES")
print("=" * 40)
print(f"Projeto: {projeto}")
print(f"Módulo: {modulo}")
print(f"Responsável: {responsavel}")
print(f"Data da execução: {data_execucao}")
print("=" * 40)
print("INICIALIZAÇÃO CONCLUÍDA")
print("=" * 40)

# Apresenta os resultados dos testes executados.
print("")
print("=" * 45)
print("RESULTADOS REGISTRADOS")
print("=" * 45)

print(f"Testes aprovados: {testes_aprovados}")
print(f"Testes reprovados: {testes_reprovados}")
print(f"Testes não executados: {testes_nao_executados}")

# Finaliza o registro dos resultados.
print("")
print("=" * 45)
print("REGISTRO CONCLUÍDO")
print("=" * 45)

# Edilson: Calcula a quantidade total de testes.
total_testes = testes_aprovados + testes_reprovados + testes_nao_executados

# Edilson: Calcula a quantidade de testes executados.
testes_executados = testes_aprovados + testes_reprovados

# Edilson: Calcula as porcentagens dos testes.
taxa_aprovacao = (testes_aprovados / testes_executados) * 100
taxa_reprovacao = (testes_reprovados / testes_executados) * 100
taxa_nao_executados = (testes_nao_executados / total_testes) * 100

# Edilson: Exibe as métricas calculadas no terminal.
print("")
print("=" * 45)
print("MÉTRICAS DA EXECUÇÃO")
print("=" * 45)

print(f"Total de testes: {total_testes}")
print(f"Testes executados: {testes_executados}")
print("")
print(f"Taxa de aprovação: {taxa_aprovacao}%")
print(f"Taxa de reprovação: {taxa_reprovacao}%")
print(f"Taxa de não executados: {taxa_nao_executados}%")

# Edilson: Finaliza a apresentação das métricas.
print("")
print("=" * 45)
print("CÁLCULOS CONCLUÍDOS")
print("=" * 45)
