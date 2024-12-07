
import hashlib
import csv
from datetime import datetime, timedelta


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

    return sha256_digest


if __name__ == '__main__':
    fixed = "11022320240226"
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["CertId"])

        for i in range(9999):
            cardId = fixed + "%05d" % i
            writer.writerow([get_md5_sha256(cardId)])

        date_string = "2024-02-25"
        for i in range(100):
            original_date = datetime.strptime(date_string, "%Y-%m-%d")
            new_date = original_date - timedelta(days=i)
            date_str = new_date.strftime("%Y%m%d")
            fixed = "110223" + date_str
            for i in range(9999):
                cardId = fixed + "%05d" % i
                writer.writerow([get_md5_sha256(cardId)])



