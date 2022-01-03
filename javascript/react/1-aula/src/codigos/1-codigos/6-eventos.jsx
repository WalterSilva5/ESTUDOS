import ReactDom from "react-dom";

const clique = () => {
  alert("botão clicado");
};

const alerta2 = (event) => {
  console.log(event.target.value);
};

const CliqueApp = () => {
  return (
    <div>
      <button onClick={clique}>TESTE</button>
      <br />
      <button onClick={alerta2} value="teste de evento">
        teste evento
      </button>
    </div>
  );
};

export default CliqueApp;
