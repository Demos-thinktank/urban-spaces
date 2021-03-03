<template>
  <div class="input-options">
    <div class="option">
      <label for="region">Region</label>
      <select
        v-model="region_selected"
        @change="regionChange"
        name="region"
        id="region"
      >
        <option disabled value="">Select a region</option>
        <option v-for="r in regions" :key="r.selection">
          {{ r.selection }}
        </option>
      </select>
    </div>
    <div class="option">
      <label for="postcode">Postcode</label>
      <div class="postcode-div">
        <input id="postcode" type="text" class="postcode" />
        <button type="submit"><i class="fa fa-search"></i></button>
      </div>
    </div>
    <div class="option">
      <label for="constituency">Constituency</label>
      <select name="constituency" id="constituency">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="C">C</option>
      </select>
    </div>
    <div class="option">
      <label for="type-of-location">Type of location</label>
      <select name="type-of-location" id="type-of-location">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="C">C</option>
      </select>
    </div>
    <div class="results" id="region-results">
      <p ref="regionText">Guuglel</p>
    </div>
  </div>
</template>

<script>
import json_locations from "../json/locations.json";
import json_regions from "../json/regions.json";
export default {
  name: "InputOptions",
  methods: {
    regionChange() {
      let our_region = this.regions.find(r => {
        return r.selection === this.region_selected;
      })
      this.$refs.regionText.innerHTML = "People in "+ our_region.text + " think that the most important priority for improvement in their local area is " + our_region.priority;
    }
  },
  data() {
    return {
      region_selected: "",
      locations: json_locations,
      regions: json_regions
    };
  }
};

// Add postcode controller script here

// Create new component for text rendering output script
</script>

<style scoped>
.input-options {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.option {
  margin: 2rem;
  display: flex;
  flex-direction: column;
}
.postcode {
  width: 10ch;
}

.postcode-div {
  display: flex;
}
</style>
