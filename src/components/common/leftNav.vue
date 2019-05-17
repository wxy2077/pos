<template>
    <div class="left-nav" id="left-nav">
        <ul>
            <li>
                <i class="icon iconfont icon-shouyin"></i>
                <div>收银</div>
            </li>

            <li>
                <i class="icon iconfont icon-dianpu"></i>
                <div>店铺</div>
            </li>

            <li>
                <i class="icon iconfont icon-shangpin-copy"></i>
                <div>商品</div>
            </li>

            <li>
                <i class="icon iconfont icon-huiyuan"></i>
                <div>会员</div>
            </li>


            <li>
                <i class="icon iconfont icon-tongji1"></i>
                <div>统计</div>
            </li>
            <li>
                <i class="icon iconfont icon-shezhi"></i>
                <div>设置</div>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "leftNav",
        data(){
            return {

            }
        },
        methods: {
            setHeight: function () {
                //
                let orderHeight = window.screen.height;
                // window.console.log(orderHeight, "2222")
                document.getElementById("left-nav").style.height = orderHeight + 'px';

            }
        },
        mounted() {
            this.setHeight()
        },

    }
</script>

<style scoped>
    .left-nav{
        color: #fff;
        font-size: 10px;
        height: 100%;
        background-color: dodgerblue;
        float: left;
        width: 5%;
        margin-right: 5px;
    }
    .iconfont{
        font-size: 24px;
    }
    .left-nav ul{
        padding: 0px;
        margin: 0px;
    }
    .left-nav li{
        list-style: none;
        text-align: center;
        border-bottom: 1px solid #20a0ff;
        padding: 10px;
    }


</style>