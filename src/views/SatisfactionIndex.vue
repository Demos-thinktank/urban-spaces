<template>
  <Layout
    title="SATISFACTION INDEX"
    subtitle="We asked people to score how well their local areas were doing on the things they themselves thought were important. We found [a general sense of dissatisfaction]: leading to an overall local priority mismatch score of X, where 0 means that what is provided in a local area is in line with their population’s priorities."
    instruction="Use these buttons to explore these results in different parts of the country and find out the reasons why."
  />
</template>

<script>
// @ is an alias to /src
import Layout from "@/components/Layout.vue";

export default {
  name: "SatisfactionIndex",
  components: {
    Layout
  }
};
</script>
