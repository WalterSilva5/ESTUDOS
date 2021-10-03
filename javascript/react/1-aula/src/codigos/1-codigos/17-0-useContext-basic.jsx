const Componente = () => {
  const { nome, setnome } = React.useContext(Dados);
  return (
    <div>
      {nome}
      <br />
      <input
        type="text"
        value={nome}
        onChange={(e) => setnome(e.target.value)}
      />
    </div>
  );
};

export const Dados = React.createContext();

const App = () => {
  const [nome, setnome] = React.useState("");
  return (
    <div>
      <Dados.Provider value={{ nome, setnome }}>
        <Componente />
      </Dados.Provider>
    </div>
  );
};

export default App;
