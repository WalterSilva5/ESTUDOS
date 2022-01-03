const Contador = () => {
  const setCount = React.useContext(CountData);
  return (
    <div>
      <button
        className="btn btn-primary"
        onClick={() => setCount("DECREMENT_1")}
      >
        decrement
      </button>
      <button
        className="btn btn-primary m-2"
        onClick={() => setCount("INCREMENT_1")}
      >
        increment
      </button>
    </div>
  );
};

export const CountData = React.createContext();

const App = () => {
  const countReducer = (state, action) => {
    switch (action) {
      case "INCREMENT_1":
        return {
          ...state,
          count_1: state.count_1 + 1,
        };
      case "DECREMENT_1":
        return {
          ...state,
          count_1: state.count_1 - 1,
        };
      default:
        return state;
    }
  };

  const [count, setCount] = React.useReducer(countReducer, { count_1: 0 });

  return (
    <div>
      <div className="container col-4 text-center border rounded border-secondary p-5 mt-5">
        <h2 className="text-center">
          <b>{count.count_1}</b>
        </h2>
        <CountData.Provider value={setCount}>
          <Contador />
        </CountData.Provider>
      </div>
    </div>
  );
};

export default App;
