import requests
import csv


def get_doc_image_urls(doc_id: str):
    try:

        url = "https://a1.go2yd.com/Website/contents/content?docid="
        url = url + doc_id
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            if data["code"] == 0 and "documents" in data and len(data["documents"]) > 0:
                doc = data["documents"][0]
                if "image_urls" in doc and len(doc["image_urls"]) > 0:
                    return doc["image_urls"]
    finally:
        pass
    return None

def build_image_urls(doc_id, img_ids):
    i1 = "https://i1.go2yd.com/image.php?url="
    i1_perf = "https://i1-perf.go2yd.com/image.php?url="
    str1 = ""
    for id in img_ids:
        arr = []
        arr.append(doc_id)
        arr.append(i1 + id)
        arr.append(i1 + id + "&type=webp_219x146")
        arr.append(i1_perf + id + "&type=webp_219x146")
        arr.append(i1 + id + "&type=webp_960x540")
        arr.append(i1_perf + id + "&type=webp_960x540")
        arr.append(i1 + id + "&type=webp_326x240")
        arr.append(i1_perf + id + "&type=webp_326x240")
        str1 = str1 + ",".join(arr) + "\n"
    return str1


if __name__ == '__main__':
    header = ["doc_id", "原图", "原219x146", "优化219x146", "原960x540", "优化960x540", "原326x240", "优化326x240"]

    fc = open("url.csv", "w+", encoding='utf-8')

    fc.write(",".join(header) + "\n")

    with open("./docid.txt", "r") as f:
        for line in f.readlines():
            print(line)
            doc_id = line.strip()
            img_ids = get_doc_image_urls(doc_id)
            if img_ids is not None:
                str1 = build_image_urls(doc_id, img_ids)
                if len(str1) > 0:
                    fc.write(str1)

    fc.close()

