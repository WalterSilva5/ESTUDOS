package _7_Modificador_Final;

//quando usamos o modificador final o elemento usado
//nao podera ser mais modificado em outro lugar

public class Carro {
    public static final double VELOCIDADE_FINAL = 240;
    private String nome;
    private String marca;

    @Override
    public String toString() {
        return "Carro{" +
                "nome='" + nome + '\'' +
                ", marca='" + marca + '\'' +
                '}';
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }
}

/*
se colocarmos final em uma classe ela não podera sex extendida
apenas estanciada
então ela é o final de uma extensão de classes

 */