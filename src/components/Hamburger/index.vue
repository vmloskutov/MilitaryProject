<template>
  <div style="padding: 0 15px;" @click="toggleClick">
    <svg width="25" height="18" viewBox="0 0 25 18" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M0 1H25" stroke="white" stroke-width="2"/>
      <path d="M0 9H25" stroke="white" stroke-width="2"/>
      <path d="M0 17H25" stroke="white" stroke-width="2"/>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'Hamburger',
  props: {
    isActive: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    toggleClick() {
      this.$emit('toggleClick')
    }
  }
}
</script>

<style scoped>
.hamburger {
  display: inline-block;
  vertical-align: middle;
  width: 20px;
  height: 20px;
}

.hamburger.is-active {
  transform: rotate(180deg);
}
</style>
