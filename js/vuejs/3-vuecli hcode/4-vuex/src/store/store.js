import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            nome: "walter",
            idade: 24,
        }
    },
    getters: {
        getIdade(state) {
            return "idade: " + state.idade;
        },
        getNome(state) {
            return "nome: " + state.nome;
        }
    },

    mutations: {
        setNome(state, novoNome) {
            state.nome = novoNome;
        }
    },

    actions: {
        changeNome(context, dados) {
            context.commit('setNome', dados)
        }
    }
})

export default store;