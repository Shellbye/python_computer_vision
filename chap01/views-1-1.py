# -*- coding:utf-8 -*-
# Created by shellbye on 2016/12/27.


from PIL import Image


def grey(src_path, des_path):
    pil_im = Image.open(src_path).convert('L')
    pil_im.save(des_path)


def thumbnail(src_path, des_path, size_tuple):
    pil_im = Image.open(src_path)
    pil_im.thumbnail(size_tuple)
    pil_im.save(des_path)


def crop_paste(src_path, des_path, box_tuple):
    # 四元组的坐标依次是(左，上，右，下)。PIL 中指定 坐标系的左上角坐标为(0，0)
    pil_im = Image.open(src_path)
    region = pil_im.crop(box_tuple)
    region.save('../pic/region.jpg')
    region = region.transpose(Image.ROTATE_180)
    pil_im.paste(region, box_tuple)
    pil_im.save(des_path)


def resize(src_path, des_path, size_tuple):
    pil_im = Image.open(src_path)
    pil_im_resized = pil_im.resize(size_tuple)
    pil_im_resized.save(des_path)


def rotate(src_path, des_path, degree):
    pil_im = Image.open(src_path)
    pil_im_rotated = pil_im.rotate(degree)
    pil_im_rotated.save(des_path)

if __name__ == '__main__':
    empire = '../pic/empire.jpg'
    # grey(empire, '../pic/empire_grey.jpg')
    # thumbnail(empire, '../pic/empire_thumb.jpg', (128, 128))
    # crop_paste(empire, '../pic/empire_crop_paste.jpg',
    #            (100, 100, 400, 400))
    # resize(empire, '../pic/empire_resize.jpg', (50, 50))
    rotate(empire, '../pic/empire_rotate.jpg', 180)
    pass
