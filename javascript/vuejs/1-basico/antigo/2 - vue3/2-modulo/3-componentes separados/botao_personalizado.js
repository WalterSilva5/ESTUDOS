var botao_personalizado = {
    data() {
        return {
            texto: "TEXTO DO BOTÃO PERSONALIZADO",
        };
    },
    template: `
        <button>
            BOTAO: {{texto}}
        </button>
    `,
};
export default botao_personalizado;