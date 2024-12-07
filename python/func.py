def enroll(name, sex=6, city='BeiJing'):
    print("name:", name)
    print('sex:', sex)
    print('city:', city)
    return None


enroll('caojianwei', city='shanghai')


def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n
    return sum


sum = calc(1, 2, 3, 4, 5, 6)

print(sum)


def person(name, age, **kw):
    print(kw)


print(person('aaa', 10))

import hashlib


def get_md5_sha256(input_string):
    input_string = input_string.upper()
    # 计算MD5哈希值
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    md5_digest = md5_hash.hexdigest()

    # 计算SHA256哈希值
    sha256_hash = hashlib.sha256()
    sha256_hash.update(md5_digest.encode('utf-8'))
    sha256_digest = sha256_hash.hexdigest()

    return md5_digest, sha256_digest






if __name__ == '__main__':
    # 使用示例
    input_string = '411322199108095432x'.upper()
    md5, sha256 = get_md5_sha256(input_string)
    print(sha256 == "b516a75694a61ad4f6857aba198f84eb5f4721fedd6ae8bd814c790dcfea75e3")
    print(f'MD5: {md5}')
    print(f'SHA256: {sha256}')