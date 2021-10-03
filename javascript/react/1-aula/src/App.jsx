/* eslint-disable jsx-a11y/anchor-is-valid */
import { Route, NavLink, Switch, Redirect } from 'react-router-dom';
import Imagem from './Imagem/Imagem';
import Pagina1 from './Pagina_1';
import Pagina2 from './Pagina_2';

const App = () => (
  <div>
    <div>
      <NavLink
        activeClassName="btn-danger"
        className="btn btn-primary mx-2"
        exact
        to="/"
      >
        INDEX
      </NavLink>
      <NavLink
        activeClassName="btn-danger"
        className="btn btn-primary mx-2"
        to="/pagina1"
      >
        PAGINA 1
      </NavLink>
      <NavLink
        activeClassName="btn-danger"
        className="btn btn-primary mx-2"
        to="/galeria"
      >
        GALERIA
      </NavLink>
    </div>
    <hr />
    <Switch>
      <Route exact path="/">
        <Redirect to="/index" />
      </Route>
      <Route exact path="/index">
        <h1>INDEX</h1>
      </Route>
      <Route exact path="/pagina1">
        <Pagina1 />
      </Route>
      <Route exact path="/galeria">
        <Pagina2 />
      </Route>
      <Route path="/galeria/:imagem">
        <Imagem />
      </Route>
      <Route path="*">
        <h1>ERROR 404: PAGE NOT FOUND!</h1>
      </Route>
    </Switch>
  </div>
);
export default App;
