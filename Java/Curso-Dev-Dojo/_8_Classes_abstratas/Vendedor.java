package _8_Classes_abstratas;

public class Vendedor extends Funcionario {
    @Override
    public void calculaSalario(double salario) {
        this.salario = salario + ( salario * 0.1);
    }
}
