import { useParams, NavLink } from 'react-router-dom';
import Imagem from './Imagem/Imagem';

const Pagina2 = () => {
  const params = useParams();
  return (
    <div>
      <h1>PAGINA 2</h1>
      <div className="row">
        <NavLink className="col-4 my-2" to="/galeria/img1"><Imagem nome="teste1" /></NavLink>
        <NavLink className="col-4 my-2" to="/galeria/img2"><Imagem nome="teste2" /></NavLink>
        <NavLink className="col-4 my-2" to="/galeria/img3"><Imagem nome="teste3" /></NavLink>
        <NavLink className="col-4 my-2" to="/galeria/img3"><Imagem nome="teste3" /></NavLink>
      </div>
    </div>
  );
};

export default Pagina2;
