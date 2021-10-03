const App = () => {
  const [nome, setNome] = React.useState("");

  const mudarNome = (event) => {
    setNome(event.target.value);
  };

  return (
    <form>
      <label>
        Name:
        <input type="text" value={nome} onChange={mudarNome} />
      </label>
      <p>{nome}</p>
    </form>
  );
};

export default App;
