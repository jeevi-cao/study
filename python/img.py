import requests

host = "http://10.126.160.14:8088/v1/image/process"

imgs = ["/home/caojianwei/img/a.jpg", "/home/caojianwei/img/b.jpg", "/home/caojianwei/img/c.jpg"]
cmds = ["resize,m_fixed,w_123,h_75/format,f_png", "crop,m_center,w_400,h_300/resize,m_lfit,w_200,h_150/format,f_avif",
        "info", "crop,m_center,w_400,h_300/resize,m_lfit,w_200,h_150/format,f_avif/limit,l_1000000"]


def post_file(img, cmd):
    try:
        files = {'file': open(img, 'rb')}
        values = {'x-image-process': cmd}
        res = requests.post(host, files=files, data=values)
        print(res)
    except:
        pass


while True:
    for img in imgs:
        for cmd in cmds:
            post_file(img, cmd)
