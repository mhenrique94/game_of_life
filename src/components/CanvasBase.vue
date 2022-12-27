<template>
  <div class="canvasBase">
    <div v-for="cellX in width" :key="cellX">
      <div v-for="cellY in height" :key="cellY">
        <SingleCell :key="`${cellX}:${cellY}`" />
      </div>
    </div>
  </div>
</template>

<script>
import SingleCell from "./SingleCell.vue";
export default {
  name: "CanvasBase",
  components: { SingleCell },
  data() {
    return {
      boardSize: 0,
      width: 12,
      height: 12,
    };
  },
  created() {
    this.boardSize = this.width * this.height;
  },
};
</script>

<style>
.canvasBase {
  border: 1px solid grey;
  background-color: #63b984;
  display: flex;
  padding: 32px;
  margin: 32px;
}
</style>
