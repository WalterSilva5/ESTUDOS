package _3_manipulacao_de_classe;

public class CriarEstudante {
    public static void main(String[] args) {
        float[] notas={10,5,10};
        Estudante estudante = new Estudante();
        estudante.setIdade(22);
        estudante.setNome("walter");
        estudante.setNotas(notas);
        System.out.println(estudante.mostrarNotas());
    }
}
