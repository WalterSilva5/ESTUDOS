package _5_heranca;

public class Atleta extends Pessoa {
    public String habilidade;

    public Atleta(String nome, String habilidade) {
        super(nome);
        this.habilidade = habilidade;
    }

    public String getHabilidade() {
        return habilidade;
    }

    public void setHabilidade(String habilidade) {
        this.habilidade = habilidade;
    }

    public void print(){
        System.out.println(this.nome+" é um atleta e sua habilidade é "+this.habilidade);
    }
}
