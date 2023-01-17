<template>
  <div class="canvasBody">
    <div class="canvasBase" id="canvasBase">
      <div v-for="(row, index) in boardMatrix" :key="index">
        <SingleCell
          v-for="(cell, subindex) in row"
          :key="index + ':' + subindex"
          @toggle="selectCell(index, subindex), countCellsAlive()"
          :class="{ active: cellSelected(index, subindex) }"
        />
      </div>
    </div>
    <div :style="cover()"></div>
    <div class="boardControl">
      <p>
        Selecione as células iniciais no quadro ou experimente o
        <span class="boldText">RANDOMIZE</span> e pressione Iniciar.
      </p>
      <button class="controlButton" @click="startRandomize()">RANDOMIZE</button>
      <button
        class="controlButton"
        :disabled="cellsAlive === 0"
        @click="toggle()"
      >
        {{ startStopText }}
      </button>
      <div class="controlForm">
        <p>
          Para alterar as dimensões do quadro ou limpá-lo, selecione a
          quantidade de células nos campos abaixo e clique em
          <span class="boldText">reiniciar</span>.
        </p>
        <div class="inputForm">
          <label for="boardWidth"
            >Selecione a quantidade de células
            <span class="boldText">horizontalmente</span></label
          >
          <div class="sliderWrapper">
            <input
              type="range"
              min="12"
              max="48"
              name="boardWidth"
              v-model="width"
              class="slider"
            />
            <div class="sliderValue">{{ width }}</div>
          </div>
          <br />
          <label for="boardHeight"
            >Selecione a quantidade de células
            <span class="boldText">verticalmente</span></label
          >
          <div class="sliderWrapper">
            <input
              type="range"
              min="12"
              max="48"
              name="boardHeight"
              v-model="height"
              class="slider"
            />
            <div class="sliderValue">{{ height }}</div>
          </div>
        </div>
        <button class="controlButton" @click="start()" :disabled="disabled">
          Reiniciar
        </button>
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
      boardMatrix: [],
      actualBoard: [],
      cellsAlive: 0,
      width: 48,
      height: 32,
      cycles: 0,
      timeInterval: undefined,
      disabled: false,
    };
  },
  created() {
    this.start();
  },
  computed: {
    startStopText() {
      return this.timeInterval !== undefined ? "Parar" : "Iniciar";
    },
  },
  methods: {
    selectCell(row, col) {
      this.boardMatrix[row].splice(col, 1, true);
    },
    cellSelected(row, col) {
      return this.boardMatrix[row][col] === true;
    },
    start() {
      this.cellsAlive = 0;
      this.boardMatrix = [];
      for (var i = 0; i < this.width; i++) {
        this.boardMatrix.push([]);
        for (var j = 0; j < this.height; j++) {
          this.boardMatrix[i].push(false);
        }
      }
    },
    countCellsAlive() {
      this.cellsAlive = this.boardMatrix.reduce(
        (count, row) => count + row.filter((cell) => cell).length,
        false
      );
    },
    startRandomize() {
      this.boardMatrix = [];
      for (var i = 0; i < this.width; i++) {
        this.boardMatrix.push([]);
        for (var j = 0; j < this.height; j++) {
          this.boardMatrix[i].push([true, false][Math.round(Math.random())]);
        }
      }
      this.countCellsAlive();
    },
    nextCycle() {
      let grid = [];
      for (var x = 0; x < this.width; x++) {
        grid[x] = [];
        for (var y = 0; y < this.height; y++) {
          let isActive = this.boardMatrix[x][y];
          let aliveNeighbours = this.neighbours(x, y);
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
      this.countCellsAlive();
      if (this.cellsAlive === 0) {
        this.stopCycle();
      }
    },
    neighbours(x, y) {
      let neighborhood = 0;

      for (var dx = -1; dx <= 1; dx++) {
        for (var dy = -1; dy <= 1; dy++) {
          let neighbourX = x + dx;
          let neighbourY = y + dy;
          if (
            (dx !== 0 || dy !== 0) &&
            neighbourX >= 0 &&
            neighbourX < this.width &&
            neighbourY >= 0 &&
            neighbourY < this.height &&
            this.boardMatrix[neighbourX][neighbourY]
          ) {
            neighborhood++;
          }
        }
      }

      return neighborhood;
    },
    startCycle() {
      this.timeInterval = setInterval(this.nextCycle, 1000);
      this.disabled = true;
    },
    stopCycle() {
      clearInterval(this.timeInterval);
      this.timeInterval = undefined;
      this.disabled = false;
    },
    toggle() {
      if (this.timeInterval === undefined) {
        this.startCycle();
      } else {
        this.stopCycle();
      }
    },
    cover() {
      if (this.disabled) {
        return {
          width: `${this.width * 24}px`,
          height: `${this.height * 24}px`,
          float: "left",
          zIndex: 5,
          position: "absolute",
        };
      }
    },
  },
};
</script>

<style>
.canvasBody {
  display: flex;
}
.canvasBase {
  border: 1px solid grey;
  background-color: #63b984;
  display: flex;
  padding: 32px;
  margin: auto;
}

.boardControl {
  display: flex;
  flex-direction: column;
  padding: 32px;
  margin: auto;
  width: 30%;
  max-width: 300px;
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
  justify-content: space-around;
}

.controlButton {
  padding: 12px;
  font-size: 22pt;
  border: none;
}

.controlButton:hover {
  background-color: #63b984;
  cursor: pointer;
}

.active {
  background-color: black !important;
}

.boldText {
  font-weight: 700;
}

.inputForm {
  display: flex;
  flex-direction: column;
  margin: 24px auto;
}

label {
  margin-top: 12px;
}

.coverBoard {
  display: none !important;
}

.slider {
  width: 100%;
  margin: 0;
}

.sliderWrapper {
  display: flex;
  gap: 18px;
  justify-content: space-between;
  align-items: center;
  margin-top: 8px;
}

.sliderValue {
  background-color: white;
  padding: 8px;
}
</style>
