<script>
import CanvasBase from "./components/CanvasBase.vue";
export default {
  components: { CanvasBase },
  data() {
    return {
      modal: false,
    };
  },
  methods: {
    toggleModal() {
      this.modal = this.modal ? false : true;
    },
  },
};
</script>

<template>
  <h1>John Conway's Game Of Life!</h1>

  <img
    class="info"
    src="../public/info-button.png"
    alt="icone de informação"
    @click="toggleModal"
  />
  <a href="https://github.com/mhenrique94" target="_blank">
    <img
      class="git_logo"
      src="../public/github-mark.png"
      alt="Logo do Github"
    />
  </a>

  <div v-show="modal" class="disclaimer">
    <p>Desenvolvido em Vue.js por Marcelo Silva com base em:</p>
    <p class="links">John Conway, claro! Mas também:</p>
    <p class="links">
      <a href="https://playgameoflife.com/"
        >Game of Life by Edwin Martin (regras)</a
      >
    </p>
    <p class="links">
      <a
        href="https://www.youtube.com/watch?v=Di9URIW4eY0&list=PL5k6y1ttLXO__cZG3_jUonI1D6BZAprkB&index=1"
        >Aprenda a programar GOL em Javascript | Canal Sabe contar? (lógica dos
        vizinhos)
      </a>
    </p>
    <p class="links">
      <a href="https://github.com/zoispag/vue-conways-game-of-life"
        >Conway's Game Of Life | Zoispag's Github (animação)
      </a>
    </p>
  </div>

  <CanvasBase />
</template>

<style scoped>
h1 {
  margin: 0 auto 22px auto;
  padding: 12px;
  background-color: aliceblue;
}
.links {
  margin-bottom: 12px;
}
.info {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 32px;
  height: 32px;
  cursor: pointer;
}

.git_logo {
  position: absolute;
  width: 32px;
  height: 32px;
  top: 12px;
  right: 56px;
}

.disclaimer {
  background-color: antiquewhite;
  width: 420px;
  padding: 22px;
  font-size: 11pt;
  position: absolute;
  right: 64px;
  top: 32px;
  border-radius: 8px;
}
</style>
