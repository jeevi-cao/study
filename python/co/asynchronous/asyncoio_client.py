import asyncio

if __name__ == '__main__':

    def redis_send_proto_get(msg: str):
        # 3\r\n$3\r\nSET\r\n$3\r\nkey\r\n$5\r\nvalue\r\n
        b = b"*2\r\n$3\r\nGET\r\n"
        rt = msg.encode()
        ll = len(rt)
        l_s = "${}".format(ll)
        b += l_s.encode()
        b += b"\r\n"
        b += rt
        b += b"\r\n"
        return b


    async def tcp_echo_client(message):
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 5001)

        print(f'Send: {message!r}')
        print(redis_send_proto_get(message))
        writer.write(redis_send_proto_get(message))
        await writer.drain()

        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')

        writer.close()
        await writer.wait_closed()


    asyncio.run(tcp_echo_client("aaa"))
    asyncio.run(tcp_echo_client("bbb"))