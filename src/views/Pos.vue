<template>
    <div class="pos" id="order-list">
        <div>
            <el-row>
                <el-col :span="7" class="pos-order">
                    <el-tabs>
                        <el-tab-pane label="订单">
                            <el-table :data="orderList" border height="550" lazy style="width: 100%">

                                <el-table-column prop="goodsName" label="商品"></el-table-column>
                                <el-table-column prop="count" label="量" width="50"></el-table-column>
                                <el-table-column prop="price" label="单价(¥)" width="70"></el-table-column>
                                <el-table-column label="操作" width="100" fixed="right">

                                    <template slot-scope="scope">
                                        <el-button type="text" size="small"
                                                   @click="deleteOrder(scope.$index, scope.row)">
                                            删除
                                        </el-button>
                                        <!--<el-button type="text" size="small">增加</el-button>-->
                                    </template>

                                </el-table-column>
                            </el-table>

                            <div class="totalDiv">
                                <small>数量：</small>
                                <strong>{{ orderCount }}</strong> &nbsp;&nbsp;&nbsp;&nbsp;
                                <small>总计：</small>
                                <strong>{{ orderMoney }}</strong> 元
                            </div>

                            <div class="div-btn">

                                <el-button type="warning">挂单</el-button>
                                <el-button type="danger" :disabled="isClick" @click="deleteAllOrder">删除</el-button>
                                <el-button type="success" :disabled="isClick" @click="checkout" >结账</el-button>
                            </div>
                        </el-tab-pane>

                        <el-tab-pane label="挂单">
                            挂单

                        </el-tab-pane>

                        <el-tab-pane label="外卖">
                            外卖
                        </el-tab-pane>

                    </el-tabs>
                </el-col>

                <el-col :span="15" id="often-right">

                    <div class="often-goods">
                        <div class="title">常用商品</div>
                        <div class="often-goods-list">
                            <ul>
                                <li v-for="(goods, index) in oftenGoods" :key="index">
                                    <span>{{goods.goodsName}}</span>
                                    <span class="o-price"> ¥ {{goods.price}} 元</span>
                                    <span class="addFood" @click="addOrder(goods)">
                                            <el-button type="primary" circle
                                                       style="width: 40px; height: 40px">+1</el-button>
                                    </span>
                                </li>
                            </ul>

                        </div>
                    </div>

                    <div class="goods-type">
                        <el-tabs v-model="activeName" @tab-click="switchClick">
                            <el-tab-pane label="单点" name="foods">
                                <ul class='cookList'>
                                    <li v-for="(goods, index) in foods" :key="index">
                                        <span class="foodImg"><img
                                                src="http://pic.616pic.com/ys_b_img/00/04/02/Hy0t5dQYvO.jpg"
                                                width="100%"></span>
                                        <span class="foodName">{{ goods.goodsName }}</span>
                                        <span class="foodPrice">￥{{ goods.price }}元</span>
                                        <span class="addFood" @click="addOrder(goods)">
                                            <el-button type="primary" circle
                                                       style="width: 40px; height: 40px">+1</el-button>
                                        </span>
                                    </li>
                                </ul>
                            </el-tab-pane>
                            <el-tab-pane label="饮料" name="drinks">
                                <ul class='cookList'>
                                    <li v-for="(goods, index) in drinks" :key="index">
                                        <span class="foodImg"><img
                                                src="http://pic.616pic.com/ys_b_img/00/04/02/Hy0t5dQYvO.jpg"
                                                width="100%"></span>
                                        <span class="foodName">{{goods.goodsName}}</span>
                                        <span class="foodPrice">￥{{goods.price}}元</span>
                                        <span class="addFood" @click="addOrder(goods)">
                                            <el-button type="primary" circle
                                                       style="width: 40px; height: 40px">+1</el-button>
                                        </span>
                                    </li>
                                </ul>
                            </el-tab-pane>
                            <el-tab-pane label="套餐" name="meal">
                                <ul class='cookList'>
                                    <li v-for="(goods, index) in meal" :key="index">
                                        <span class="foodImg"><img
                                                src="http://pic.616pic.com/ys_b_img/00/04/02/Hy0t5dQYvO.jpg"
                                                width="100%"></span>
                                        <span class="foodName">{{goods.goodsName}}</span>
                                        <span class="foodPrice">￥{{goods.price}}元</span>
                                        <span class="addFood" @click="addOrder(goods)">
                                            <el-button type="primary" circle
                                                       style="width: 40px; height: 40px">+1</el-button>
                                        </span>
                                    </li>
                                </ul>
                            </el-tab-pane>
                        </el-tabs>
                    </div>

                </el-col>

            </el-row>

        </div>
    </div>
</template>

