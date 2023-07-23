package _2_Relacionamento_entre_classes;

public class Pessoa {
    public static void main(String[] args){
        Telefone numero =  new Telefone();
        String nome = "walter";
        numero.numero=1;
        System.out.println("Nome: "+nome+", Numero: "+numero.numero);
    }
}
