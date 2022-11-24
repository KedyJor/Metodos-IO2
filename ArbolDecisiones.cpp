#include <iostream>
#include <cmath>
int numeracion=1;
using namespace std;
class Nodo{
public:
    string tipo;
    int dato;
    float prob=0;
    float cost;
    float resp;
    Nodo* sig[10];
    int cs=0;
};

float arboldecision(Nodo* a, int cont){
    int auxi;
    float auxf, max, sum;
    cout<<"Tipo de Nodo: ";cin>>a->tipo;
    if(a->tipo=="d"){
        max=0;
        a->dato=numeracion;
        cout<<"Ramas del Nodo "<<numeracion<<": ";cin>>auxi;
        numeracion++;
        for(int i=0;i<auxi;i++){
            Nodo *nuevo_nodo=new Nodo();
            a->sig[i]=nuevo_nodo;
            auxf=arboldecision(a->sig[i],cont+1);
            if(auxf>max){
                max=auxf;
            }
            a->cs++;
        }
        a->cost=max;
        if(a->prob!=0){
            a->resp=a->cost*a->prob;
        }else{
            a->resp=a->cost;
        }
    }
    if(a->tipo=="p"){
        sum=0;
        a->dato=numeracion;
        cout<<"Ramas del Nodo "<<numeracion<<": ";cin>>auxi;
        numeracion++;
        for(int i=0;i<auxi;i++){
            Nodo *nuevo_nodo=new Nodo();
            a->sig[i]=nuevo_nodo;
            cout<<"Probabilidad del Nodo "<<numeracion+i<<": ";cin>>a->sig[i]->prob;
            auxf=arboldecision(a->sig[i],cont+1);
            sum=sum+auxf;
            a->cs++;
        }
		a->cost=sum;
		if(a->prob!=0){
			a->resp=a->cost*a->prob;
		}else{
			a->resp=a->cost;
		}
    }
    if(a->tipo=="t"){
        a->dato=numeracion;
        numeracion++;
        cout<<"Ingrese el costo: ";cin>>a->cost;
        if(a->prob!=0){
            a->resp=a->cost*a->prob;
        }else{
            a->resp=a->cost;
        }
    }
    return a->resp;
}

void mostrararbol(Nodo* a, int cont){
    if(a->cs>=0){
        for(int i=0;i<(a->cs);i++){
            mostrararbol(a->sig[i],cont+1);
        }
    }
    for(int i=0;i<cont;i++){cout<<"\t\t\t";} 
    if(a->prob!=0){
        cout<<a->tipo<<": "<<a->dato<<" : "<<a->cost<<endl;
    }else{
        cout<<a->tipo<<": "<<a->dato<<" : "<<a->resp<<endl;
    }
    
}

int main(){
    system("cls");
    Nodo a;
    cout<<"comenzando"<<endl;
    arboldecision(&a,1);
    mostrararbol(&a,1);
    cout<<"fin"<<endl;
}