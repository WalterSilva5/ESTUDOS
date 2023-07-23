
import { createStore } from 'redux';

const nomeState = {
  nome: 'padrao',
  labelOculta: false,
};

const nomeReducer = (state = nomeState, action) => {
  if (action.type === 'mudarNome') {
    state.nome = action.value;
  } else if (action.type === 'toggleLabel') {
    state.labelOculta = !action.value;
  }
  return state;
};

const store = createStore(nomeReducer);

export default store;
