const ExibeSlots = (props) => {
  return (
    <div>
      <div>{props.primeiro}</div>
      <div>{props.segundo}</div>
    </div>
  );
};

const PrimeiroComp = () => {
  return <h1>Primeiro Componente</h1>;
};

const SegundoComp = () => {
  return <h1>Segundo Componente</h1>;
};

function App() {
  return <ExibeSlots primeiro={<PrimeiroComp />} segundo={<SegundoComp />} />;
}

export default App;
