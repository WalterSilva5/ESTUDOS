<template>
    <div class="corpo-do-site">
        <component :is="paginaAtual"></component>
    </div>
</template>
currentComponent

<script lang="ts">
import Pagina1 from './paginas/Pagina1.vue'
import Pagina2 from './paginas/Pagina2.vue'
export default {
    components: {
        Pagina1,
        Pagina2,
    },
    props:{
        paginaAtual: String
    }

}
</script>

<style lang="scss" scoped>
    .corpo-do-site{
        background-color: rgba(255, 255, 162, 0.733);
        min-height: 600px;
    }
</style>