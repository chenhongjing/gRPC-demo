#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import Queue

import grpc
import schema_pb2
import schema_pb2_grpc

queue = Queue()


def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = schema_pb2_grpc.GatewayStub(channel)
        queue.put(1)
        resp = stub.Call(generate_message())
        for r in resp:
            num = r.num
            queue.put(num)


def generate_message():
    while True:
        num = queue.get()
        print(num)
        yield schema_pb2.Request(num=num)
        # yield schema_pb2.Request()


if __name__ == "__main__":
    main()