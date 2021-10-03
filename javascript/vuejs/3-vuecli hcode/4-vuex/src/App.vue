<template>
  <div>
    <wsi-header @trocarDePagina="trocarDePagina" />
    <h1 style="color: red;">{{ nome }}</h1>

    <h1 style="color: red;">{{ idade }}</h1>

    <input
      type="text"
      @keyup="this.$store.commit('setNome', $event.target.value)"
    />

    <wsi-corpo :paginaAtual="paginaAtual" />
    <wsi-footer />
  </div>
</template>

<script>
import WsiHeader from "./components/WsiHeader.vue";
import WsiCorpo from "./components/WsiCorpo.vue";
import WsiFooter from "./components/WsiFooter.vue";
import axios from 'axios';



import { mapGetters, mapState } from "vuex";
export default {
  name: "App",
  components: {
    WsiHeader,
    WsiFooter,
    WsiCorpo,
  },
  data() {
    return {
      paginaAtual: "Pagina1",
    };
  }, 
  created() {
    axios
      .get("https://api.github.com/users/waltersilva5")
      .then((response) => this.$store.dispatch('changeNome', response.data.login));
  },
  methods: {
    trocarDePagina(pagina) {
      this.paginaAtual = pagina;
    },
  },

  computed: {
    ...mapGetters({
      nome: "getNome",
      idade: "getIdade",
    }),
  },
};
</script>

<style></style>
