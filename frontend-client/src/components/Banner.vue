<template>
<div class="banner">
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
  background-image: url('../images/BG.jpg');
  background-size: 100vw 60vh;
  height: 60vh;
  width: 100vw;
  position: relative;
  
  .header {
    font-weight: 800;
    font-size: 43px;
    line-height: 77px;
    top: 35vh;
    left: 50vw;
    transform: translate(-50%, 0);
    position: absolute;
    color: $color-background;
  }
}
</style>
