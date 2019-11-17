<template>
  <div id="app">
    <banner />
    <home/>
  </div>
</template>
<script>
// @ is an alias to /src
import Home from '@/components/Home';
import Banner from '@/components/Banner';

export default {
  name: 'app',
  components: {
    Home,
    Banner
  }
};
</script>
<style lang="scss">

@import "./_variables.scss";

#app {
  font-family: Montserrat, 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: auto;
  background: $color-background;
}
</style>
