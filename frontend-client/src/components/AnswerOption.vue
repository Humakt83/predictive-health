<template>
  <div class="section-container">
    <h2>{{section}}</h2>
    <div class="options-container">
      <div class="option" :class="{'option--selected': option === selectedOption}" v-for="option in options" v-bind:key="option" @click="selectOption(option)">
        <span>{{ option }}</span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'answer-option',
  props: {
    section: {
      type: String,
    }
  },
  data: () => {
    return {
      selectedOption: undefined,
      options: ['Daily', 'Weekly', 'Monthly', 'Never']
    }
  },
  methods: {
    selectOption(option) {
      this.selectedOption = option;
    }
  }
}
</script>

<style scoped lang="scss">

$option-width: 50px;
$color: #07020d;
$color2: #5ec2b7;
$color3: #f1e9db;

.section-container {
  max-width: 1200px;
  margin: auto;
}

h2 {
  color: $color;
  background-color: $color3;
  padding: 0.5rem;
  border-radius: 90px;
  width: 200px;
  margin: auto;
  margin-bottom: -5px;
  font-size: 1.2rem;
}

.options-container {
  display: flex;
  color: $color;
  flex-direction: row;
  justify-content: space-evenly;
  margin-bottom: 1rem;
  &:before {
    content: '';
    background-color: $color3;
    position: absolute;
    height: $option-width / 5;
    width: 100%;
    z-index: 0;
    margin-top: $option-width / 3;
  }
  &:after {
    content: '';
    background-color: $color3;
    position: absolute;
    height: $option-width / 5;
    width: 100%;
    z-index: 0;
    margin-top: $option-width - ($option-width / 7);
  }
  .option {
    z-index: 5;
    font-size: 1rem;
    border-radius: 90px;
    border: 5px solid $color2;
    font-weight: bolder;
    padding: 0 1rem;
    background-color: $color3;
    width: $option-width;
    position: relative;
    cursor: pointer;
    &:before {
      content: '';
      display: block;
      padding-top: $option-width / 1.75;
    }
    &:after {
      content: '';
      display: block;
      padding-bottom: $option-width / 1.75;
    }
    &:hover {
      background-color: $color3;
    }
    &.option--selected {
      background-color: $color2;
    }
  }
}
</style>