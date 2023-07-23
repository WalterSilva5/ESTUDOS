import { createSlice, configureStore } from '@reduxjs/toolkit';

const nomeState = {
  nome: 'padrao',
  labelOculta: false,
};

const nomeSlice = createSlice({
  name: 'nomeSlice',
  initialState: nomeState,
  reducers: {
    mudarNome(state, action) {
      state.nome = action.payload;
    },
    toggleLabel(state) {
      state.labelOculta = !state.labelOculta;
    },
  },

});

const store = configureStore({
  reducer: { nomeState: nomeSlice.reducer },
});

export const nomeActions = nomeSlice.actions;

export default store;
