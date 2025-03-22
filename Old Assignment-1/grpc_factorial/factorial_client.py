import grpc
import factorial_pb2
import factorial_pb2_grpc

def run():
    # Connect to gRPC server
    channel = grpc.insecure_channel("localhost:50051")
    stub = factorial_pb2_grpc.FactorialServiceStub(channel)

    # Get user input
    n = int(input("Enter a non-negative integer: "))

    # Create request and call server method
    request = factorial_pb2.FactorialRequest(n=n)
    response = stub.Calculate(request)

    # Display result
    print(f"Factorial of {n} is: {response.factorial}")

if __name__ == "__main__":
    run()