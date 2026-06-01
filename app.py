from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Simulando um banco de dados na memória
historico_tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Arrow Functions em JS",
        "categoria": "Estudos",
        "status": "concluida",
        "data": "2026-05-28",
        "duracao_minutos": 25
    }, # <-- Vírgula separando os dicionários na lista
    {
        "id": 2,
        "titulo": "Criar layout do TaskFlow",
        "categoria": "Design",
        "status": "Concluída", # <-- Corrigido de 'stauts' para 'status'
        "data": "2026-05-29",
        "duracao_minutos": 50
    }
]

# Rota padrão para testar se o servidor está online
@app.route('/', methods=['GET']) # <-- Corrigido de list_methods para methods
def home():
    return jsonify({"status": "Servidor rodando e pronto para o TaskFlow!"})

# Rota para buscar todas as tarefas
@app.route('/api/tarefas', methods=['GET'])
def obter_tarefas():
    return jsonify(historico_tarefas)

# Rota de Insights (Movida para antes do inicializador do app)
@app.route('/api/insights', methods=['GET'])
def ler_lista():
    # Passo 1: Inicializa o contador de minutos
    total_minutos = 0

    # Passo 2: Conta a quantidade de itens na lista (Armazenado na variável correta)
    total_tarefas = len(historico_tarefas)

    # Passo 3: Laço de Repetição para somar os minutos (Na mesma linha)
    for tarefa in historico_tarefas:
        total_minutos = total_minutos + tarefa["duracao_minutos"]

    # Passo 4: Devolver a resposta empacotada em JSON
    return jsonify({
        "quantidade_tarefas_concluidas": total_tarefas,
        "minutos_totais_focados": total_minutos,
        "mensagem": "Excelente trabalho! Continue no foco."
    })

if __name__ == '__main__':
    app.run(debug=True)