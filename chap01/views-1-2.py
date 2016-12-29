# -*- coding:utf-8 -*-
# Created by shellbye on 2016/12/29.
from PIL import Image
from pylab import array, imshow, show, title, figure
from pylab import contour, axis, gray, hist, ginput
# 在 PyLab 库中，我们约定图像的左上角为坐标原点


def plot():
    # 读取图像到数组中
    im = array(Image.open('../pic/empire.jpg'))
    # 绘制图像
    imshow(im)

    # 一些点: 四个点，第一行是这些点的横坐标，第二行是纵坐标
    x = [100, 100, 400, 400]
    y = [200, 500, 200, 500]

    # 使用红色星状标记绘制点
    plot(x, y, 'r*')
    # plot(x,y)         默认为蓝色实线
    # plot(x,y,'r*')    红色星状标记
    # plot(x,y,'go-')   带有圆圈标记的绿线
    # plot(x,y,'ks:')   带有正方形标记的黑色虚线

    # 基本颜色
    # 'b' 蓝色 'g' 绿色 'r' 红色 'c' 青色 'm' 品红 'y' 黄色 'k' 黑色 'w' 白色

    # 基本线
    # '-' 实线 '--' 虚线 ':' 点线

    # 基本绘制标记
    # '.' 点 'o' 圆圈 's' 正方形 '*' 星形 '+' 加号 'x' 叉号

    # 绘制连接前两个点的线
    plot(x[:2], y[:2])

    # 添加标题，显示绘制的图像
    title('Plotting: "empire.jpg"')

    # 不显示坐标轴
    # axis('off')
    show()


def my_contour(src_path):
    # 这里将原图进行了灰度化（0-255）
    im = array(Image.open(src_path).convert('L'))
    # 新建一个图像
    figure()
    # 不使用颜色信息，这里是将最终展示的图片信息中的颜色信息屏蔽掉
    gray()
    # 在原点的左上角显示轮廓图像
    contour(im, origin='image')
    # todo 为什么这里需要一个 equal
    axis('equal')
    # axis('off')
    show()


def my_hist(src_path):
    im = array(Image.open(src_path).convert('L'))
    figure()
    # 因为 hist() 只接受一 维数组作为输入，所以我们在绘制图像直方图之前，
    # 必须先对图像进行压平处理。
    # flatten() 方法将任意数组按照行优先准则转换成一维数组
    hist(im.flatten(), 128)
    show()


def interactive_mark(src_path):
    im = array(Image.open(src_path))
    imshow(im)
    print 'Please click 3 points'
    x = ginput(3)
    print 'you clicked:', x
    show()


if __name__ == '__main__':
    empire = '../pic/empire.jpg'
    # plot()
    # my_contour(empire)
    # my_hist(empire)
    interactive_mark(empire)
    pass
