import asyncio
import functools
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

import hiredis
import random
import time
import datetime

"""
 主进程接受请求 业务处理部分放入进程池/线程池处理
"""

d = {}

process_pool_executor = ProcessPoolExecutor(max_workers=7)

#process_pool_executor = ThreadPoolExecutor(max_workers=50)


def process(req):
    r = random.randint(0, 5)
    time.sleep(r/1000)

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


async def echo_server(reader, writer):
    loop = asyncio.get_event_loop()
    hireader = hiredis.Reader()
    while True:
        s = await reader.read(4096)
        if not s:
            break
        hireader.feed(s)
        while True:
            req = hireader.gets()
            if not req:
                break
            t1 = datetime.datetime.now().timestamp() * 1000
            res = await loop.run_in_executor(process_pool_executor, functools.partial(process, req))
            t2 = datetime.datetime.now().timestamp() * 1000
            cost = (t2 - t1)
            if cost > 1:
                print(cost)
            writer.write(res)
            await writer.drain()
    return 0


async def main():
    server = await asyncio.start_server(echo_server, '0.0.0.0', 5001)
    print('serving on {}'.format(server.sockets[0].getsockname()))
    await server.serve_forever()
    return 0


if __name__ == '__main__':
    asyncio.run(main())
