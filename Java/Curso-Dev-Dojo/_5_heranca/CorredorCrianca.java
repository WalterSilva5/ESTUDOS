package _5_heranca;

public class CorredorCrianca extends Atleta {
    public int idade;

    public CorredorCrianca(String nome, String habilidade, int idade){
        super(habilidade, nome);
        setIdade(idade);
    }

    public void setIdade(int idade){
        if(idade>12){
            System.out.println("Essa pessoa não é uma criança");
        }
        else{
            this.idade = idade;
            System.out.println("Cadastrado!");
        }
    }

}
