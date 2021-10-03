const ExibirTemperatura = (props) => {
  if (props.celsius >= 100) {
    return <p>A agua esta fervendo</p>;
  }
  return <p>A agua não esta quente</p>;
};

const App = () => {
  const [temperatura, setTemperatura] = React.useState("");
  const mudar = (e) => {
    setTemperatura(e.target.value);
  };
  return (
    <fieldset>
      <legend>Enter temperature in Celsius:</legend>
      <input value={temperatura} onChange={mudar} />
      <ExibirTemperatura celsius={parseFloat(temperatura)} />
    </fieldset>
  );
};

export default App;
