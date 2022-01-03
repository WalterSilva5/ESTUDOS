<template>

    <div>
        
        <div class="container">

            <div class="row mt-5">
                <h3>Você está vendo notícias do: {{ championship }}</h3>
            </div>

        </div>
        
        <component :is="currentComponent"></component>

        <div class="container">

            <div class="row my-club mt-5">

                <div class="col-6">
                    <h2>Seu clube é: {{ myClub }}</h2>
                </div>

                <div class="col-6">
                    <HcodeInput v-model="myClub" />
                </div>

            </div>

        </div>

    </div>

</template>

<script>
import HcodeSectionBanner from './HcodeSectionBanner'
import HcodeInput from './HcodeInput'

export default {
    components: {
        HcodeSectionBanner,
        HcodeSectionNews: () => import('./HcodeSectionNews'),
        HcodeInput
    },
    data() {
        return {
            myClub: 'Hcode Treinamentos'
        }
    },
    props: {
        championship: String,
        currentComponent: String
    }
}
</script>

<style scoped>

</style>