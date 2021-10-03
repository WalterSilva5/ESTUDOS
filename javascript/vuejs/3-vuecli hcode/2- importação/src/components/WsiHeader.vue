<template>
    <div id="wsi-navbar">
        <wsi-botao>PAGINA 1</wsi-botao>
        <wsi-botao>PAGINA 2</wsi-botao>
    </div>
</template>


<script lang="ts">
    import WsiBotao from "./WsiBotao.vue"
    export default {
        components:{
            WsiBotao
        }
    }
</script>


<style scoped lang="scss">
    #wsi-navbar{
        width: 100%;
        height: 60px;
        background-color: black;
    }
</style>