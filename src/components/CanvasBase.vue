<template>
  <div class="canvasBase" id="canvasBase">
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
      <button @click="nextCycle()">Iniciar</button>
      <button @click="start()">Reiniciar</button>
      <button>Parar</button>
    </div>
    <div class="controlForm">
      Para alterar as dimensões do quadro, insira a quantidade de células nos
      campos abaixo e clique em <strong>reiniciar</strong>.

      <label for="boardWidth"
        >Insira a <strong>largura</strong> personalizada</label
      >
      <input type="text" name="boardWidth" v-model="width" />
      <label for="boardHeight"
        >Insira a <strong>altura</strong> personalizada</label
      >
      <input type="text" name="boardHeight" v-model="height" />
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
      actualBoard: [],
      cellsAlive: 0,
      width: 12,
      height: 12,
      cycles: 0,
    };
  },
  created() {
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
      this.boardMatrix = [];
      for (var i = 0; i < this.width; i++) {
        this.boardMatrix.push([]);
        for (var j = 0; j < this.height; j++) {
          this.boardMatrix[i].push(false);
        }
      }
    },
    nextCycle() {
      let grid = [];
      for (var x = 0; x < this.width; x++) {
        grid[x] = [];
        for (var y = 0; y < this.height; y++) {
          let isActive = this.boardMatrix[x][y];
          let aliveNeighbours = this.neighbors(x, y);
          let result = false;

          if (isActive && aliveNeighbours < 2) {
            result = false;
          }

          if (isActive && (aliveNeighbours === 2 || aliveNeighbours === 3)) {
            result = true;
          }

          if (isActive && aliveNeighbours > 3) {
            result = false;
          }

          if (!isActive && aliveNeighbours === 3) {
            result = true;
          }

          grid[x][y] = result;
        }
      }
      for (let x = 0; x < this.width; x++) {
        for (let y = 0; y < this.height; y++) {
          this.boardMatrix[x][y] = grid[x][y];
        }
      }
      this.cellsAlive = this.boardMatrix.reduce(
        (count, row) => count + row.filter((cell) => cell).length,
        false
      );
    },
    neighbors(x, y) {
      let neighborhood = 0;

      for (var dx = -1; dx <= 1; dx++) {
        for (var dy = -1; dy <= 1; dy++) {
          let neighborX = x + dx;
          let neighborY = y + dy;
          if (
            (dx !== 0 || dy !== 0) &&
            neighborX >= 0 &&
            neighborX < this.width &&
            neighborY >= 0 &&
            neighborY < this.height &&
            this.boardMatrix[neighborX][neighborY]
          ) {
            neighborhood++;
          }
        }
      }

      return neighborhood;
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
