package _4_projeto_seminarios.classes;

public class Seminario {
    private String titulo;//um seminario deve ter um titulo
    private Aluno[] alunos;//um seminario pode ter varios alunos
    private Professor professor;//um seminario so pode ter um professor
    private Local local;// um seminario devera ter um local


    public Seminario(String titulo) {
        this.titulo = titulo;
    }

    public Professor getProfessor() {
        return professor;
    }

    public void setProfessor(Professor professor) {
        this.professor = professor;
    }

    public Local getLocal() {
        return local;
    }

    public void setLocal(Local local) {
        this.local = local;
    }


    public Aluno[] getAlunos() {
        return alunos;
    }

    public void setAlunos(Aluno[] alunos) {
        this.alunos = alunos;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void print(){
        System.out.println("Seminario: "+this.titulo);
        for (int i = 0; i < alunos.length; i++) {
            System.out.println("Aluno: "+i+" - "+this.alunos[i].getNome());
        }
        professor.print();
        local.print();
    }
}
