#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 17:39
# @Author  : wgPython
# @File    : posAdminAPI.py
# @Software: PyCharm
# @Desc    :
"""
对应的pos后台的接口
简单的模拟 就不分文件结构不连接数据库
"""
import json
import random

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 模拟数据  随机操作
FOODS = [["f1", "炸鸡翅", 10], ["f2", "牛肉汉堡", 5], ["f3", "鸡米花", 6], ["f4", "炸薯条", 7], ["f5", "蛋挞", 3], ["f6", "鸡肉卷", 6]]
DRINKS = [["d1", "可口可乐", 3], ['d2', "美年达", 2], ['d3', "雪碧", 2], ['d4', "奶茶", 3], ['d5', "咖啡", 3], ['d6', "牛奶", 4]]
MEAL = [['m1', "炸鸡全家桶", 45], ['m2', "汉堡全家桶", 55], ['m3', "大杂烩", 65]]


@app.route("/get/often/goods")
def get_often_goods():
    """
    获取常用商品 列表
    实际是随机模拟
    :return:
    """
    temp_list = []
    temp_list.extend(FOODS)
    temp_list.extend(DRINKS)
    temp_list.extend(MEAL)

    drinks = []
    for i in range(7):
        temp_data = dict()
        goods_info = random.choice(temp_list)
        temp_data["goodsId"] = goods_info[0]
        temp_data["goodsName"] = goods_info[1]
        temp_data["price"] = goods_info[2]
        drinks.append(temp_data)
    return jsonify(drinks)


@app.route("/get/goods")
def get_goods():
    args_data = request.values.get("param")

    # 获取的参数是str
    try:
        args_data = json.loads(args_data)
    except Exception as e:
        return jsonify({"code": 1, "error": e})

    # 这里是判断分类 如果是数据库里面的话  直接按条件查询 不用这么判断
    temp_food = []
    if args_data.get("cate") == "foods":
        temp_food = FOODS
    elif args_data.get("cate") == "drinks":
        temp_food = DRINKS
    elif args_data.get("cate") == "meal":
        temp_food = MEAL

    drinks = []
    for i in temp_food:
        temp_data = dict()
        if i:
            temp_data["goodsId"] = i[0]
            temp_data["goodsName"] = i[1]
            temp_data["price"] = i[2]
        drinks.append(temp_data)

    return jsonify(drinks)


@app.route("/order/checkout", methods=['POST'])
def order_checkout():
    """
    象征性接受下参数 模拟提交订单
    :return:
    """
    res = request.values.get("param")
    if res:
        # 下订单逻辑
        print(res, type(res))
        return jsonify({"code": 1, "msg": "ok"})
    else:
        return jsonify({"code": 0, "msg": "error"})


if __name__ == '__main__':
    app.run(debug=True)
