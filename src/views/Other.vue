<template>
    <div class="other">
        <p>Other Page</p>
        <!--<button @click="$store.commit('add',1)">+</button>-->
        <!--<button @click="$store.commit('reduce')">-</button>-->

        <button @click="add(1)">+</button>
        <button @click="reduce">-</button>

        <p>{{ $store.state.count }}</p>
    </div>
</template>

<script>
    import {mapMutations} from 'vuex';

    export default {
        name: "Other",
        data() {
            return {}
        },
        methods: mapMutations([
            'add', 'reduce'
        ]),
    }
</script>

<style scoped>

</style>