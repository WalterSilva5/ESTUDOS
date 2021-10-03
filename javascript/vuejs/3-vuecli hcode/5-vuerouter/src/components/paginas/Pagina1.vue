<template>
  <div>
    <h1>PAGINA 1</h1>
    <h1 style="color: red;">{{ nome }}</h1>
    <h1 style="color: red;">{{ idade }}</h1>
    <input
      type="text"
      @keyup="this.$store.commit('setNome', $event.target.value)"
    />
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters, mapState } from "vuex";

export default {
  created() {
    axios
      .get("https://api.github.com/users/waltersilva5")
      .then((response) =>
        this.$store.dispatch("changeNome", response.data.login)
      );
  },
  computed: {
    ...mapGetters({
      nome: "getNome",
      idade: "getIdade",
    }),
  },
};
</script>

<style lang="scss" scoped></style>
