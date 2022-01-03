const Componente = (props) => {
  const [teste, setTeste] = React.useState("valor de teste");

  const mudarValorTeste = () => {
    setTeste(props.nome);
  };

  return (
    <div>
      <h1>{props.nome}</h1>
      <h1>{teste}</h1>
      <button onClick={mudarValorTeste}>mudar nome</button>
    </div>
  );
};

const App = () => {
  return <Componente nome="walter" />;
};

export default App;
