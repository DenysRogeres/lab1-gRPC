import grpc 
import contadorPalavras_pb2
import contadorPalavras_pb2_grpc
from concurrent import futures

class ContadorPalavrasServicer(contadorPalavras_pb2_grpc.ContadorPalavrasServicer):
    def CalcularQuantidade(self, request, context):
        tamanhoListaPalavras = len(request.palavras)
        return contadorPalavras_pb2.QtdPalavras(quantidadePalavras=tamanhoListaPalavras)
    
    def VerificarPalavras(self, request, context):
        dictPalavras = dict() 
        listaPalavras = request.palavras
        
        for palavra in listaPalavras:
            if palavra in dictPalavras:
                dictPalavras[palavra] = dictPalavras[palavra] + 1
            else:
                dictPalavras[palavra] = 1
        
        for key in list(dictPalavras.keys()):
            palavra_verificada = contadorPalavras_pb2.PalavraVerificada(palavra=key, quantidade=dictPalavras[key])
            yield palavra_verificada
        
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    contadorPalavras_pb2_grpc.add_ContadorPalavrasServicer_to_server(ContadorPalavrasServicer(), server)
    print('Server is running')
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()
    