<template>
  <footer>
    <img alt="demos logo" class="demos-logo" src="../assets/demos-logo.jpg" />
    <img
      alt="legal and general logo"
      class="lg-logo"
      src="../assets/landg.png"
    />
  </footer>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
footer {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  border-top: 1px solid black;
  background-color: #1d3336;
}

.demos-logo {
  height: 2.5rem;
  margin: 1rem;
}

.lg-logo {
  height: 3rem;
  margin: 0rem;
}
</style>
