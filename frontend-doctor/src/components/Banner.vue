<template>
  <div class="banner">
    <img src="assets/BG.png">
    <div class="header">
      PREDICTIVE HEALTH
    </div>
  </div>
</template>
<script>
export default {
  name: 'banner'
};
</script>

<style scoped lang="scss">

@import "../_variables.scss";

.banner {
  background: linear-gradient(to right bottom, #FFF17A, #FCD232, #FFF17A,);
  height: 40vh;
  width: 100vw;
  position: absolute;
  margin: auto;
  top: 0;
  left: 0;
  img {
    max-height: 100%;
  }
  
  .header {
    font-weight: 800;
    font-size: 43px;
    line-height: 77px;
    top: 27vh;
    left: 50vw;
    transform: translate(-50%, 0);
    position: absolute;
    color: $color-background;
  }
}
</style>
