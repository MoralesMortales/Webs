<script setup>
import {ref} from "vue";
import HelloWorld from "./HelloWorld.vue";

const counter = ref(0);

function rest() {
  if(counter.value > 0){
    counter.value--;
  }

}

</script>

<template>
  <div class="btn">

    <HelloWorld msg="READ THIS" msg1 = "Nuevo TXT"></HelloWorld>

    <button @click="counter++">Sumar</button>
    <button @click="rest">Restar</button>
    <button @click="counter = 0">Reiniciar</button>
    
  </div>

  <h1 id="">{{ counter }}</h1>
  
</template>
