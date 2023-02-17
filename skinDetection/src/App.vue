<template>
  <div>
    <MenuBar />

  </div>

  <div class="container">
    <Header/>
    <p>Image must be as close as possible. Blurry images can cause incorrect results.</p>
    <div class="buttonStyle">
      <Button />


    </div>

    <!-- <p>{{ message }}</p> -->
  </div>
</template>


<script>
import Header from './components/Header.vue'
import MenuBar from './components/MenuBar.vue'
import Button from './components/Button.vue'

import axios from 'axios';

export default {
  name: 'App',
  components: {
    Header,
    MenuBar,
    Button
  },
  data () {
    return {
      message: '',

    }
  },
  created() {
    axios.get('http://localhost:5000/api/endpoint')
      .then(response => {
        this.message = response.data.message;
      })
      .catch(error => {
        console.error(error);
      });
      
  },

}



</script>


<style>
header {
  line-height: 1.5;
}

header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }


body {
  font-family: 'Poppins', sans-serif;
}
.buttonStyle {
  padding: 15px;
  display: flex;
  justify-content: center;


}
.container {
  position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  overflow: auto;
  min-height: 750px;
  min-width: 750px;

  border: 2px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}


</style>
