<template>
  <div>
    <wsi-header
    @trocarDePagina="trocarDePagina"
    />
    <wsi-corpo
    :paginaAtual="paginaAtual"
    />
    <wsi-footer/>
  </div>
</template>

<script lang="ts">
import WsiHeader from './components/WsiHeader.vue'
import WsiFooter from './components/WsiFooter.vue'
import WsiCorpo from './components/WsiCorpo.vue'
export default {
  name: 'App',
    components: {
      WsiHeader,
      WsiFooter,
      WsiCorpo,
  },
  data() {
    return {
      paginaAtual: 'Pagina1'
    }
  },
  methods:{
    trocarDePagina(pagina){
      this.paginaAtual = pagina;
    }
  }
}
</script>

<style>

</style>
