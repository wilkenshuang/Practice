# -*- coding: utf-8 -*-
"""
Created on 08/02/2017 16:14:58 

@author: wilkenshuang
"""

# coding=utf8
import math
import time
import matplotlib.pyplot as plt
import numpy as np

old_settings = np.seterr(all='ignore')

#定义节点类型
class KD_node:
    def __init__(self, point=None, split=None, left=None, right=None):
        '''

        :param point: 数据点的特征向量
        :param split: 切分的维度
        :param left: 左子类
        :param right: 右子类
        '''
        self.point = point
        self.split = split
        self.left = left
        self.right = right

def computeVariance(arrayList):
    '''

    :param arrayList: 所有数据某一维的向量
    :return: 返回
    '''
    for ele in arrayList:
        ele = float(ele)
    LEN = float(len(arrayList))
    array = np.array(arrayList)
    sum1 = float(array.sum())
    array2 = np.dot(array, array.T)
    sum2 = float(array2.sum())
    mean = sum1 / LEN
    variance = sum2 / LEN - mean ** 2
    return variance

def createKDTree(root, data_list):
    '''

    :param root: 输入一个根节点，以此建树
    :param data_list: 数据列表
    :return: 返回根节点
    '''
    LEN = len(data_list)
    if LEN == 0:
        return
        # 数据点的维度
    dimension = len(data_list[0]) - 1 #去掉了最后一维标签维
    # 方差
    max_var = 0
    # 最后选择的划分域
    split = 0
    for i in range(dimension):
        ll = []
        for t in data_list:
            ll.append(t[i])
        var = computeVariance(ll) #计算出在这一维的方差大小
        if var > max_var:
            max_var = var
            split = i
            # 根据划分域的数据对数据点进行排序
    data_list = list(data_list)
    data_list.sort(key=lambda x: x[split]) #按照在切分维度上的大小进行排序
    data_list = np.array(data_list)
    # 选择下标为len / 2的点作为分割点
    point = data_list[LEN / 2]
    root = KD_node(point, split)
    root.left = createKDTree(root.left, data_list[0:(LEN / 2)])#递归的对切分到左儿子和右儿子的数据再建树
    root.right = createKDTree(root.right, data_list[(LEN / 2 + 1):LEN])
    return root

def computeDist(pt1, pt2):
    '''

    :param pt1: 特征向量1
    :param pt2: 特征向量2
    :return: 两个向量的欧氏距离
    '''
    sum_dis = 0.0
    for i in range(len(pt1)):
        sum_dis += (pt1[i] - pt2[i]) ** 2
    #实现的欧氏距离计算，效率很低的版本，可以改成numpy的向量运算
    return math.sqrt(sum_dis)

def findNN(root, query):
    '''
    
    :param root: 建立好的KD树的树根
    :param query: 查询数据
    :return: 与这个数据最近的前三个节点
    '''
    # 初始化为root的节点
    NN = root.point
    min_dist = computeDist(query, NN)
    nodeList = []
    temp_root = root
    dist_list = [temp_root.point, None, None] #用来存储前三个节点
    ##二分查找建立路径
    while temp_root:
        nodeList.append(temp_root) #对向下走的路径进行压栈处理
        dd = computeDist(query, temp_root.point) #计算当前最近节点和查询点的距离大小
        if min_dist > dd:
            NN = temp_root.point
            min_dist = dd
            # 当前节点的划分域
        temp_split = temp_root.split
        if query[temp_split] <= temp_root.point[temp_split]:
            temp_root = temp_root.left
        else:
            temp_root = temp_root.right
            ##回溯查找
    while nodeList:
        back_point = nodeList.pop()
        back_split = back_point.split
        if dist_list[1] is None:
            dist_list[2] = dist_list[1]
            dist_list[1] = back_point.point
        elif dist_list[2] is None:
            dist_list[2] = back_point.point
        if abs(query[back_split] - back_point.point[back_split]) < min_dist: 
            #当查询点和回溯点的距离小于当前最小距离时，另一个区域有希望存在更近的节点
            #如果大于这个距离，可以理解为假设在二维空间上，直角三角形的直角边已经不满足要求了，那么斜边也一定不满足要求
            if query[back_split] < back_point.point[back_split]:
                temp_root = back_point.right
            else:
                temp_root = back_point.left
            if temp_root:
                nodeList.append(temp_root)
                curDist = computeDist(query, temp_root.point)
                if min_dist > curDist:
                    min_dist = curDist
                    dist_list[2] = dist_list[1]
                    dist_list[1] = dist_list[0]
                    dist_list[0] = temp_root.point
                elif dist_list[1] is None or curDist < computeDist(dist_list[1], query):
                    dist_list[2] = dist_list[1]
                    dist_list[1] = temp_root.point
                elif dist_list[2] is None or curDist < computeDist(dist_list[1], query):
                    dist_list[2] = temp_root.point
    return dist_list

