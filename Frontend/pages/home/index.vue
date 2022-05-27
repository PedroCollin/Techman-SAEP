<template>
  <main>
    <Header />
    <div class="homeContent flexColumn">
      <div
        class="equipment flexRowCenter"
        v-for="(device, index) in equipments"
        :key="index"
      >
        <div class="deviceImage flexRowCenter">
          <img
            v-if="device.image"
            :src="$store.state.BASE_URL + device.image"
            alt=""
            class="equipmentImg"
          />
        </div>
        <div class="equipmentContent flexColumnSpaced">
          <h2 class="name">{{ device.name }}</h2>
          <p class="description">{{ device.description }}</p>
          <div class="options flexRowBottom">
            <img src="icones/comentario.png" alt="" class="option" @click="showModal1 = true" />
            <img src="icones/deletar.png" alt="" class="option" @click="showModal2 = true"/>
          </div>
        </div>
      </div>
      <inserirComentario v-show="showModal1" @close-modal="showModal1 = false"/>
      <excuirComentario v-show="showModal2" @close-modal="showModal2 = false"/>
    </div>
  </main>
</template>
<script>
import axios from "axios";
export default {
  name: "home",
  data() {
    return {
      showModal1: false,
      showModal2: false,
      equipments: [],
      display: false,
    };
  },
  methods: {
    getDevices: async function () {
      await axios
        .get(this.$store.state.BASE_URL + "/devices/")
        .then((response) => {
          let data = response.data;
          this.equipments = data.data;
          console.log(this.equipments);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    openModal(){
      this.display = true
    },
    closeModal(){
      this.display = false
    }
  },
  mounted: async function () {
    this.getDevices();
  },
};
</script>

<style lang="scss" scoped>
.homeContent {
  height: auto;
  padding: 60px 40px;
  background: var(--bodyBackground);
  .equipment {
    padding: 25px 0;
    border-bottom: 1px solid var(--dark);
    .deviceImage {
      height: 200px;
      width: 500px;
      background: #fff;
      img {
        height: 120px;
        width: auto;
      }
      border: 1px solid var(--dark);
    }
    .equipmentContent {
      margin: 0 10px;
      height: 200px;
      .name {
        height: auto;
        width: auto;
        margin-bottom: 10px;
        font-size: 12pt;
        color: var(--dark);
      }
      .description {
        height: auto;
        max-width: 900px;
        font-size: 10pt;
        font-weight: 200;
      }
      .options {
        .option {
          height: 30px;
          width: 30px;
        }
        height: auto;
        width: auto;
        img {
          cursor: pointer;
          margin-right: 15px;
        }
      }
    }
  }
}
</style>