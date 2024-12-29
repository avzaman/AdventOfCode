/*
create starting wire list
create a wire dict, key is name, value is 0 or 1
create a list of gates, gate has left wire, right wire, out wire, operation type
now operate() on all gates with only starting wires (remove them as you go along)
then operate() on the rest of the gates
create a list of all z wires, order that list
print the binary
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <set>

using namespace std;

struct gate{
    string leftWire;
    string operation;
    string rightWire;
    string outWire;
};

void tokenize(const string& s, vector<string>& tokens, const string& del = " "){
    int start, end = -1*del.size();

    do{
        start = end + del.size();
        end = s.find(del, start);
        tokens.push_back(s.substr(start, end-start));
    } while(end != -1);
}

int main(){
    
    map<string, int> wires;
    vector<struct gate> gates;
    set<string> startingWires;
    
    //open first file with starting wires
    ifstream file("24.txt");
    if(!file){
        cerr << "error opening file\n";
        return 1;
    }

    vector<string> tokens;
    string line;
    string wire;
    int val;

    while(getline(file, line)){
        tokenize(line, tokens, ": ");
        if (tokens.size() < 2) {
            cerr << "Invalid line format: " << line << endl;
            continue;
        }
        wire = tokens[0];
        val = stoi(tokens[1]);
        startingWires.insert(wire);
        wires[wire] = val;
        tokens.clear();
    }
    

    file.close();

    cout << "Printing starting wires:" << endl;
    for(string const& s : startingWires){
        cout << s << ' ';
    }
    cout << endl;

    cout << "Printing current wires map:" << endl;
    for(const auto& pair : wires){
        cout << pair.first << ' ' << pair.second << ", ";
    }
    cout << endl;

    //open second file with gates
    ifstream filetwo("242.txt");
    if(!filetwo){
        cerr << "error opening gate file\n";
        return 1;
    }

    string leftWire;
    string rightWire;
    string outWire;
    string operation;
     

    while(getline(filetwo, line)){
        // cout << line << endl;
        tokenize(line, tokens);
        if (tokens.size() < 5) {
            cerr << "Invalid line format: " << line << endl;
            continue;
        }
        // cout << tokens[0] << endl;
        gate g;
        leftWire = tokens[0];
        operation = tokens[1];
        rightWire = tokens[2];
        outWire = tokens[4];
        gates.push_back({tokens[0],tokens[1],tokens[2],tokens[4]});
        if(wires.find(leftWire) == wires.end()){
            wires[leftWire] = 2;
        }
        if(wires.find(rightWire) == wires.end()){
            wires[rightWire] = 2;
        }
        if(wires.find(outWire) == wires.end()){
            wires[outWire] = 2;
        }
        tokens.clear();
    }

    file.close();

    cout << "Printing current wires map:" << endl;
    for(const auto& pair : wires){
        cout << pair.first << ' ' << pair.second << ", ";
    }
    cout << endl;

    cout << "Printing gates:" << endl;
    for(const gate& g : gates){
        cout << "Gate: " << g.leftWire << " " << g.operation << " " << g.rightWire << " " << g.outWire << endl;
    }
    cout << endl;

}