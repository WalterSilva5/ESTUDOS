function Dialog(props) {
  return (
    <div>
      <h1>{props.title}</h1>
      <p>{props.message}</p>
    </div>
  );
}

function App() {
  return (
    <Dialog title="Welcome" message="Thank you for visiting our spacecraft!" />
  );
}
export default App;
