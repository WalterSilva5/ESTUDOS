package _3_manipulacao_de_classe;

public class Estudante {
    private String nome;
    private int idade;
    private float[] notas = new float[3];
    private float media;
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public float[] getNotas() {
        return notas;
    }

    public void setNotas(float[] notas) {
        this.notas = notas;
    }

    public String mostrarNotas(){
        this.media = (this.notas[0]+this.notas[1]+this.notas[2])/2;
        return "A media do aluno foi: "+ Float.toString(this.media);
    }
}
