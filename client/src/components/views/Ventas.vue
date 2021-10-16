<template>
  <h1>ventas</h1>
</template>

<script>
import axios from 'axios'
export default {
  created () {
    axios.get('http://127.0.0.1:4000/ventas').then((result) => {
      console.log(result.data)
    })
  }
}
</script>
