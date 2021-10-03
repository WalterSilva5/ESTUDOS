package _8_Classes_abstratas;

public class Gerente extends Funcionario {
    @Override
    public void calculaSalario(double salario) {
        this.salario = salario + ( salario * 0.5);
    }
}
