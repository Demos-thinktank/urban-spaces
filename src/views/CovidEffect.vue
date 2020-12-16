<template>
  <Layout
    title="COVID EFFECT"
    subtitle="Across the country x% of people are moving home because of factors related to the pandemic, or are seriously thinking of doing so.  Another result here, eg about cities or reasons for moving or both."
    instruction="Use these buttons to see how people in different parts of the country are thinking about moving because of the pandemic."
  />
</template>

<script>
// @ is an alias to /src
import Layout from "@/components/Layout.vue";

export default {
  name: "CovidEffect",
  components: {
    Layout
  }
};
</script>
