package _4_projeto_seminarios.classes;

public class Professor {
    private String nome;
    private Seminario[] seminario;//um professor podera ministrar um ou varios seminarios
    private String especialidade;


    public Professor(String nome, String especialidade) {
        this.nome = nome;
        this.especialidade = especialidade;
    }

    public Seminario[] getSeminario() {
        return seminario;
    }

    public void setSeminario(Seminario[] seminario) {
        this.seminario = seminario;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    public void print(){
        System.out.println("Professor: "+this.nome);
        System.out.println("Especialidade: "+this.especialidade);
    }

}
