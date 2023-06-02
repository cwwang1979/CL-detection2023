# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zhanghongyuan2017@email.szu.edu.cn

import os
import shutil
import numpy as np
from PIL import Image
import SimpleITK as sitk


def load_train_stack_data(file_path: str) -> np.ndarray:
    """
    function to load train_stack.mha data file | 加载train_stack.mha数据文件的函数
    :param file_path: train_stack.mha filepath | 挑战赛提供的train_stack.mha文件路径
    :return: a 4-dim array containing 400 training set cephalometric images | 一个包含了400张训练集头影图像的四维的矩阵
    """
    sitk_stack_image = sitk.ReadImage(file_path)
    np_stack_array = sitk.GetArrayFromImage(sitk_stack_image)
    return np_stack_array


def remove_zero_padding(image_array: np.ndarray) -> np.ndarray:
    """
    function to remove zero padding in an image | 去除图像中的0填充函数
    :param image_array: one cephalometric image array, shape is (2400, 2880, 3) | 一张头影图像的矩阵，形状为(2400, 2880, 3)
    :return: image matrix after removing zero padding | 去除零填充部分的图像矩阵
    """
    row = np.sum(image_array, axis=(1, 2))
    column = np.sum(image_array, axis=(0, 2))

    non_zero_row_indices = np.argwhere(row != 0)
    non_zero_column_indices = np.argwhere(column != 0)

    last_row = int(non_zero_row_indices[-1])
    last_column = int(non_zero_column_indices[-1])

    image_array = image_array[:last_row+1, :last_column+1, :]
    return image_array


def check_and_make_dir(dir_path):
    if os.path.exists(dir_path):
        if os.path.isfile(dir_path):
            raise ValueError('Error, the provided path (%s) is a file path, not a folder path.' % dir_path)
        shutil.rmtree(dir_path, ignore_errors=False, onerror=None)
        os.makedirs(dir_path)
    else:
        os.makedirs(dir_path)


if __name__ == '__main__':
    # load the train_stack.mha data file using SimpleITK package
    # 使用SimpleITk库加载提供的train_stack.mha数据文件
    mha_file_path = './train_stack.mha'
    train_stack_array = load_train_stack_data(mha_file_path)

    # check the dimension information of the matrix, theoretically it should be (400, 2400, 2880, 3)
    # the first dimension is the number of images,
    # the second and third dimensions are the width and height of the image filled with 0, respectively,
    # and the fourth dimension is the number of channels of the image
    # 查看一下矩阵的维度信息，理论上应该是(400, 2400, 2880, 3)
    # 第一个维度是图像的数量，第二和第三个维度分别为图像的填充0后的宽和高，第四个维度是图像的通道数
    print(np.shape(train_stack_array))

    # directly traverse all images and store them in BMP format
    # If the following for loop is executed, you can observe the saved bmp images,
    # and you can find that many pictures are filled with 0 for unified storage.
    # of course, you can also directly use this model for training and prediction
    # 直接遍历所有图像，以bmp格式存储下来
    # 如果下面这个for循环执行完后，你可以观察一下保存下来的PNG图像
    # 可以发现为了统一存储，许多图片都进行了填充0处理，当然，你也可以直接使用这个模型训练和预测
    save_dir_path = './unprocessed_images'
    check_and_make_dir(save_dir_path)
    for i in range(np.shape(train_stack_array)[0]):
        image_array = train_stack_array[i, :, :, :]
        pillow_image = Image.fromarray(image_array)
        pillow_image.save(os.path.join(save_dir_path, '%s.bmp' % i))

    # The function of the following script is to remove the redundant 0 padding problem,
    # which may slightly improve the performance of your model.
    # Don't worry, this operation will not affect the processing of the label points of the key points,
    # because the coordinates of the key points are all in the upper left corner as the reference system
    # 接下来的这段脚本的功能是去除多余的0填充问题，这或许可以稍微的提高你的模型性能。
    # 放心，这个操作不会影响到关键点的标注点的处理，因为关键点的坐标都是左上角为参考系的
    save_dir_path = './processed_images'
    check_and_make_dir(save_dir_path)
    for i in range(np.shape(train_stack_array)[0]):
        image_array = train_stack_array[i, :, :, :]
        image_array = remove_zero_padding(image_array)
        pillow_image = Image.fromarray(image_array)
        pillow_image.save(os.path.join(save_dir_path, '%s.bmp' % i))
