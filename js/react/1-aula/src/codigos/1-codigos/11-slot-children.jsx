function JanelaFilha(props) {
  return <div>{props.children}</div>;
}

function App() {
  return (
    <JanelaFilha>
      <h1>Ola!</h1>
      <p>este conteudo esta sendo passado como slot props children</p>
    </JanelaFilha>
  );
}

export default App;
