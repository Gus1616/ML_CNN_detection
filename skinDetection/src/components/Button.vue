<template>
  <div>
    <!-- <form>
      <input type="file" ref="fileInput" @change="upload"/>
    </form> -->
    <form class="upload-form">
  <label class="upload-label">
    <span class="upload-icon"><i class="fa fa-cloud-upload"></i></span>
    <span class="upload-text">Choose a file</span>
    <input class="upload-input" type="file" ref="fileInput" @change="upload"/>
  </label>
</form>
<div>
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
      showText: false
    }
  },
  methods: {
upload() {
      const input = this.$refs.fileInput
      const file = input.files[0]

      const formData = new FormData()
      formData.append('photo', file)

      axios.post('http://localhost:5000/api/photo/upload', formData).then(response => {
        console.log(response.data)
        this.showText = true
        this.message = response.data.message
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



</style>
