
import json
import os


# with open('./image/image.json') as jf:
#     im = json.load(jf)
#
# image2 = './image/need_fix.json'
# imn = {}

# print(len(im))
# for id in im:
#     if im[id]['i1_psnr'] < 30.00 or im[id]['14_psnr'] < 30 or im[id]['14_i1_psnr'] < 30:
#         print(json.dumps(im[id], indent=4, ensure_ascii=False))
#         imn[id] = im[id]
#
# print(len(imn))
#
# with open(image2, 'w') as f:
#     f.write(json.dumps(imn, indent=4, ensure_ascii=False))


with open('./image/image_80.json') as jf:
    im = json.load(jf)

i1len = 0
for id in im:
    i1len += im[id]['o_len']

s = "平均长度:{}".format(i1len/len(im))
print(s)