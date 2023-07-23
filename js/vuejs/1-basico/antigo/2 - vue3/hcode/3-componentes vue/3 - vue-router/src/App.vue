<template>
  <div id="app">
    <AppHeader/>
    <AppSection/>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import AppSection from './components/AppSection.vue'
export default {
  name: 'App',
  components: {
      AppHeader,
      AppSection,
  }
}
</script>

<style>

</style>
