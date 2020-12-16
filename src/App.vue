<template>
  <div id="app">
    <router-view id="router-view" />
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
  name: "App",
  components: {
    Footer
  }
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  /* -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale; */
  /* text-align: center; */
  color: #1d3336;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

#router-view {
  flex: 1;
}
</style>
