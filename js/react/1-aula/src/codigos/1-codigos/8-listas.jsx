const App = () => {
  let lista = ["a", "b", "c"];
  let linhas = lista.map((letra) => {
    return <li key={letra}>{letra}</li>;
  });
  console.log(linhas);
  return <ul>{linhas}</ul>;
};

export default App;
