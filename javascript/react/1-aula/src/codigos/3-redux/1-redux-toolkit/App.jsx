import { useSelector, useDispatch } from 'react-redux';

import { nomeActions } from './store/store';

const App = () => {
  const nomeState = useSelector((state) => state.nomeState);
  const dispatch = useDispatch();

  const mudarNome = () => {
    dispatch(
      nomeActions.mudarNome(document.getElementById('inputNome').value),
    );
  };

  const mudarNomeAuto = (e) => {
    dispatch(nomeActions.mudarNome(e.target.value));
  };

  const ocultarLabel = () => {
    dispatch(nomeActions.toggleLabel());
  };

  return (
    <div className="container">
      {nomeState.labelOculta ? <h1 /> : (
        <h1>
          Nome:
          {nomeState.nome}
        </h1>
      )}
      <input
        type="text"
        value={nomeState.nome}
        onChange={mudarNomeAuto}
        className="form-control col-2 container"
      />

      <input
        type="text"
        id="inputNome"
        className="form-control col-2 container my-3"
      />
      <button onClick={mudarNome} className="btn btn-primary">
        salvar
      </button>
      <button onClick={ocultarLabel} className="btn mx-3 btn-primary">
        {nomeState.labelOculta ? 'exibir label' : 'ocultar label '}
      </button>
    </div>
  );
};

export default App;
