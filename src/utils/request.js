/*
* 封装axios发送http请求
* */
import axios from 'axios'


// create an axios instance
const service = axios.create({
    baseURL: "http://127.0.0.1:5000/", // 指向自己的flask框架url
    timeout: 1000 * 10,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
});

// 返回 service 对象 方便封装接口
export default service
