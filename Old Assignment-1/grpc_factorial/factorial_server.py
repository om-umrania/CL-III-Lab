import grpc
from concurrent import futures
import time

import factorial_pb2
import factorial_pb2_grpc

# Create the service class
class FactorialServicer(factorial_pb2_grpc.FactorialServiceServicer):
    def Calculate(self, request, context):
        n = request.n
        factorial = 1
        if n < 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "n must be non-negative")
        for i in range(2, n + 1):
            factorial *= i
        return factorial_pb2.FactorialResponse(factorial=factorial)

# Start gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    factorial_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("🟢 gRPC Server is running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()