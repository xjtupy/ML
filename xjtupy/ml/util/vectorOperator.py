#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/1/9 21:51
# @Author: peng yang
# @File  : vectorOperator.py
import numpy as np

"""
向量运算
"""


class VectorOperator(object):

    @staticmethod
    def distance(v, w):
        """两点的距离"""
        return np.math.sqrt(VectorOperator.squared_distance(v, w))

    @staticmethod
    def squared_distance(v, w):
        """
        两点之间的欧式距离
        """
        return np.dot(np.array(v) - np.array(w), np.array(v) - np.array(w))
