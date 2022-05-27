<template>
  <div class="modal-overlay">
    <h6></h6>
    <div class="modal">
      <h6>Cadastro de Comentario</h6>
      <form >
      <input type="text" class="inputxt" name="Nome" placeholder="Comentario">
    
      <button>Cadastrar</button>
      </form>
    </div>
    <div class="close" @click="$emit('close-modal')">
      
    </div>
  </div>
</template>
<script>
  export default {
    name: 'inserirComentario',
}
</script>

<style scoped>


.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #000000da;
}

.modal {
  
  text-align: center;
  background-color: white;
  height: 400px;
  width: 1000px;
  margin-top: 10%;
  
  
}
.close {
  margin: 10% 0 0 16px;
  cursor: pointer;
}

.check {
  width: 150px;
}

h6 {
  padding-right: 35px;
  height: 50px;
  font-size: 24px;

}

p {
  font-size: 16px;
  margin: 20px 0;
}


button {
  background-color: #44babc;
  width: 150px;
  height: 40px;
  color: white;
  font-size: 14px;
  border-radius: 16px;
  margin-top: 150px;


}
.inputxt{
  font-family: inherit;
  width: 90%;
  height: 40px;
  border: 0;
  border-bottom: 2px solid #000;
  outline: 0;
  font-size: 1.3rem;
  color: #000;
  padding: 3px 0;
  background: transparent;
  
}

.check{
  width: 20px;
  height: 20px;
}

</style>