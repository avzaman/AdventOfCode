#include <iostream>
#include <fstream>
using namespace std;

int main(){
    fstream file("1.txt", ios::in);
    int zeros = 0, dial = 50, turn = 0;
    string line;
    while(!file.eof()){
        getline(file, line);
        if(line[0]=='L'){
            turn = stoi(line.substr(1))%100;
            dial -= turn;
            if(dial<0){
                dial = dial+100;
            }
        }else{
            turn = stoi(line.substr(1))%100;
            dial += turn;
            if(dial>99){
                dial = dial-100;
            }
        }
        cout << "Dial set to: " << dial << " after turning: " << turn << endl;
        if(dial == 0){
            zeros++;
        }
    }

    cout << "Num zeros: " << zeros << endl;
    return 0;
}