package _10_Exceptions_e_Scanner;

import java.util.Scanner;

public class Exemplo1 {

    public static void main(String[] args) {
        String nome;
        int numero;
        Scanner input = new Scanner(System.in);

        nome = input.nextLine();

        System.out.println(nome);

        try {
            numero = Integer.parseInt(nome);
        }catch (NumberFormatException e){
            System.out.println("Ocorreu uma exessão do tipo: "+e);
        }
    }
}
