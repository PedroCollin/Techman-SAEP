<template>
  <main class="flexRowCenter">
    <div class="loginContainer flexColumnCenter">
      <img src="techman.png" alt="techman" />

      <div class="login flexColumnCenter">
        <input id="pass" type="password" v-model="password" disabled />

        <div class="numbersContainer flexColumnCenter">
          <div
            v-for="(row, index) in buttons"
            :key="index"
            class="rowsNumber flexRowCenter"
          >
            <button v-for="(btn, id) in row" :key="id"
             @click="btnClick(btn)">
              {{ btn }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      password: "",
      //CLIQUE 'WINDOWS' + . E SE SURPREENDA!
      buttons: [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["C", "0", "↲"],
      ],
    };
  },
  methods:{
    btnClick: function(btn){
      switch(btn){
        case "C":
          this.password = "";
          break;

        //login:
        case "↲":
          if(this.password.length >= 6)
          {
            this.$axios.post(this.$store.state.BASE_URL + "/users/?auth", 
              {
                password: this.password
              }
            )
            .then((response)=>{
              console.log("response",response.data);
              if(response.data.msg){
                alert(response.data.msg)
                this.password = "";   
              }
              else{
                this.$router.push("/home");
              }

            })
            .catch((error)=>{
              console.log("error",error);
            })
          }          
          else{
            alert("Senha deve conter ao menos 6 números");
          }


          break;

        default:
          this.password += btn;
          break;
      }

    }
  }
};
</script>


<style lang="scss" scoped>
main {
  width: 100vw;
  height: 100vh;
  max-height: 100vh;
  background-color: #cce2e2;

  .loginContainer {
    width: 50vw;
    max-width: 500px;
    height: 70vh;

    img {
      height: 100px;
      width: 85%;
    }
    .login {
      margin-top: 10px;
      background-color: #ffff;
      width: 100%;
      height: calc(100% - 100px);
      padding: 30px 80px;

      #pass {
        height: 50px;
        border: none;
        border-bottom: 1px solid black;
        text-align: center;
        outline: none;
        font-size: 20px;
      }
      .numbersContainer {
        .rowsNumber {
          padding: 10px;
          button {
            border-radius: 100%;
            border: 1px solid #35797d;
            margin: 0px 10px;
            width: 90px;
            height: 90px;
            font-size: 35px;
            color: #35797d;
            cursor: pointer;

            &:hover{
              background-color: #cce2e2;
            }
          }
        }
      }
    }
  }
}
</style>