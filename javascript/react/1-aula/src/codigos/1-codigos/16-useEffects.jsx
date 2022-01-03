function LoginScreen(props) {
  const [login, setLogin] = React.useState("");
  const [loginValido, setLoginValido] = React.useState(false);

  /*

  o use effect funciona como uma maneira de manipular a parte de tras da aplicação
  a cada alteração e uma de suas dependencias ele manipula algo definido

  */

  React.useEffect(() => {
    login.includes("@") ? setLoginValido(true) : setLoginValido(false);
  }, [login]);

  const mudarLogin = (e) => {
    setLogin(e.target.value);
  };

  return (
    <div className="align-middle container border border-secondary rounded mt-5">
      <div className="row d-flex justify-content-center my-5">
        <div className="container col-8">
          <label>
            <b>Login</b>
          </label>
          <input className="form-control" onChange={mudarLogin} value={login} />
          <div className="d-flex justify-content-end mt-2">
            <div className="mx-4">
              {loginValido ? (
                <span>login valido</span>
              ) : (
                <span>login invalido</span>
              )}
            </div>
            <button className="btn btn-primary">ENTRAR</button>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return <LoginScreen />;
}

export default App;
