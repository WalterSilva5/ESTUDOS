package _5_heranca;


//para usar coisas da super classe usamos ela como super
/*ex: se a superclasse tem um atributo nome
    usamos super.nome para acessar esse nome
 */

public class Trabalhador extends Pessoa {
    public String trabalho;

    public Trabalhador(String nome, String trabalho) {
        super(nome);
        this.trabalho = trabalho;
    }

    public String getTrabalho() {
        return trabalho;
    }

    public void setTrabalho(String trabalho) {
        this.trabalho = trabalho;
    }

    public void print(){
        System.out.println(this.nome+" é um Trabalhador e seu emprego é "+this.trabalho);
    }
}
