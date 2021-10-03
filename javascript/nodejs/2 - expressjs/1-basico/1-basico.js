/* eslint-disable no-console */
import express from 'express';

const app = express();
// rotas
app.get('/', (req, res) => {
  res.send('<h1>INDEX DO PROJETO</h1>');
});
app.get('/teste', (req, res) => {
  res.send('<h1>PAGINA DE TESTE</h1>');
});

app.listen(80, (erro) => {
  if (erro) {
    console.log('ocorreu um erro');
  } else {
    console.log('servidor funcionando');
  }
});
