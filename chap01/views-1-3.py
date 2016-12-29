# -*- coding:utf-8 -*-
# Created by shellbye on 2016/12/29.
from PIL import Image
from pylab import array, imshow, show


def display(src):
    im = array(Image.open(src))
    print im.shape, im.dtype  # 无符号八位整数 uint8
    im = array(Image.open(src).convert('L'), 'f')
    print im.shape, im.dtype


def grey_op(src):
    im = array(Image.open(src).convert('L'))
    # im = array(Image.open(src))
    # 因为上面用到了 convert('L'),
    # 所以下面的 imshow 和 show 就没有展示正确的图像
    # imshow(im)  # Display an image on the axes.
    # show()  # Display a figure.
    im2 = 255 - im  # 对图像进行反相处理
    im3 = (100.0 / 255) * im + 100  # 将图像像素值变换到 100...200 区间
    im4 = 255.0 * (im / 255.0) ** 2  # 对图像像素值求平方后得到的图像
    Image.fromarray(im2).save("im2.jpg")
    Image.fromarray(im3).save("im3.jpg")
    Image.fromarray(im4).save("im4.jpg")


if __name__ == '__main__':
    empire = '../pic/empire.jpg'
    # display(empire)
    grey_op(empire)
    pass
