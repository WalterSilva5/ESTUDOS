import ReactDom from "react-dom";
import logo from "./favicon.svg";

class Relogio extends Component {
  constructor(props){
    super(props);
    this.state = {hora: new Date().toLocaleTimeString()}
  }
  render() {
    return(
      <h1>{this.state.hora}</h1>
    )
  }
}

setInterval(() => {
  ReactDom.render(<Relogio />, document.getElementById("root"));
}, 1000);
