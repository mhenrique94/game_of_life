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
  border: 1px solid gray;
}

.cellButton:hover {
  background-color: #c2c2c4;
}
</style>
