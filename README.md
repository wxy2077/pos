# fantastic

- vue-cli3 + element-ui + 后台Flask API接口
- vue2 + python3
> 这是仿照教程 [jspang](https://jspang.com/posts/2017/05/22/vuedemo.html) 写的pos系统 https://jspang.com/posts/2017/05/22/vuedemo.html

## 运行前端项目
```
npm install

npm run serve
```
## 运行后端接口
> 我用的是极简的 web框架 flask 就一个文件 posAdminAPI.py
```
# 安装python3.6 及以上  注意安装pip  windows系统 python官网找到对应版本双击即可 注意添加环境变量

# cmd 输入python 如果没有提示 命令没找到 则安装成功

# 安装依赖
pip install flask
pip install flask_cors  # 跨域

# 运行
python3 posAdminAPI.py

```
