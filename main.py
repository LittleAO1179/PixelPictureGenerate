from PIL import Image
import numpy as np
import json
import sys

def progress(image :np.array) -> np.array:
    config = json.load(open("config.json", "r"))
    """ 转换成像素画 """
    # 0. 降低分辨率
    image = image[::config['zoom_size'], ::config['zoom_size']]
    # 1. 分离出RGB三个通道
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    # 2. 将每个通道的值转换成二进制，然后将末位变成0
    red = red >> config['level'] << config['level']
    green = green >> config['level'] << config['level']
    blue = blue >> config['level'] << config['level']
    # 3. 将三个通道合并
    res = np.zeros_like(image)
    res[:, :, 0] = red
    res[:, :, 1] = green
    res[:, :, 2] = blue
    # 4. 将分辨率放大
    res = np.repeat(np.repeat(res, config['zoom_size'], axis=0), config['zoom_size'], axis=1)
    return res

if __name__ == "__main__":
    try:
        image = Image.open(sys.argv[1])
    except:
        print("Usage: python main.py <input> <output>")
        exit(0)
    image = np.array(image)
    res = progress(image)
    res = Image.fromarray(res)
    res.save(sys.argv[2])
