<template>
  <div class="boardControl">
    <div class="controlButtons">
      <button>Iniciar</button>
      <button>Parar</button>
      <button>Reiniciar</button>
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
export default {
  name: "BoardControl",
};
</script>

<style scoped>
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
</style>
