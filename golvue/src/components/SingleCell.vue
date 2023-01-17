<template>
  <div name="cell" class="cellButton" @click="clicked()"></div>
</template>
<script>
export default {
  name: "SingleCell",
  methods: {
    clicked() {
      this.$emit("toggle");
    },
  },
};
</script>
<style scoped>
.cellButton {
  width: 16px;
  height: 16px;
  margin: 0px;
  line-height: 0;
  background-color: whitesmoke;
  transition: background-color 0.25s linear;
  border: 1px solid gray;
}

.cellButton:hover {
  background-color: #c2c2c4;
  cursor: pointer;
}
</style>
