from flask import Flask, request
from flask_restful import Api, Resource
from habilidades import Habilidades, Habilidade

import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':0,
        'nome': 'Rafael',
        'habilidades':['Python', 'Flask']
    },
    {
        'id':1,
        'nome': 'Leandro',
        'habilidades':['Python', 'VB']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {
                'status': 'erro', 'mensagem': mensagem
            }
        except Exception:
            mensagem = 'Erro desconhecido, contate o administrador da API'
            response = {
                'status': 'erro', 'mensagem': mensagem
            }
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {
            'status': 'sucesso',
            'mensagem': 'Registro excluido'
        }

class Lista_Desenvolvedores(Resource):
    def get(self):
       return desenvolvedores

    def post(self):
        novo_desenvolvedor = json.loads(request.data)
        posicao = len(desenvolvedores)
        novo_desenvolvedor["id"] = posicao
        desenvolvedores.append(novo_desenvolvedor)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidade, '/habilidades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)