package _9_interfaces;


/*
uma interface vai dizer oq a classe faz mas não vai dizer como
ex: uma interface é uma classe abstrata
porem completamente abstrata
sem implementar nada!
 */
public interface Produto {

    //todos os atributos da interface devem ser constantes
    public static final String NOME = "walter";

    //todos os metodos da interface devem ser abstratos
    public abstract void vender();
}
