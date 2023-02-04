

<template>
  <div class="container">
    <Header/>
  </div>
</template>


<script>
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Header
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

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

body {
  font-family: 'Poppins', sans-serif;
}
.container {
  max-width: 700px;
  margin: auto;
  overflow: auto;
  min-height: 300px;
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
