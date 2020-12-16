<template>
  <div class="input-options">
    <div class="option">
      <label for="region">Region</label>
      <select name="region" id="region">
        <option value="north">North</option>
        <option value="south">South</option>
        <option value="east">East</option>
        <option value="west">West</option>
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
  </div>
</template>

<script>
export default {
  name: "InputOptions"
};
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
