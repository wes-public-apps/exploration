// Wesley Murray
// 2/9/2021
// This program is meant to calculate the area of shapes.

#define _USE_MATH_DEFINES

//compiler directives to import libraries
#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

//determine the area of a rectangle
float rectArea(){
    float length,width;

    //collect dimensions from user
    cout << "Rectangle Dimensions: " << endl;
    cout << "Length: "; cin >> length;
    cout << "Width: "; cin >> width;
    
    //calculate area
    float area = length * width;

    cout << "Area: " << area << endl;

    return area;
}

//determine area of circle
float circleArea(){
    float radius;

    //collect dimensions from user
    cout << "Circle Dimensions: " << endl;
    cout << "Radius: "; cin >> radius;

    //calculate area
    float area = M_PI * pow( radius, 2);

    cout << "Area: " << area << endl;

    return area;
}

//define list of possible args
string argList(){
    return "\
    --rectangle   calculates the area of a rectangle. \n\
    --rect        calculates the area of a rectangle. \n\
    --circle      calculates the area of a circle. \n\
    --help        list possible args. \n";
}

//define run method
int main(int numArgs, char** args){

    // for each arg run associated code
    for(int i = 1; i < numArgs; i++){
        if(!strcmp(args[i],"--rectangle")){
            rectArea();
        } else if (!strcmp(args[i],"--circle")){
            circleArea();
        } else if (!strcmp(args[i],"--help")){
            cout << argList();
        } else {
            cout << args[i] << " is not a valid input." << endl;
        }
    }

    return 0;
}