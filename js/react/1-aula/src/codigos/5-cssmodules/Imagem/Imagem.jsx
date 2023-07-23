import { useParams } from 'react-router';

import classes from "./Imagem.module.scss"

const Imagem = (props) => {
  const params = useParams();
  const { nome } = props;
  return (
    <div className={`border border-warning rounded ${classes.testeDiv}`}>
      <h4 className="text-center">{nome}</h4>
      <h4>{ params.imagem}</h4>
    </div>
  );
};

export default Imagem;
