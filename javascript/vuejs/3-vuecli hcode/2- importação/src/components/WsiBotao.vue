<template>
<button class="botao" v-bind:onclick="clickar">
    <slot>BOTAO</slot>
</button>    
</template>

<script lang="ts">
export default {
    methods: {
        clickar: (e)=>{
            console.log(e.target.innerText);
        }
    }
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