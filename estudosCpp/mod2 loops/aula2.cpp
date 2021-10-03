#include <iostream>
using namespace std;

int main(){
    string nome = "walter";
    string sobrenome = " silva \n";

    nome.append(sobrenome);
    cout << nome;
    return 0;
}