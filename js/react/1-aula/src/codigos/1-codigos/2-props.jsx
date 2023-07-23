const Componente = (props) => {
  return (
    <div>
      <h1>nome: {props.nome}</h1>
    </div>
  );
};

const App = () => {
  return <Componente nome="walter" />;
};

//<App  nome="walter" />,
export default App;
