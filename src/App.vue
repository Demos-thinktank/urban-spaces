<template>
  <div id="app">
    <Header />
    <router-view id="router-view" />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";

export default {
  name: "App",
  components: {
    Header
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
  color: #1d3336;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

#router-view {
  flex: 1;
}
</style>
