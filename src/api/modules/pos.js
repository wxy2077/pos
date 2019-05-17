/*
* pos 页面操作的接口
* */

import request from '@/utils/request'

export function getGoods(param) {
    return request({
        url: '/get/goods',
        method: 'get',
        params: { param }

    })
}

export function getOftenGoods() {
    return request({
        url: '/get/often/goods',
        method: 'get',
    })
}

export function postOrder(param) {
    return request({
        url: '/order/checkout',
        method: 'post',
        // header: {""},
        params: { param }
    })
}