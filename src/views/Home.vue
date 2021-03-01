<template>
  <div class="home">
    <div class="section section-1">
      <div class="section-1_left">
        <h1>PLACE<br />PRI<span class="white">O</span>RITIES</h1>
        <img class="tube-map" alt="tube map graphic" src="../assets/blue-lines.png">
      </div>
      <div class="section-1_right">
        <h2 class="subtitle">Improving shops is Britain’s most important regeneration priority.</h2>
        <p>
        We asked people to think about what was available in their local area at the moment 
        and tell us what needed improving most urgently. The most popular answer for the 
        country as a whole was “good local shops” followed by “good transport services”. 
        </p>
        <router-link to="/read-the-report"
          ><p class="explore-link s1 mr">READ THE REPORT</p></router-link
        >
      </div>
    </div>
    <div class="section section-2">
      <div class="section-2_content">
        <h2 class="subtitle">Around 2.5 million people have already moved house because of Covid-19. A further 5.5 million either plan to or are thinking about it.</h2>
        <p>
        Across Britain, 9% of the adult population have already moved home because of 
        factors related to the pandemic, or have made plans to do so. A further 6% are 
        thinking about it. The most common reasons cited for moving are needing more 
        suitable housing, and wanting to be nearer family or in a more supportive community. 
        </p>
        <router-link to="/covid-effect"
          ><p class="explore-link s2">
            EXPLORE BY LOCATION
          </p></router-link
        >
        <img class="tube-map" alt="tube map graphic" src="../assets/blue-lines.png">
      </div>
    </div>
    <div class="section section-3">
      <div class="section-3_content">
        <h2 class="subtitle">How your place rates</h2>
        <p>
        We asked people to score how well their local areas were doing on the 
        everyday things they themselves thought were important. We asked about 
        access to fresh air and nature, shops, transport, housing, internet 
        access, places to go out, premises to support jobs, exercise and 
        sports facilities and supportive communities and pleasant streets. 
        Overall, the average rating across Britain across all categories was 
        somewhere between “good” and “neither good nor bad”.
        </p>
        <router-link to="/satisfaction-index"
          ><p class="explore-link mr s3">
            EXPLORE BY LOCATION
          </p></router-link
        >
        <img class="tube-map" alt="tube map graphic" src="../assets/white-lines.png">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home"
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
}

.section {
  min-height: 500px;
  overflow: hidden;
}

.subtitle{
  text-transform: uppercase;
}

.section-1 {
  flex: 1;
  display: flex;
  justify-content: space-between;
  /* flex-wrap: wrap; */
  padding: 1rem 2rem;
  background-color: #ee7155;
  position: relative;
}

@media screen and (max-width: 600px) {
  .section-1 {
    flex-direction: column;
  }
}

.section-1_left {
  display: flex;
  flex-direction: column;
  width: 30vw;
  min-width: max-content;
  margin-right: 5rem;
  height: 4em;
}

.section-1_right {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  text-align: right;
  max-width: 600px;

}

.tube-map {
  position: absolute;
  width: 89%;
  min-width: 1000px;
}

.section-1 .tube-map {
  transform: rotate(25deg);
  top:265px;
  right: 30%;
}

.section-2 .tube-map {
  top:2%;
  left: 68%;
  transform: scaleX(-1);
}

.section-3 .tube-map {
  right: 66%;
  transform: rotate(135deg);
  top: 50%;
}

/* Stop tube maps in their tracks on low widths */
@media screen and (max-width: 960px) {
  .section-1 .tube-map {
    right: 283px;
  }
  
  .section-2 .tube-map {
    left: 643px;
  }
  .section-3 .tube-map {
    right: 624px;
  }
}

.section-2 {
  border-bottom: 1px solid #1d3336;
  flex: 1;
  padding: 1rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background-color: #bfc6cf;
  position: relative;
}

.section-2_content,
.section-3_content {
  max-width: 600px;
}

.section-3 {
  flex: 1;
  padding: 1rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  text-align: end;
  background-color: #1d3336;
  color: whitesmoke;
  position: relative;
}

.explore-link {
  font-weight: bold;
  cursor: pointer;
  margin-top: 0.75rem;
  width: max-content;
}

a {
  text-decoration: none;
}

.s1 {
  text-align: end;
}
.s1,
.s2 {
  color: #1d3336;
}

.s3 {
  color: whitesmoke;
}

.mr {
  margin-left: auto;
}

.white {
  color: white;
  font-weight: 500;
}
</style>
