<template>
  <div name="cell" class="cellButton" @click="clicked()"></div>
</template>
<script>
export default {
  name: "SingleCell",
  methods: {
    clicked() {
      let cellOrientation = this.$.vnode.key.split(":");
      console.log("printa no filho ", cellOrientation[0], cellOrientation[1]);
      this.$emit("toggle", cellOrientation[0], cellOrientation[1]);
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
  background-color: #e5e5e6;
}
</style>
