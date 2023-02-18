<template>
<div>
  <form class="upload-form">
      <label class="upload-label">
        <span class="upload-icon"><i class="fa fa-cloud-upload"></i></span>
        <span class="upload-text" v-if="showText">Choose another file to analyse</span>
        <span class="upload-text" v-else="showText">Choose file to analyse</span>

        <input class="upload-input" type="file" ref="fileInput" @change="upload"/>
      </label>
  </form>
  <div style="padding-top: 60px;">
    <div style="display: flex; justify-content: center; align-items: center;">
      <p v-if="loading">Loading result...</p>
      <div v-if="loading" class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>
      <p v-if="showText">The result of the sample that you uploaded is: <strong>{{ message }}</strong></p>
  </div>
</div>

  
   

</template>

<script>
import axios from 'axios';

export default {
    name: 'Button',
    data () {
    return {
      // image: null
      message: '',
      showText: false,
      loading: false,

    }
  },
  methods: {
upload() {
      const input = this.$refs.fileInput
      const file = input.files[0]

      const formData = new FormData()
      formData.append('photo', file)
      this.loading = true;

      axios.post('http://localhost:5000/api/photo/upload', formData)
      .then(response => {
        console.log(response.data)
        this.showText = true
        this.message = response.data.message
      })
      .catch(error => {
        console.log("error with photo and response")
      })
      .finally(() => {
        this.loading = false;
      })
    }


  }

 
}
</script>

<style scoped>
strong {
  font-weight: bold;
  color: red;
}
.upload-form {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.upload-label {
  display: inline-block;
  position: relative;
  font-size: 16px;
  font-weight: bold;
  padding: 10px 20px;
  color: #fff;
  background-color: #3498db;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.upload-label:hover {
  background-color: #2980b9;
}

.upload-icon {
  display: inline-block;
  margin-right: 10px;
}

.upload-icon i {
  font-size: 20px;
}

.upload-text {
  display: inline-block;
  vertical-align: middle;
}

.upload-input {
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
  cursor: pointer;
  width: 100%;
  height: 100%;
}

.lds-spinner {
  color: official;
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-spinner div {
  transform-origin: 40px 40px;
  animation: lds-spinner 1.2s linear infinite;
}
.lds-spinner div:after {
  content: " ";
  display: block;
  position: absolute;
  top: 3px;
  left: 37px;
  width: 6px;
  height: 18px;
  border-radius: 20%;
  background: blue;
}
.lds-spinner div:nth-child(1) {
  transform: rotate(0deg);
  animation-delay: -1.1s;
}
.lds-spinner div:nth-child(2) {
  transform: rotate(30deg);
  animation-delay: -1s;
}
.lds-spinner div:nth-child(3) {
  transform: rotate(60deg);
  animation-delay: -0.9s;
}
.lds-spinner div:nth-child(4) {
  transform: rotate(90deg);
  animation-delay: -0.8s;
}
.lds-spinner div:nth-child(5) {
  transform: rotate(120deg);
  animation-delay: -0.7s;
}
.lds-spinner div:nth-child(6) {
  transform: rotate(150deg);
  animation-delay: -0.6s;
}
.lds-spinner div:nth-child(7) {
  transform: rotate(180deg);
  animation-delay: -0.5s;
}
.lds-spinner div:nth-child(8) {
  transform: rotate(210deg);
  animation-delay: -0.4s;
}
.lds-spinner div:nth-child(9) {
  transform: rotate(240deg);
  animation-delay: -0.3s;
}
.lds-spinner div:nth-child(10) {
  transform: rotate(270deg);
  animation-delay: -0.2s;
}
.lds-spinner div:nth-child(11) {
  transform: rotate(300deg);
  animation-delay: -0.1s;
}
.lds-spinner div:nth-child(12) {
  transform: rotate(330deg);
  animation-delay: 0s;
}
@keyframes lds-spinner {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}




</style>
