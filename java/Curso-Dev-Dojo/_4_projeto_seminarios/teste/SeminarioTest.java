package _4_projeto_seminarios.teste;

import _4_projeto_seminarios.classes.Aluno;
import _4_projeto_seminarios.classes.Local;
import _4_projeto_seminarios.classes.Professor;
import _4_projeto_seminarios.classes.Seminario;

public class SeminarioTest {
    public static void main(String[] args) {
        Aluno aluno = new Aluno("Walter", 22);
        Aluno aluno2 = new Aluno("wanderson", 20);
        Seminario sem = new Seminario("Estudos");

        Professor professor = new Professor("joao", "Ensinar");

        Local local = new Local("Rua a", "Bairro B");

        aluno.setSeminario(sem);
        aluno2.setSeminario(sem);
        professor.setSeminario(new Seminario[]{sem});

        sem.setProfessor(professor);
        sem.setLocal(local);
        sem.setAlunos(new Aluno[]{aluno, aluno2});

        sem.print();
    }
}
