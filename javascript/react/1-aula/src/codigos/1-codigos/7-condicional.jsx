const App = () => {
  const [logado, setLogado] = React.useState("");

  const mudarLogado = (e) => {
    if (e.target.value == "sim") {
      console.log(e.target.value);
      setLogado(true);
    } else if (e.target.value == "nao") {
      console.log(e.target.value);
      setLogado(false);
    }
  };

  return (
    <div>
      {logado ? <h1>logado</h1> : <h1>nao logado</h1>}
      <input onChange={mudarLogado} />
    </div>
  );
};

export default App;