def judge_if_normal(dist_list):
    '''
    
    :param dist_list: 利用findNN查找出的最近三个节点进行投票表决
    :return: 
    '''
    normal_times = 0
    except_times = 0
    for i in dist_list:
        if abs(i[-1] - 0.0) < 1e-7: #浮点数的比较
            normal_times += 1
        else:
            except_times += 1
    if normal_times > except_times: #判断是normal
        return True
    else:
        return False
    
def pre_data(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    lstall = []
    for line in lines:
        lstn = []
        lst = line.split(",")
        u = 0
        y = 0
        for i in range(0, 9):
            if lst[i].isdigit():
                lstn.append(float(lst[i]))
                u += 1
            else:
                pass
        for j in range(21, 31):
            try:
                lstn.append(float(lst[j]))
                y += 1
            except:
                pass
        if lst[len(lst) - 1] == "smurf.\n" or lst[len(lst) - 1] == "teardrop.\n":
            lstn.append(int("1"))
        else:
            lstn.append(int("0"))
        lstall.append(lstn)
    nplst = np.array(lstall, dtype=np.float16)
    return nplst

def my_test(all_train_data, all_test_data, train_data_num):
    train_data = all_train_data[:train_data_num]
    train_time_start = time.time()
    root = KD_node()
    root = createKDTree(root, train_data)
    train_time_end = time.time()
    train_time = train_time_end - train_time_start
    right = 0
    error = 0
    test_time_start = time.time()
    for i in range(len(all_test_data)):
        if judge_if_normal(findNN(root, all_test_data[i])) is True and abs(all_test_data[i][-1] - 0.0) < 1e-7:
            right += 1
        elif judge_if_normal(findNN(root, all_test_data[i])) is False and abs(all_test_data[i][-1] - 1.0) < 1e-7:
            right += 1
        else:
            error += 1
    test_time_end = time.time()
    test_time = test_time_end - test_time_start
    right_ratio = float(right) / (right + error)
    return right_ratio, train_time, test_time


def draw(train_num_list=[10, 100, 1000, 10000], train_data=[], test_data=[]):
    train_time_list = []
    test_time_list = []
    right_ratio_list = []
    for i in train_num_list:
        print 'start run ' + i.__str__()
        temp = my_test(train_data, test_data, i)
        right_ratio_list.append(temp[0])
        train_time_list.append(temp[1])
        test_time_list.append(temp[2])
    plt.title('train data num from ' + train_num_list[0].__str__() + ' to ' + train_num_list[:-1].__str__())
    plt.subplot(311)
    plt.plot(train_num_list, right_ratio_list, c='b')
    plt.xlabel('train data num')
    plt.ylabel('right ratio')
    plt.grid(True)
    plt.subplot(312)
    plt.plot(train_num_list, train_time_list, c='r')
    plt.xlabel('train data num')
    plt.ylabel('time of train data (s)')
    plt.grid(True)
    plt.subplot(313)
    plt.plot(train_num_list, test_time_list, c='g')
    plt.xlabel('train data num')
    plt.ylabel('time of test data (s)')
    plt.grid(True)
    plt.show()


data = pre_data('KDD-test\ddos+normal_70.txt')
data2 = pre_data('KDD-test\ddos+normal_30.txt')

draw(train_num_list=[10, 100, 500, 1000, 2000, 3000, 5000, 10000, 15000, 20000, 50000, 100000, 265300],
     train_data=data[:], test_data=data2[:])
