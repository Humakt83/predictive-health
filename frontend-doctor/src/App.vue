<template>
  <div id="app">
    <banner />
    <home />
  </div>
</template>

<script>
import Home from '@/views/Home';
import Banner from '@/components/Banner';


export default {
  name: 'app',
  components: {
    Home,
    Banner
  },
};
</script>

<style lang="scss">
body {
  overflow-x: hidden;
  width: 100vw;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: auto;
  width: 100vw;
}
</style>
