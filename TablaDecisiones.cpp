#include <iostream>
#include <cmath>
#include <windows.h>
using namespace std;

int main(){
    int auxi, nd, ne;
    float auxf, alfa, sum, ve, min, max, lap, hur, sav;
    system("cls");
    cout<<"Ingrese el numero de Decisiones: "; cin>>nd;
    cout<<"Ingrese el numero de Estados: "; cin>>ne;
    float M[nd+1][ne+6];
    //probabilidades
    for(int i=0; i<ne; i++){
        cout<<"Ingrese la probabilidad del Estado "<<i+1<<": "; cin>>auxf;
        M[nd][i]=auxf;
    }
    //Ingreso de datos
    for(int i=0; i<nd; i++){
        for (int j=0; j<ne; j++){
            cout<<"Decision "<<i+1<<" Estado "<<j+1<<": "; cin>>auxf;
            M[i][j]=auxf;
        }
    }
    //Desarrollo
    //Valor esperado, Pesimista, Maximista, Laplace, Hurwikz
    alfa=0.5;
    for(int i=0; i<nd; i++){
        min=M[i][0];
        max=M[i][0];
        sum=M[i][0];
        M[i][ne]=M[i][0]*M[nd][0];
        for (int j=1; j<ne; j++){
            M[i][ne]=M[i][ne]+M[i][j]*M[nd][j];
            if(M[i][j]<min){
                min=M[i][j];
            }
            if(M[i][j]>max){
                max=M[i][j];
            }
            sum=sum+M[i][j];
        }
        hur=(max*alfa)+(min*(1-alfa));
        lap=sum/ne;
        M[i][ne+1]=min;
        M[i][ne+2]=max;
        M[i][ne+3]=lap;
        M[i][ne+4]=hur;
    }
    //Savage
    for(int j=0; j<ne; j++){
        max=M[0][j];
        for (int i=1; i<nd; i++){
            if(M[i][j]>max){
                max=M[i][j];
            }
        }
        if(j==0){
            for (int i=0; i<nd; i++){
                M[i][ne+5]=abs(M[i][j]-max);
            }
        }else{
            for (int i=0; i<nd; i++){
                if(abs(M[i][j]-max)>M[i][ne+5]){
                    M[i][ne+5]=abs(M[i][j]-max);
                }
            }
        }
    }
    //Impresion de la matriz
    cout<<endl;
    for(int i=0; i<nd; i++){
        for (int j=0; j<ne+6; j++){
            cout<<"\t"<<M[i][j];
            if(j==ne-1){
                cout<<"\t|";
            }
        }
        cout<<endl;
    }
    cout<<endl;
}