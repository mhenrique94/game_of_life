<template>
  <div class="canvasBase">
    <div v-for="(row, index) in boardMatrix" :key="index">
      <SingleCell
        v-for="(cell, subindex) in row"
        :key="index + ':' + subindex"
        @toggle="selectCell(index, subindex)"
        :class="{ active: cellSelected(index, subindex) }"
      />
    </div>
  </div>
  <div class="boardControl">
    <div class="controlButtons">
      <button @click="start()">Reiniciar</button>
      <button>Parar</button>
    </div>
    <div class="controlForm">
      <label for="boardWidth"
        >Insira a <strong>largura</strong> personalizada</label
      >
      <input type="text" name="boardWidth" />
      <label for="boardHeight"
        >Insira a <strong>altura</strong> personalizada</label
      >
      <input type="text" name="boardHeight" />
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
      boardMatrix: [],
      arrayY: [],
      boardSize: 0,
      width: 12,
      height: 12,
    };
  },
  created() {
    this.boardSize = this.width * this.height;
    this.start();
  },
  methods: {
    selectCell(row, col) {
      this.boardMatrix[row].splice(col, 1, true);
    },
    cellSelected(row, col) {
      return this.boardMatrix[row][col] === true;
    },
    start() {
      for (var i = 0; i < this.width; i++) {
        this.boardMatrix.push([]);
        for (var j = 0; j < this.height; j++) {
          this.boardMatrix[i].push(false);
        }
      }
    },
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
.boardControl {
  display: flex;
  flex-direction: column;
}
.controlForm,
.boardControl {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.controlButtons {
  display: flex;
  gap: 30px;
}
.active {
  background-color: black !important;
}
</style>
