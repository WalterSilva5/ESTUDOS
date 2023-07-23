<template>
    <div class="section bg-info">
        <AppSectionPost/>
    </div>
</template>

<script>
import AppSectionPost from './AppSectionPost.vue'
export default {
    components:{
        AppSectionPost,
    }
}
</script>

<style scoped>
.section{
    min-height:600px;
}    
</style>