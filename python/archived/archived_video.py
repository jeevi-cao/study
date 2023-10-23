# encode=utf-8
import os
import subprocess


def tar_gz(path, file_name):
    subprocess.call(['tar', "-czf", file_name, path])


def traverse_file(path, mv_path):
    path = path.rstrip("/")
    children_path = os.listdir(path)
    for cp in children_path:
        is_dir = os.path.isdir(path + "/" + cp)
        if is_dir and cp[0] not in (".", ".."):
            try:
                os.makedirs(mv_path + '/' + cp, mode=0O766)
            except:
                pass
            finally:
                pass
            traverse_file(path + "/" + cp, mv_path + '/' + cp)
        elif os.path.isfile(path + "/" + cp) and cp[0] not in (".", ".."):
            os.chdir(path + "/")
            print("compress file:{} dir:{}".format(cp + ".tar.gz", path + "/" + cp))
            filename = cp
            tar_gz(cp, filename + ".tar.gz")
            subprocess.call(['mv', filename + ".tar.gz", mv_path])
    return


if __name__ == '__main__':
    path = "/Users/jeevi/Desktop/video/101-150/"
    mv_path = "/Users/jeevi/Desktop/video/101-150.bak/"
    traverse_file(path, mv_path)

print("done")
