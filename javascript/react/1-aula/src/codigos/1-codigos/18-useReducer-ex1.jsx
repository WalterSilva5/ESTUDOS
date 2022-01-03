const FormInputs = () => {
  const loginReducer = (state, action) => {
    return action;
  };

  const senhaReducer = (state, action) => {
    return action;
  };

  const [login, setlogin] = React.useReducer(loginReducer, "");

  const [senha, setsenha] = React.useReducer(senhaReducer, "");
  const setFormValid = React.useContext(UserData);

  React.useEffect(() => {
    if (login.includes("@") && senha.length > 5) {
      setFormValid(true);
    } else {
      setFormValid(false);
    }
  }, [login, senha]);

  return (
    <div>
      <label>login</label>
      <input
        type="text"
        className="form-control"
        value={login}
        onChange={(e) => setlogin(e.target.value)}
      />
      <label>Senha</label>
      <input
        className="form-control"
        value={senha}
        onChange={(e) => setsenha(e.target.value)}
      />
    </div>
  );
};

export const UserData = React.createContext();

const App = () => {
  const [formValid, setFormValid] = React.useState(false);

  return (
    <div className="align-middle container border border-secondary rounded mt-5">
      <div className="row d-flex justify-content-center my-5">
        <div className="container col-8">
          <UserData.Provider value={setFormValid}>
            <FormInputs />
          </UserData.Provider>
          <div className="d-flex justify-content-end mt-2">
            <div className="mx-4">
              {formValid ? (
                <span>form valido</span>
              ) : (
                <span>form invalido</span>
              )}
            </div>
            <button className="btn btn-primary">ENTRAR</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
