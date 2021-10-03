<template>
  <div>
    <wsi-header/>
    <wsi-corpo/>
    <wsi-footer/>
  </div>
</template>

<script>
import WsiHeader from "./components/WsiHeader.vue";
import WsiCorpo from "./components/WsiCorpo.vue";
import WsiFooter from "./components/WsiFooter.vue";

export default {
  name: "App",
  components: {
    WsiHeader,
    WsiFooter,
    WsiCorpo,
  },
};
</script>

<style></style>
