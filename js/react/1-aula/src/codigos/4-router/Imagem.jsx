import { useParams } from 'react-router';

const Imagem = (props) => {
  const params = useParams();
  const { nome } = props;
  return (
    <div className="border border-warning rounded" style={{ height: '300px', width: '300px' }}>
      <h4 className="text-center">{nome}</h4>
      <h4>{ params.imagem}</h4>
    </div>
  );
};

export default Imagem;
