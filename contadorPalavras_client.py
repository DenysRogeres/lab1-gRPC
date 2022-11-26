import grpc
import string
import contadorPalavras_pb2
import contadorPalavras_pb2_grpc

def run():
    texto = open("arquivo.txt")
    lista = []
    
    for linha in texto:
        linha = linha.strip()
        linha = linha.translate(linha.maketrans("", "", string.punctuation))
        palavras = linha.split(" ")
        
        for palavra in palavras:
            lista.append(palavra)
            
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = contadorPalavras_pb2_grpc.ContadorPalavrasStub(channel)
        
        request = contadorPalavras_pb2.ListaPalavras(palavras=lista)
        response = stub.CalcularQuantidade(request)
        print(f"Quantidade de palavras totais : {response.quantidadePalavras}\n" )
        
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = contadorPalavras_pb2_grpc.ContadorPalavrasStub(channel)
        
        request = contadorPalavras_pb2.ListaPalavras(palavras=lista)
        response = stub.VerificarPalavras(request)
        
        for res in response: 
            if res.quantidade == 1:
                print(f"A palavra '{res.palavra}' apareceu {res.quantidade} vez")
            else:
                print(f"A palavra '{res.palavra}' apareceu {res.quantidade} vezes")
        
if __name__ == "__main__":
    run()