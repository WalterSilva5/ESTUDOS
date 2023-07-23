import { createRouter, createWebHashHistory } from 'vue-router'
import pagina1 from "../components/paginas/Pagina1.vue"
import pagina2 from "../components/paginas/Pagina2.vue"

const routes = [{
        path: '/',
        component: pagina1
    },
    {
        path: '/pagina2',
        component: pagina2
    }
]

const router = createRouter({
    linkExactActiveClass: 'link-active',
    history: createWebHashHistory(),
    routes
})

export default router