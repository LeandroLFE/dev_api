from flask_restful import Resource, request
import json

lista_habilidades=['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        nova_habilidade = json.loads(request.data)
        tamanho_atual = len(lista_habilidades)
        tamanho_add = len(nova_habilidade)
        permissao_add = True
        hab = ""

        for i in range(tamanho_atual):
            for j in range(tamanho_add):
                if lista_habilidades[i] == nova_habilidade[j]:
                    permissao_add = False
                    hab = lista_habilidades[i]

        if permissao_add:
            lista_habilidades.extend(nova_habilidade)
            return nova_habilidade
        else:
            retorno = {
                'status': 'erro',
                'mensagem': 'Habilidade {} já existente na lista'.format(hab)
            }
            return retorno

class Habilidade(Resource):
    def put(self, id):
        try:
            hab_alterada = json.loads(request.data)
            lista_habilidades[id] = hab_alterada
            retorno ={
                'status':'sucesso',
                'mensagem': hab_alterada
            }
            return retorno

        except IndexError:
            retorno = {
                'status': 'erro',
                'mensagem':'índice invalido'
            }
            return retorno
        except Exception:
            retorno = {
                'status': 'erro',
                'mensagem': 'Erro desconhecido, contate o administrador da API'
            }
            return retorno

    def delete(self, id):
        try:
            lista_habilidades.pop(id)
            retorno = {
                'status': 'sucesso',
                'mensagem': "Habilidade da posição {} excluída.".format(id)
            }
            return retorno

        except IndexError:
           retorno = {
                'status': 'erro',
                'mensagem': 'índice invalido'
            }
           return retorno

        except Exception:
            retorno = {
                'status': 'erro',
                'mensagem': 'Erro desconhecido, contate o administrador da API'
            }
            return retorno




