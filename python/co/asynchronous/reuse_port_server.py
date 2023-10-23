import asyncio
import functools
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing import Process

import hiredis
import uvloop
from hiredis import ProtocolError

process_pool_executor = ThreadPoolExecutor(max_workers=10)


# 共享端口多进程方案 每个进程中启动一个事件循环
# @see Redis的通信协议 https://blog.csdn.net/lt326030434/article/details/128150427
# @see Benchmark asyncio vs gevent vs native epoll h
# ttps://dev.to/skywind3000/performance-asyncio-vs-gevent-vs-native-epoll-bnl
# @see asyncio python3协程版本  https://blog.csdn.net/cwdelphi/article/details/115195002

def redis_reply_string(msg: str):
    b = b"+"
    b += msg.encode()
    b += b"\r\n"
    return b


# "空字符串"
def redis_reply_empty():
    return b'$0\r\n\r\n'


def process(req):
    cmd = req[0].lower()
    if cmd == b'set':
        return b"+OK\r\n"
    elif cmd == b'get':
        v = req[1]
        if v is None:
            return b'$-1\r\n'
        else:
            # 调用推理
            req_str = v
            if type(v) == bytes:
                req_str = v.decode()
            print(req_str)
            msg = redis_reply_string(req_str)
            return msg
    elif cmd == b'ping':
        return b"+PONG\r\n"
    elif cmd == b'config':
        return b'-ERROR\r\n'
    elif cmd == b'command':
        return b"+OK\r\n"
    else:
        return b'-ERROR\r\n'
    return b''


async def echo_server(reader, writer):
    loop = asyncio.get_event_loop()
    hi_reader = hiredis.Reader()
    try:
        while True:
            s = await reader.read(4096)
            if not s:
                break
            hi_reader.feed(s)
            while True:
                try:
                    req = hi_reader.gets()
                except ProtocolError:
                    req = False
                if not req:
                    break
                res = await loop.run_in_executor(process_pool_executor, functools.partial(process, req))
                writer.write(res)
                await writer.drain()
    except ConnectionResetError or Exception:
        pass
    writer.close()
    return 0


async def main_process():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    server = await asyncio.start_server(echo_server, '0.0.0.0', 5001, reuse_port=True)
    print('serving on {}'.format(server.sockets[0].getsockname()))
    await server.serve_forever()
    server.close()
    return 0


def server_run():
    asyncio.run(main_process())


def main() -> None:
    for _ in range(3):
        worker = Process(target=server_run)
        worker.start()
    server_run()


if __name__ == '__main__':
    main()
