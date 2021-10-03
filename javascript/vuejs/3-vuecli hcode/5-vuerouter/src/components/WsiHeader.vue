<template>
  <div id="wsi-navbar">
    <router-link to="/"><wsi-botao>PAGINA 1</wsi-botao></router-link>
    <router-link to="/pagina2"> <wsi-botao>PAGINA 2</wsi-botao></router-link>
  </div>
</template>

<script lang="ts">
import WsiBotao from "./WsiBotao.vue";
export default {
  components: {
    WsiBotao,
  },
};
</script>

<style scoped lang="scss">
#wsi-navbar {
  width: 100%;
  height: 60px;
  background-color: black;
}
</style>
