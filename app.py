from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/velas')
def velas():
    return jsonify([
        {"rodada": "2280001", "vela": "2.45", "horario": "12:01:02", "data": "2025-04-20"},
        {"rodada": "2280002", "vela": "1.97", "horario": "12:02:30", "data": "2025-04-20"}
    ])

@app.route('/api/analises/sem_vela_rosa_resultado')
def analise_rosa():
    return jsonify({
        "ultima_rosa": {"vela": "12.00", "horario": "11:59:02"},
        "media_minutos_entre_rosas": "15.3 min",
        "tempo_desde_ultima_rosa": "18.7 min",
        "tempo_desde_ultima_100x": {
            "ultima": {"valor": "112.3", "horario": "10:32:11"},
            "descricao": "faz 2h que não sai uma vela de 100x"
        },
        "velas_por_horario": {
            "09 - 10": {"azul": 12, "roxa": 5, "rosa": 1},
            "10 - 11": {"azul": 11, "roxa": 8, "rosa": 2},
            "11 - 12": {"azul": 7, "roxa": 9, "rosa": 3}
        }
    })

@app.route('/api/analises/bot_analista_minuto_ciclo')
def analise_ciclo():
    return jsonify({
        "ciclos": [
            {"horario_ciclo": "12:10:00", "vela": "2.53"},
            {"horario_ciclo": "11:58:00", "vela": "2.10"}
        ],
        "sinais": [
            {"tipo": "sinal", "vela_detectada": "1.00", "horario_previsto": "12:22", "teto_min_estimado": 8, "teto_max_estimado": 12}
        ]
    })

if __name__ == '__main__':
    app.run()
