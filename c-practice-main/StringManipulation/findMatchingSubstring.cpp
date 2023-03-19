// Wesley Murray
// 2/10/2021
// This script is meant to find all substring references in another string.

#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

//simple method using c string
int* findSubstring(string sub, string sample){
    int matchCount = 0, arrayLen = 2;
    int* indexes=new int[arrayLen];
    int* tempArr;

    //while where are sub string matches
    int index = sample.find(sub);
    while (index!=std::string::npos){
        //if array of indees is too small double the size
        if(arrayLen<=matchCount) {
            tempArr = new int[arrayLen * 2];
            for(int i=0; i<arrayLen; i++){
                tempArr[i]=indexes[i];
            }
            //reset tracking variables
            arrayLen*=2;
            indexes = tempArr;
            cout << "Doubled array: " << arrayLen << endl;
        }

        //add index to list
        indexes[matchCount]=index;

        //search rest of string
        index = sample.find(sub,index+1);

        matchCount++;
    }
    return indexes;
}

//use vectors to find matching substrings
vector<int> findSubstringVector(string sub, string sample){
    vector<int> indicies;

    int index = sample.find(sub);
    while(index!=std::string::npos){
        indicies.push_back(index);
        index = sample.find(sub,index+1);
    }

    return indicies;
}

//define run method
int main(){
    cout << "--------------- Array Based --------------------" << endl;

    //should detect 6 matches
    int* indexes=findSubstring("abc","abciuwrrfabcabcopwerewabceirfrhabcijabcoieruwedhed");
    cout << "Six matches: " << endl;
    for(int i=0;i<sizeof(indexes);i++) cout << indexes[i] << endl;

    //should detect 4 matches
    indexes=findSubstring("abc","abciuwrrfabcabcopwerewabc");
    cout << "Four matches: " << endl;
    for(int i=0;i<sizeof(indexes);i++) cout << indexes[i] << endl;

    //should detect no matches
    indexes = findSubstring("abc","fdghernvsdkergvdfjsd");
    cout << "No matches: " << endl;
    for(int i=0;i<sizeof(indexes);i++) cout << indexes[i] << endl;

    cout << "--------------- Vector Based --------------------" << endl;

    vector<int> indicies=findSubstringVector("abc","abciuwrrfabcabcopwerewabceirfrhabcijabcoieruwedhed");
    cout << "Six matches: " << endl;
    for(auto i=indicies.begin(); i<indicies.end();i++) cout << *i << endl;

    //should detect 4 matches
    indicies=findSubstringVector("abc","abciuwrrfabcabcopwerewabc");
    cout << "Four matches: " << endl;
    for(auto i=indicies.begin(); i<indicies.end();i++) cout << *i << endl;

    //should detect no matches
    indicies = findSubstringVector("abc","fdghernvsdkergvdfjsd");
    cout << "No matches: " << endl;
    for(auto i=indicies.begin(); i<indicies.end();i++) cout << *i << endl;

    return 0;
}