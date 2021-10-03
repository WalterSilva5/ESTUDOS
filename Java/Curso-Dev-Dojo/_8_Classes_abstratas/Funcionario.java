package _8_Classes_abstratas;

//uma classe abstrata nao pode ser extendida
public abstract class Funcionario {
    public String nome;
    public double salario;

    public abstract void calculaSalario(double salario);
    //esse metodo deve ser implementado na classe filha

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}
