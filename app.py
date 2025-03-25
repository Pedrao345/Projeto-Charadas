from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {'id': 1, 'charada': 'Qual é a diferença entre a panela e o penico?', 'reposta': 'Se você não sabe, nunca me convide para almoçar na sua casa.'},
    {'id': 2, 'charada': 'Qual é a diferença entre a sogra e a cobra?', 'reposta': ' As cobras não tem tantas rugas.'},
    {'id': 3, 'charada': 'Qual o próximo número na sequência: 2, 10, 12, 16, 17, 18, 19, ...?', 'reposta': '200. Todos os números começam com a letra D.'},
    {'id': 4, 'charada': 'Quais são os três números, nenhum dos quais é zero, que dão o mesmo resultado, quer sejam somados ou multiplicados?', 'reposta': '1, 2 e 3. Pois 1 + 2 + 3 = 6 e 1 x 2 x 3 = 6.'},
    {'id': 5, 'charada': 'Por que existem camas elásticas no Pólo Norte?', 'reposta': 'Para o urso polar.'},
    {'id': 6, 'charada': 'O que dá a mistura de uma pulga com a letra A?', 'reposta': 'Um assaltante.'},
    {'id': 7, 'charada': 'Como se fala policial em japonês?', 'reposta': 'Takatiro.'},
    {'id': 8, 'charada': 'O que é um pontinho verde em uma noiva?', 'reposta': 'Greenalda.'},
    {'id': 9, 'charada': 'Qual é a panela que você usa quando está triste?', 'reposta': 'De-pressão.'},
    {'id': 10, 'charada': 'O que é inteiro mas tem nome de metade?', 'reposta': 'Meia.'},
]

@app.route('/')
def index():
    return 'CharadAPI tá ON! Ria!', 200

@app.route('/charadas', methods=['GET'])
def charada():
    id_aleatorio = random.randint(0,10)
    charada_aleatoria = charadas[id_aleatorio]
    return jsonify(charada_aleatoria), 200
    

if __name__ == '__main__':
    app.run()