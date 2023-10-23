import asyncio
import functools
import queue
import socket
import uvloop
from multiprocessing import Process, Queue
import hiredis

'''
 asyncio 基于多进程版本server 主进程接受请求 将请求连接放入Queue供子进程处理链接
'''

d = {}


def process(req):
    cmd = req[0].lower()
    if cmd == b'set':
        d[req[1]] = req[2]
        return b"+OK\r\n"
    elif cmd == b'get':
        v = d.get(req[1])
        if v is None:
            return b'$-1\r\n'
        else:
            return b'$1\r\n1\r\n'
    elif cmd == b'config':
        return b'-ERROR\r\n'
    else:
        return b'-ERROR\r\n'
    return b''


async def handle_conn(reader, writer):
    h_reader = hiredis.Reader()
    while True:
        data = await reader.read(4096)
        if not data:
            print("close")
            break
        h_reader.feed(data)
        while True:
            req = h_reader.gets()
            if not req:
                print(req)
                break
            res = process(req)
            writer.write(res)
            await writer.drain()
    print("-----------")
    writer.close()


async def process_conn(conn: socket) -> None:
    # reader, writer = await asyncio.open_unix_connection()
    reader, writer = await asyncio.open_connection(sock=conn)
    await handle_conn(reader, writer)


async def main_process_async(q: Queue):
    loop = asyncio.get_running_loop()
    while True:
        try:
            conn, addr = await loop.run_in_executor(None, functools.partial(q.get, timeout=1))
            print(conn, addr)
            await process_conn(conn)
        except queue.Empty:
            pass


def main_process(q: Queue) -> None:
    loop = asyncio.get_event_loop()
    loop.create_task(main_process_async(q))
    loop.run_forever()
    print("over")


async def server(loop, q):
    server_ip = "0.0.0.0"
    server_port = 8085
    count = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((server_ip, server_port))
        server_socket.listen(128)
        server_socket.setblocking(False)
        while True:
            conn, addr = await loop.sock_accept(server_socket)
            q.put((conn, addr))
            count += 1
            print("conn", count)


def main() -> None:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    q = Queue(maxsize=1000)
    for _ in range(4):
        worker = Process(target=main_process, args=(q,))
        worker.start()
    loop = asyncio.get_event_loop()
    loop.create_task(server(loop, q))
    loop.run_forever()


if __name__ == '__main__':
    main()
