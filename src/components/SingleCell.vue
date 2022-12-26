<template>
  <button name="cell" class="cellButton" :cellId="`${cellX}:{cellY}`"></button>
</template>
<script>
export default {
  name: "SingleCell",
  props: ["cellX", "cellY"],
};
</script>
<style scoped>
.cellButton {
  width: 32px;
  height: 32px;
}
</style>
