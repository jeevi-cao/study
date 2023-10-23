import hashlib

import requests
import time

if __name__ == '__main__':
    
    tx_url = "https://api.rta.qq.com/api/v1/target/bind/list"
    headers = {"RtaId": "4", "Content-Type": "application/json"}
    ts = str(int(time.time()))
    headers["Time"] = ts
    auth = "4f273b5e2b5c8f6cb" + ts
    headers["Authorization"] = hashlib.md5(bytes(auth.encode(encoding="utf-8"))).hexdigest()
    # OuterTargetId RTA_ID 从 clo 后台查询
    data = {"data": {"Size": 100, "Page": 1, "OuterTargetId": "3603004"}}

    count = 0
    total = 100
    while count < total:
        res = requests.post(tx_url, json=data, headers=headers)
        result = res.json()
        print(result)
        total = int(result["data"]["Total"])
        count += int(result["data"]["Size"])
        for record in result["data"]["Records"]:
            if record["Id"] in [29612479, 30195208, 30235654, 29612525]:
                print(record)

        data["data"]["Page"] += 1
