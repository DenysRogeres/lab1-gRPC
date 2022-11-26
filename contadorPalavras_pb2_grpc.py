# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import contadorPalavras_pb2 as contadorPalavras__pb2


class ContadorPalavrasStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CalcularQuantidade = channel.unary_unary(
                '/palavras.ContadorPalavras/CalcularQuantidade',
                request_serializer=contadorPalavras__pb2.ListaPalavras.SerializeToString,
                response_deserializer=contadorPalavras__pb2.QtdPalavras.FromString,
                )
        self.VerificarPalavras = channel.unary_stream(
                '/palavras.ContadorPalavras/VerificarPalavras',
                request_serializer=contadorPalavras__pb2.ListaPalavras.SerializeToString,
                response_deserializer=contadorPalavras__pb2.PalavraVerificada.FromString,
                )


class ContadorPalavrasServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CalcularQuantidade(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerificarPalavras(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContadorPalavrasServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CalcularQuantidade': grpc.unary_unary_rpc_method_handler(
                    servicer.CalcularQuantidade,
                    request_deserializer=contadorPalavras__pb2.ListaPalavras.FromString,
                    response_serializer=contadorPalavras__pb2.QtdPalavras.SerializeToString,
            ),
            'VerificarPalavras': grpc.unary_stream_rpc_method_handler(
                    servicer.VerificarPalavras,
                    request_deserializer=contadorPalavras__pb2.ListaPalavras.FromString,
                    response_serializer=contadorPalavras__pb2.PalavraVerificada.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'palavras.ContadorPalavras', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ContadorPalavras(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CalcularQuantidade(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/palavras.ContadorPalavras/CalcularQuantidade',
            contadorPalavras__pb2.ListaPalavras.SerializeToString,
            contadorPalavras__pb2.QtdPalavras.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerificarPalavras(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/palavras.ContadorPalavras/VerificarPalavras',
            contadorPalavras__pb2.ListaPalavras.SerializeToString,
            contadorPalavras__pb2.PalavraVerificada.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
