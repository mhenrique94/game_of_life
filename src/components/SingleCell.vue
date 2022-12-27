<template>
  <button
    name="cell"
    class="cellButton"
    :class="{ active: isActive }"
    :key="key"
    @click="toggleAlive(cellId)"
  ></button>
</template>
<script>
export default {
  name: "SingleCell",
  data() {
    return {
      isActive: 0,
    };
  },
  methods: {
    toggleAlive(cellId) {
      this.isActive = this.isActive ? this.isActive - 1 : this.isActive + 1;
      this.$emit("toggleAlive", cellId);
    },
  },
  computed: {},
};
</script>
<style scoped>
.cellButton {
  width: 32px;
  height: 32px;
  margin: 1px;
  line-height: 0;
}

.active {
  background-color: black;
}
</style>
