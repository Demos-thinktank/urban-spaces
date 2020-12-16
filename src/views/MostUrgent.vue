<template>
  <Layout
    title="MOST URGENT"
    subtitle="The people want to see improved most urgently in their local area is [good local shops]. When asked which xxxx, x% said that their top priority was [ ], followed by y% who said [] ."
    instruction="Use these buttons to explore results in different parts of the country."
  />
</template>

<script>
// @ is an alias to /src
import Layout from "@/components/Layout.vue";

export default {
  name: "MostUrgent",
  components: {
    Layout
  }
};
</script>
