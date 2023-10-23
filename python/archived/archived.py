# encode=utf-8
import os
import subprocess


def tar_gz(path, file_name):
    subprocess.call(['tar', "-czf", file_name, path])


if __name__ == '__main__':
    path = "/Users/jeevi/Desktop/video/1-50/51-100/"
    children_path = os.listdir(path)
    is_dir = False
    for cp in children_path:
        # 判断是否全部是文件
        is_dir = os.path.isdir(path + "/" + cp)
        if is_dir and cp[0] != ".":
            os.chdir(path)
            print("compress file:{} dir:{}".format(cp + ".tar.gz", path + "/" + cp))
            tar_gz(cp, cp + ".tar.gz")

print("done")
