import { useSelector, useDispatch } from 'react-redux';

const App = () => {
  const nome = useSelector((state) => state.nome);
  const labelOculta = useSelector((state) => state.labelOculta);
  const dispatch = useDispatch();
  const mudarNome = () => {
    dispatch({
      type: 'mudarNome',
      value: document.getElementById('inputNome').value,
    });
  };

  const mudarNomeAuto = (e) => {
    dispatch({
      type: 'mudarNome',
      value: e.target.value,
    });
  };

  const ocultarLabel = () => {
    dispatch({
      type: 'toggleLabel',
      value: labelOculta,
    });
  };

  return (
    <div className="container">
      {labelOculta ? <h1 /> : (
        <h1>
          Nome:
          {nome}
        </h1>
      )}
      <input
        type="text"
        value={nome}
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
        {labelOculta ? 'exibir label' : 'ocultar label '}
      </button>
    </div>
  );
};

export default App;
