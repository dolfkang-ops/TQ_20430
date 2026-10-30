import struct

def get_image_info(data):
    w, h = 0, 0
    # simple jpeg dimension reader
    for i in range(len(data)-8):
        if data[i] == 0xFF and data[i+1] in [0xC0, 0xC1, 0xC2]:
            h, w = struct.unpack(">HH", data[i+5:i+9])
            break
    return w, h

import os
for f in os.listdir('images'):
    if f.endswith('.jpg'):
        with open(os.path.join('images', f), 'rb') as fp:
            w, h = get_image_info(fp.read())
            print(f"{f}: {w}x{h}")
