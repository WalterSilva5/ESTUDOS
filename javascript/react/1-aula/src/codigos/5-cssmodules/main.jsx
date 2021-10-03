import ReactDom from 'react-dom';
import App from './App';
import './assets/styles.scss';
import 'bootstrap/dist/css/bootstrap.css';
import store from './store/store';
import { Provider } from 'react-redux';

import {BrowserRouter} from 'react-router-dom'

ReactDom.render(
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>,
  document.getElementById("root")
);