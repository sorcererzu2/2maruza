#!/usr/bin/env bash
# gen.sh — talaba.proto dan Python kodini generatsiya qiladi.
# Natija: talaba_pb2.py (xabarlar) va talaba_pb2_grpc.py (server va mijoz qismi)
set -e
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. talaba.proto
ls -1 talaba_pb2*.py
