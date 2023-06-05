import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
client = calculator_pb2_grpc.CalculatorStub(channel)

add_request = calculator_pb2.AddRequest(x=5, y=3)
add_response = client.Add(add_request)
print("Addition result:", add_response.result)

subtract_request = calculator_pb2.SubtractRequest(x=10, y=4)
subtract_response = client.Subtract(subtract_request)
print("Subtraction result:", subtract_response.result)
