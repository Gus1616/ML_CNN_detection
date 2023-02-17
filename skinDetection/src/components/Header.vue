<template>
    <header>
        <h1>Upload an image to analyse</h1>
        <!-- <Button /> -->
    </header>

</template>

<script>
// import Button from './Button.vue'
export default {
    name: 'Header',
    props: {
        title: String,
    },
    components: {
        // Button
    }
}
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

</style>
