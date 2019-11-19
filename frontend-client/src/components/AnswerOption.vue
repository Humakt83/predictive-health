<template>
  <div class="section-container">
    <div class="section-title">
      <img :src="'assets/' + section.image" />
      <h2>{{section.name.toUpperCase()}}</h2>
    </div>
    <div class="options-container">
      <div class="option" :class="{'option--selected': option === selectedOption}" v-for="option in options" v-bind:key="option" @click="selectOption(option)">
        <p>{{ option }}</p>
        <font-awesome-icon class="check" icon="check-circle" v-if="option !== options[3]"/>
        <font-awesome-icon class="check check-never" icon="times-circle" v-else />
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'answer-option',
  props: {
    section: {
      type: Object,
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
      this.$emit('optionSelected', this.section.name, this.selectedOption);
    }
  }
}
</script>

<style scoped lang="scss">

@import "../_variables.scss";

.section-container {
  margin: auto;
  height: 400px;
}

.section-title {
  display: grid;
  height: 150px;
  grid-template-columns: 50vw 50vw;
  h2 {
    color: $color2;
    font-size: 26px;
    line-height: 35px;
    font-weight: 800;
    justify-self: start;
    padding-left: 1rem;
    align-self: end;
  }
  img {
    justify-self: end;
    max-width: 146px;
    max-height: 147px;
    padding-right:1rem;
    align-self: end;
  }
}

.options-container {
  position: absolute;
  display: grid;
  grid-template-columns: repeat(4, 25vw);
  color: $color;
  
  .option {
    justify-self: stretch;
    font-family: Montserrat;
    line-height: 35px;
    font-weight: 500;
    font-size: 22px;
    position: relative;
    cursor: pointer;
    .check {
      font-size: 2.5rem;
      color: $color3;
      position: absolute;
      z-index: 3;
      left: 50%;
      transform: translate(-50%, 0);
      background-color: $color-background;      
    }
    &:first-child {
      justify-self: end;
    }
    &:last-child {
      justify-self: start;
    }
    &:hover {
      .check {
        @include color-mixin(to-selected, $color3, $color2);
        animation: to-selected cubic-bezier(0.175, 0.885, 0.32, 1.275) 1.5s;
        color: $color2;
      }
      .check-never {
        @include color-mixin(to-selected-x, $color3, $color4);
        animation: to-selected-x cubic-bezier(0.175, 0.885, 0.32, 1.275) 1.5s;
        color: $color4;
      }
    }
    &.option--selected {
      .check {       
        color: $color2;
      }
      .check-never {
        color: $color4;
      }
    }
    &:after {
      position: absolute;
      content: '';
      height: 80px;
      left: 50%;
      transform: translate(-50%, -25%);
      border-left: 3px solid $color3;
    }
  }
  &:after {
    position: absolute;
    content: '';
    width: 52vw;
    bottom: -20%;
    transform: translate(24vw, 0);
    border-bottom: 3px solid $color3;
  }
}
</style>