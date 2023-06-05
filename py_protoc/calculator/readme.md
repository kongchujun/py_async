# how to install grpc in python 
```
pip install grpcio
pip install grpcio-tools
```

# how to generate code
```
protoc --python_out=. calculator.proto
$ python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. calculator.proto
```

