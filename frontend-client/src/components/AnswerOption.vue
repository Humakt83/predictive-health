<template>
  <div>
    <h2>{{answerOption.name}}</h2>
    <div class="options-container">
      <div class="option" :class="{'option--selected': option === selectedOption}" v-for="option in answerOption.options" v-bind:key="option" @click="selectOption(option)">
        <span>{{ option }}</span>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'answer-option',
  props: {
    answerOption: {
      type: Object,
    }
  },
  data: () => {
    return {
      selectedOption: undefined,
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

$option-width: 100px;
$color: gray;
$color2: aqua;
$color3: aquamarine;


h2 {
  color: $color;
  background-color: $color3;
  padding: 0.5rem;
  border-radius: 90px;
  width: 300px;
  margin: auto;
  margin-bottom: -5px;
}

.options-container {
  display: flex;
  color: $color;
  flex-direction: row;
  justify-content: space-evenly;
  margin-bottom: 5rem;
  &:before {
    content: '';
    background-color: $color3;
    position: absolute;
    height: $option-width / 5;
    width: 100%;
    z-index: 0;
    margin-top: $option-width / 4;
  }
  &:after {
    content: '';
    background-color: $color3;
    position: absolute;
    height: $option-width / 5;
    width: 100%;
    z-index: 0;
    margin-top: $option-width - ($option-width / 4);
  }
  .option {
    z-index: 5;
    font-size: 1.5rem;
    border-radius: 90px;
    border: 5px solid $color3;
    font-weight: bolder;
    padding: 0 1rem;
    background-color: $color2;
    width: $option-width;
    position: relative;
    cursor: pointer;
    &:before {
      content: '';
      display: block;
      padding-top: $option-width / 2;
    }
    &:after {
      content: '';
      display: block;
      padding-bottom: $option-width / 2;
    }
    &:hover {
      background-color: $color3;
    }
    &.option--selected {
      background-color: $color3;
    }
  }
}
</style>