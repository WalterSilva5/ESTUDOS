<template>
<button class="botao">
    <slot>BOTAO</slot>
</button>    
</template>

<script lang="ts">
export default {

}
</script>

<style scoped>
    .botao{
        background-color: gray;
        border-radius: 5px;
        height:50px;
        font-weight: bold;
        margin-top: 5px;  
    }  
</style>