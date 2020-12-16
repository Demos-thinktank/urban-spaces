<template>
  <div class="layout">
    <div>
      <h1>{{ title }}</h1>
      <p>{{ subtitle }}</p>
      <p>{{ instruction }}</p>
      <div v-if="$route.name == 'ReadTheReport'">
        [Insert pdf of the report here]
      </div>
      <div v-else><InputOptions /></div>
    </div>
    <router-link to="/"><button class="go-back">GO BACK</button></router-link>
  </div>
</template>

<script>
import InputOptions from "@/components/InputOptions.vue";

export default {
  name: "Layout",
  props: {
    title: String,
    subtitle: String,
    instruction: String
  },
  components: {
    InputOptions
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.layout {
  padding: 2rem;
  height: -webkit-fill-available;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
  background-color: #ee7155;
}
h1 {
  font-weight: bold;
  margin-bottom: 1.5rem;
}
p {
  margin-bottom: 1rem;
}
.go-back {
  padding: 0.3rem 0.5rem;
  border-radius: 5px;
  background-color: #1d3336;
  color: whitesmoke;
}
.pre-formatted {
  white-space: pre;
}
</style>
