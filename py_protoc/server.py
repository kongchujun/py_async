import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.x + request.y
        return calculator_pb2.AddResponse(result=result)

    def Subtract(self, request, context):
        result = request.x - request.y
        return calculator_pb2.SubtractResponse(result=result)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
server.add_insecure_port("[::]:50051")
server.start()
print("Listening on port 50051...")
server.wait_for_termination()
