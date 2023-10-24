from PIL import Image,ExifTags
import time
import pillow_avif
import HeifImagePlugin
from io import BytesIO
import  os

def convert_jpg_image(path, format='webp', quality=75):
    try:
        with Image.open(path) as im:
            im2 = im.resize(size=(580, 327), resample=Image.LANCZOS, box=(0, 0, 3968, 2237))
            im2.save("./covert/{}_{}.webp".format(path, time.time()), format, quality=quality)
    except OSError:
        print("cannot convert", path)


def convert_jpg_image2(path, format='webp', quality=75):
    try:
        with Image.open(path) as im:
            im2 = im.resize(size=(100, 100), resample=Image.LANCZOS, box=(100, 100, 500, 500))
            im2.save("./covert2/{}_{}.webp".format(path, time.time()), format, quality=quality)
    except OSError:
        print("cannot convert", path)


if __name__ == "__main__":
    # total = 0
    # i = 0
    # while i < 10:
    #     t = time.time()
    #     convert_jpg_image("./0Y.jpeg")
    #     t2 = time.time()
    #     cost = int(round(t2 * 1000)) - int(round(t * 1000))
    #     total += cost
    #     print("{} 耗时:{}ms\n".format(i, cost))
    #     i = i + 1
    # print("平均耗时:{}".format(total / 10))
    #
    # total = 0
    # i = 0
    # while i < 10:
    #     t = time.time()
    #     convert_jpg_image2("./0Y.jpeg")
    #     t2 = time.time()
    #     cost = int(round(t2 * 1000)) - int(round(t * 1000))
    #     total += cost
    #     print("2 {} 耗时:{}ms\n".format(i, cost))
    #     i = i + 1
    # print("2 平均耗时:{}".format(total / 10))
    t = time.time()
    # file = "./0YiucffB7q.gif"
    # try:
    #     with Image.open(file) as im:
    #         print(im.info)
    #         print(getattr(im, "is_animated", False))
    #         print(getattr(im, "n_frames", 1))
    #         im.save("./0YiucffB7q.gif.webp", "webp", quality=75, save_all=True)
    # except OSError:
    #     print("cannot convert")

    # t = time.time()
    # with Image.open(file) as im:
    #     print(im.format, im.size, im.mode)
    #     im2 = im.resize(size=(500, 250), resample=Image.LANCZOS, box=(0, 0, 4032, 2016))
    #     im2 = im2.convert(mode="RGB")
    #     im2.save("./0ZCwgItoXa.jpeg", "jpeg", quality=92)
    # t2 = time.time()
    # cost = int(round(t2 * 1000)) - int(round(t * 1000))
    # total += cost
    # print("1 {} 耗时:{}ms\n".format(i, cost))
    # i = i + 1


    # i = 0
    # total = 0
    # while i < 10:
    #     file = "./0ZH0CDQWvT.gif"
    #     try:
    #         t = time.time()
    #         with Image.open(file) as im:
    #             print(im.format, im.size, im.mode)
    #             im.seek(0)
    #             im2 = im.resize(size=(660, 402), resample=Image.LANCZOS, box=(0, 0, 1000, 609))
    #             im2 = im2.convert(mode="RGB")
    #             im2.save("./0ZH0CDQWvT.webp", "webp", quality=75)
    #         t2 = time.time()
    #         cost = int(round(t2 * 1000)) - int(round(t * 1000))
    #         total += cost
    #         print("1 {} 耗时:{}ms\n".format(i, cost))
    #         i = i + 1
    #     except OSError as e:
    #         print("cannot convert", e)
    # print("2 平均耗时:{}".format(total / 10))

    # file = "./bbbbb.heic"
    # try:
    #     t = time.time()
    #     with Image.open(file) as im:
    #         print(im.format, im.size, im.mode, getattr(im, "is_animated", False), getattr(im, "n_frames", 1))
    #         im.seek(0)
    #         # im2 = im.convert(mode="RGB")
    #         im.save("./bbbbb.3.webp", "webp", save_all=True)
    #     t2 = time.time()
    #     cost = int(round(t2 * 1000)) - int(round(t * 1000))
    #     print("耗时:{}ms\n".format(cost))
    # except OSError as e:
    #     print("cannot convert", e)

    # file = "./test/img/0ZpWvEaJyM.gif"
    #     # try:
    #     #     t = time.time()
    #     #     with Image.open(file) as im:
    #     #         print(im.format, im.size, im.mode, getattr(im, "is_animated", False), getattr(im, "n_frames", 1), getattr(im, "n_frames", 1)//2)
    #     #         im.seek(getattr(im, "n_frames", 1)//2)
    #     #         im2 = im.resize(size=(328, 240), resample=Image.LANCZOS, box=(94, 0, 545+94, 399), reducing_gap=2.0)
    #     #         im2 = im2.convert(mode="RGBA")
    #     #         bts = BytesIO()
    #     #         im2.save(bts, "avif", quality=75, method=6)
    #     #         print("长度:{} \n".format(len(bts.getvalue())))
    #     #         with open("0ZpWvEaJyM.gif.avif", "wb") as f:
    #     #             f.write(bts.getvalue())
    #     #     t2 = time.time()
    #     #     cost = int(round(t2 * 1000)) - int(round(t * 1000))
    #     #     print("耗时:{}ms\n".format(cost))
    #     # except OSError as e:
    #     #     print("cannot convert", e)

    # file = "./test/img/V_0ZbloHyE1v.png"
    # try:
    #     t = time.time()
    #     with Image.open(file) as im:
    #         print(im.format, im.size, im.mode, getattr(im, "is_animated", False), getattr(im, "n_frames", 1),
    #               getattr(im, "n_frames", 1) // 2)
    #
    #         im2 = im.resize(size=(960, 540), resample=Image.LANCZOS)
    #         #im2 = im2.convert(mode="RGBA")
    #         bts = BytesIO()
    #         im2.save(bts, "webp", quality=75, method=6)
    #         print("长度:{} \n".format(len(bts.getvalue())))
    #         with open("V_0ZbloHyE1v.png.webp", "wb") as f:
    #             f.write(bts.getvalue())
    #     t2 = time.time()
    #     cost = int(round(t2 * 1000)) - int(round(t * 1000))
    #     print("耗时:{}ms\n".format(cost))
    # except OSError as e:
    #     print("cannot convert", e)


    # file = "./test/img/0Zpa0dQvCZ.gif"
    # try:
    #     t = time.time()
    #     with Image.open(file) as im:
    #         print(im.format, im.size, im.mode, getattr(im, "is_animated", False), getattr(im, "n_frames", 1), getattr(im, "n_frames", 1)//2)
    #         im.seek(getattr(im, "n_frames", 1)//2)
    #         im2 = im.crop(box=(341, 0, 341 + 230, 150))
    #         #im2 = im.resize(size=(328, 240), resample=Image.LANCZOS, box=(94, 0, 545+94, 399), reducing_gap=2.0)
    #         im2 = im2.convert(mode="RGBA")
    #         bts = BytesIO()
    #         im2.save(bts, "webp", quality=75, method=6)
    #         print("长度:{} \n".format(len(bts.getvalue())))
    #         with open("0Zpa0dQvCZ.gif.webp", "wb") as f:
    #             f.write(bts.getvalue())
    #     t2 = time.time()
    #     cost = int(round(t2 * 1000)) - int(round(t * 1000))
    #     print("耗时:{}ms\n".format(cost))
    # except OSError as e:
    #     print("cannot convert", e)

    # file = "./YD_cnt_1_0176HrLau3tH.gif"
    #
    # with Image.open(file) as im:
    #     print(im.format, im.size, im.mode, getattr(im, "is_animated", False), getattr(im, "n_frames", 1),
    #           getattr(im, "n_frames", 1) // 2)
    #
    #     print(im.getbands(), im.info)
        # b = im.split()
        # print(im.split()[0])
        #
        # im1.show()

    # for root, dirs, files in os.walk("."):
    #     if len(files) > 0:
    #         for fl in files:
    #             file = "{}/{}".format(root, fl)
    #             try:
    #                 with Image.open(file) as im:
    #                     print(file, im.format, im.size, im.mode, getattr(im, "is_animated", False), getattr(im, "n_frames", 1),
    #                           getattr(im, "n_frames", 1) // 2)
    #             except Exception:
    #                 pass

    file = "./YD_cnt_11_019HNWhSb3SJ.gif"
    t = time.time()
    with Image.open(file) as im:
        print("info:", im.info)
        bts = BytesIO()
        background = im.info["background"]
        if isinstance(background, int) and im.getpalette() is None:
            if 0 <= background <= 255:
                im.info["background"] = (background, background, background, 0)

        im.save(bts, "webP", save_all=True, quality=75,  optimize=True)
        print("长度:{} \n".format(len(bts.getvalue())))
        with open("YD_cnt_11_019HNWhSb3SJ.gif.webP", "wb") as f:
            f.write(bts.getvalue())
        t2 = time.time()
        cost = int(round(t2 * 1000)) - int(round(t * 1000))
        print("耗时:{}ms\n".format(cost))
