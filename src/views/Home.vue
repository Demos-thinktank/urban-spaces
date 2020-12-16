<template>
  <div class="home">
    <div class="section-1">
      <div class="section-1_left">
        <h1>PLACE<br />PRIORITIES</h1>
        <router-link to="/read-the-report"
          ><button class="read-the-report">READ THE REPORT</button></router-link
        >
      </div>
      <div class="section-1_right">
        <p>
          The people want to see improved most urgently in their local area is
          [good local shops]. When asked which xxxx, x% said that their top
          priority was [ ], followed by y% who said [] .
        </p>
        <router-link to="/most-urgent"
          ><p class="explore-by-location mr s1">
            EXPLORE BY LOCATION
          </p></router-link
        >
      </div>
    </div>
    <div class="section-2">
      <div class="section-2_content">
        <p>
          Across the country x% of people are moving home because of factors
          related to the pandemic, or are seriously thinking of doing so.
          Another result here, eg about cities or reasons for moving or both.
        </p>
        <router-link to="/covid-effect"
          ><p class="explore-by-location s2">
            EXPLORE BY LOCATION
          </p></router-link
        >
      </div>
    </div>
    <div class="section-3">
      <div class="section-3_content">
        <p>
          We asked people to score how well their local areas were doing on the
          things they themselves thought were important. We found [a general
          sense of dissatisfaction]: leading to an overall local priority
          mismatch score of X, where 0 means that what is provided in a local
          area is in line with their population’s priorities
        </p>
        <router-link to="/satisfaction-index"
          ><p class="explore-by-location mr s3">
            EXPLORE BY LOCATION
          </p></router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Home",
  };
</script>

<style scoped>
  .home {
    display: flex;
    flex-direction: column;
  }

  .section-1 {
    border-bottom: 1px solid #1d3336;
    flex: 1;
    display: flex;
    justify-content: space-between;
    /* flex-wrap: wrap; */
    padding: 1rem 2rem;
    background-color: #ee7155;
  }

  @media screen and (max-width: 600px) {
    .section-1 {
      flex-direction: column;
    }
  }

  .section-1_left {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 30vw;
    min-width: max-content;
    margin-right: 5rem;
  }

  .read-the-report {
    margin: 1rem auto 1rem 0;
    padding: 0.3rem 0.5rem;
    border-radius: 5px;
    background-color: #1d3336;
    color: whitesmoke;
  }

  .section-1_right {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: right;
    max-width: 600px;
  }

  .section-2 {
    border-bottom: 1px solid #1d3336;
    flex: 1;
    padding: 1rem 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background-color: #bfc6cf;
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
  }

  .explore-by-location {
    font-weight: bold;
    cursor: pointer;
    margin-top: 0.75rem;
    width: max-content;
  }

  a {
    text-decoration: none;
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
</style>
