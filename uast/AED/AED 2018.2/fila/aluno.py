class Aluno:
    def __init__(self, nome, cpf, nota = None):
        self.nome = nome
        self.cpf = cpf
        self.nota = nota

    def tem_nota(self):
        if self.nota is None:
            return 'Não tem nota'
        else:
            situação = '{:.2f} '.format(self.nota)
            if self.nota >= 7.0:
                situação += '(aprovado)'
            else:
                situação += '(ainda não aprovado)'

            return situação
    