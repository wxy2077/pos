<template>

  <div id="app">
    <!-- 左侧导航栏 -->
    <left-nav></left-nav>

    <div id="main">
      <!--<router-link to="/">Home</router-link>-->
      <router-view/>
    </div>
  </div>
</template>

<script>
    import leftNav from '@/components/common/leftNav.vue'
    export default {
        name: 'app',
        components: {
            // HelloWorld
            leftNav
        },
    }
</script>
<style>

</style>
