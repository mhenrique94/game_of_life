<template>
  <div class="canvasBase">
    <div v-for="cellX in width" :key="cellX">
      <div v-for="cellY in height" :key="cellY">
        <SingleCell
          :key="`${cellX}:${cellY}`"
          :x="cellX"
          :y="cellY"
        ></SingleCell>
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
      cellsArray: [],
      boardSize: 0,
      width: 12,
      height: 12,
    };
  },
  created() {
    this.boardSize = this.cellsCount();
  },
  methods: {
    cellsCount() {
      return this.width * this.height;
    },
  },
};
</script>

<style>
.canvasBase {
  border: 1px solid grey;
  background-color: #63b984;
  width: 384px;
  display: flex;
}
</style>
