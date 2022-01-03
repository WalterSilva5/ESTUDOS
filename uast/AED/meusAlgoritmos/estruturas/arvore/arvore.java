class No{
    public Arvore(Integer valor){
        this.valor = valor;
        this.pai = No;
        this.direita = No;
        this.esquerda = No;
    }
}
public class Arvore{
    public Arvore(){
        this.raiz = None;
        this.numeroDeFolhas = 0;
    }

    public add(int valor){
        no = No(valor);
        atual = this.raiz;
        if (atual == None){
            this.raiz = no;
        }
        else{
            this.addRec(this.raiz, atual.direita);
            this.numeroDeFolhas+=1;
        }
    }
    private addRec(No atual,No no,No pai){
        no.pai = pai;

        if(no.valor > atual.valor){
            if (atual.direita == None){
                atual.direita = no
            }
            else{
                this.addRec(atual.direita, no, atual)
            }

        }
    }
}
