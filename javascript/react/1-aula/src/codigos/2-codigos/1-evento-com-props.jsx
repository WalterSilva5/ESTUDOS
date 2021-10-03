const Componente = () => {
  const [nome, mudarNome] = useState("");

  return (
    <div>
      <h1>{nome}</h1>
      <button onClick={mudarNome}>mudar nome</button>
    </div>
  );
};
''
const App = () => {
  return <Componente nome="walter" />;
};

export default App;