<script>
    // import store from '@/store'
    // import {mapMutations} from 'vuex';


    import api from '../api/index'

    export default {
        name: "Pos",
        data() {
            return {
                orderLength: 20,   //
                orderList: [],  //  点餐订单
                orderCount: 0,
                orderMoney: 0,

                isClick: true,

                oftenGoods: [{goodsName: '汉堡', price: 10}, {goodsName: '可乐', price: 5}],

                activeName: 'foods',  // 点单栏 首页

                foods: [],    // 单点小食
                drinks: [],   // 饮料
                meal: [],     // 套餐
            }
        },
        methods: {
            // 强制设置页面文本高度
            setHeight: function () {
                // 设置高度
                // let orderHeight = document.body.clientHeight;
                let orderHeight = window.screen.height;
                document.getElementById("order-list").style.height = orderHeight + 'px';
            },
            // 获取常用商品
            getOftenGoods: function () {
                api.pos.getOftenGoods().then(({data}) => {
                    this.oftenGoods = data
                    // window.console.log(data)
                }).catch(({error}) => {
                    window.console.log(error)
                })
            },
            // 获取table中的商品
            getGoods: function (cate, page, size) {
                api.pos.getGoods({cate, page, size}).then(({data}) => {
                    //  老感觉 这样不行
                    if (cate === "foods") {
                        this.foods = data
                    } else if (cate === "drinks") {
                        this.drinks = data
                    } else if (cate === "meal") {
                        this.meal = data
                    }
                    // window.console.log( data, "ok成功!");
                }).catch(({error}) => {
                    window.console.log("Error", error)
                })
            },
            // 切换goods table
            switchClick: function (tab) {
                // window.console.log(tab)
                this.getGoods(tab.name, 1, 10)
            },
            // 添加订单项
            addOrder: function (food) {
                this.orderCount = 0;
                this.orderMoney = 0;
                let isHave = false;
                //判断是否这个商品已经存在于订单列表

                for (let i = 0; i < this.orderList.length; i++) {
                    if (this.orderList[i].goodsId === food.goodsId) {
                        isHave = true; //存在
                    }
                }
                //根据isHave的值判断订单列表中是否已经有此商品
                if (isHave) {
                    //存在就进行数量添加
                    let arr = this.orderList.filter(o => o.goodsId === food.goodsId);
                    arr[0].count++;
                    //console.log(arr);
                } else {
                    //不存在就推入数组
                    let newGoods = {goodsId: food.goodsId, goodsName: food.goodsName, price: food.price, count: 1};
                    this.orderList.push(newGoods);
                }

                this.calcOrder()
            },
            // 删除订单项
            deleteOrder: function (index, foods) {
                this.orderList.splice(index, 1)
                // window.console.log(index, "index")
                window.console.log("删除" + foods.goodsName)
                this.calcOrder()
            },
            // 计算订单合计栏
            calcOrder: function () {
                this.orderCount = 0;
                this.orderMoney = 0;
                if (this.orderList) {
                    this.orderList.forEach((element) => {
                        this.orderCount += element.count;
                        this.orderMoney = this.orderMoney + (element.price * element.count);
                        window.console.log(this.orderCount, "111")
                        window.console.log(this.orderMoney, "222")
                    });
                }
            },
            // 删除所有订单
            deleteAllOrder() {
                this.$confirm('确定删除订单, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                    this.orderCount = 0;
                    this.orderMoney = 0;
                    this.orderList = [];
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },
            // 模拟生成订单

            checkout(){
                this.$confirm('请扫描二维码付款', '提示', {
                    // 实际一般都是第三方支付 跳转支付宝或者微信 银联之类的
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    // 象征性的向后台发送post请求
                    api.pos.postOrder({
                        "orderList": this.orderList
                    }).then(({data}) => {
                        if(data.code === 1){
                            this.$message({
                                type: 'success',
                                message: '付款成功!'
                            });
                            this.$notify({
                                title: '付款成功',
                                message: '已经付款成功，该订单已经生产！订单号为:xxxx',
                                duration: 0
                            });

                            this.orderCount = 0;
                            this.orderMoney = 0;
                            this.orderList = [];
                        }else{
                            this.$message({
                                type: 'info',
                                message: '付款失败!'
                            });
                        }

                    }).catch(({error}) => {
                        this.$message({
                            type: 'error',
                            message: error
                        });
                    });


                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消付款'
                    });
                });
            }

        },
        watch:{
            // 监听 orderList长度来控制开关  主要 disable要加 :在前面
            orderList: function () {
                // window.console.log(this.isClick, "is click")
                if(this.orderList.length >= 1){
                    this.isClick = false
                }else{
                    this.isClick = true
                }
            }
        },
        mounted() {
            this.setHeight(),
            this.getGoods("foods", 1, 10),
            this.getOftenGoods()
        },
    }
</script>

<style scoped>
    .pos-order {
        background-color: #f9fafc;
        border-right: 1px solid #c0ccda;
    }

    /*底部按钮*/
    .div-btn {
        margin-top: 10px;
        float: right;
        margin-right: 30px;
        /*border: 1px solid;*/
    }

    .title {
        height: 20px;
        border-bottom: 1px solid #d3dce6;
        background-color: #f9fafc;
        padding: 10px;
        text-align: left;
    }

    .often-goods-list ul li {
        list-style: none;
        float: left;
        border: 1px solid #e5e5e5;
        padding: 10px;
        margin: 10px;
        background-color: white;
    }

    .o-price {
        color: #58b7ff;
    }

    .goods-type {
        margin-left: 5px;
        clear: both;
    }

    .cookList li {
        list-style: none;
        width: 23%;
        border: 1px solid #E5E9F2;
        height: auto;
        overflow: hidden;
        background-color: #fff;
        padding: 2px;
        float: left;
        margin: 2px;

    }

    .cookList li span {

        display: block;
        float: left;
    }

    .foodImg {
        width: 40%;

    }

    .foodName {
        font-size: 18px;
        padding-left: 10px;
        color: brown;
        height: 39px;
        width: 55%;
        line-height: 39px;
        text-align: center;
    }

    .foodPrice {
        font-size: 18px;
        padding-left: 10px;
        padding-top: 10px;
        /*float: right;*/
        /*display: inline;*/

    }

    .addFood {
        margin-left: 10px;
        height: 100%;
        width: 17%;
        /*background-color: chartreuse;*/
    }


</style>