function Relogio(props) {
  const [hora, setHora] = React.useState("");
  setInterval(() => {
    setHora(new Date().toLocaleTimeString());
  }, 1000);

  return (
    <div>
      <h2>Agora são: {hora}</h2>
    </div>
  );
}

const App = () => {
  return <Relogio />;
};

export default App;
