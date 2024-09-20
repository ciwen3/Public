//-----headers-----

#include <iostream>
#include <cstring>

//-----namespace std.-----

using namespace std;

//-----macro definitions-----

//-----code-----

// start the program
int main()
{

    //-----declaring variables-----
    //example declare: 	string  pid; 
    //example use: 	cin >> pid;

    string cleartext = "", ciphertext = "", crypt = "";
    signed int offset, newoffset;
    char charArray[]= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//    unsigned int KeyNumb = 0;

    // print program information
    cout << "This is a basic Caesar Cipher. \nThis Program was created by Christopher Iwen AKA Strat0m \n\n1. You will be asked to input clear text\n2. choose an offset\n3. determine if [E]ncrypting or [D]ecrypting \nAfter that it will print out the modified text.\n\n";

    //ask for clear text input 
    cout << "Input text\n"; 
    //take input and assign to variable cleartext
    cin >> cleartext; 

    cout << "Input the offset you would like to use\n"; 
    //take input and assign to variable offset
    cin >> offset; 
//    cout << "the offset is: " << offset << "\n";


    //ask if encrypting or decrypting
    cout << "Do you want to [E]ncrypt or [D]ecrypt the text?\n"; 
    //take input and assign to variable cleartext
    cin >> crypt; 

    if (toupper(crypt[0]) == charArray[3]){ //make the first character uppercase and check to see if it is the letter "D"
        offset = offset * -1; //make offset negative
    }

//    cout << "the number of characters in the clear text is: " << size(cleartext) << "\n"; //size of clear text is the number of characters

//    cout << "the number of characters in the charArray is: " << sizeof(charArray) << "\n"; //size of clear text is the number of characters

    for(signed int i = 0; i < size(cleartext); i++){ //for each character in cleartext
//        cout << i << " " << cleartext[i] << "\n"; // Print placement number in cleartext and the letter
        for (signed int k = 0; k < 26; k++){ //for each character in charArray
//            cout << k << " " << charArray[k] << "\n"; // Print placement number in array and the letter
            if (toupper(cleartext[i]) == charArray[k]){ //check to see if the characters match
//                cout << "k equals: " << k << "\n"; 
//                cout << "offset equals: " << offset << "\n"; 
//                cout << "k + offset equals: " << (k + offset) << "\n"; 
                if (k + offset > 25){ //check to see if a correction is needed for a loop around
//                    cout << "k + offset = over 25\n"; 
                    newoffset = offset - 26; //make correction
                    ciphertext += charArray[k + newoffset]; //add modified character to ciphertext variable
//                    cout << "clear text: " << cleartext[i] << " is found at array location: " << charArray[k] << "\n"; // Print character
//                    cout << "clear text: " << cleartext[i] << " will become cipher text: " << charArray[k + newoffset] << "\n"; // Print character
                    break;
                } else if (k + offset < 0){ //check to see if a correction is needed for a negative loop around
//                    cout << "k + offset = less than 0\n"; 
                    newoffset = offset + 26; //make correction
                    ciphertext += charArray[k + newoffset]; //add modified character to ciphertext variable
//                    cout << "clear text: " << cleartext[i] << " is found at array location: " << charArray[k] << "\n"; // Print character
//                    cout << "clear text: " << cleartext[i] << " will become cipher text: " << charArray[k + newoffset] << "\n"; // Print character
                    break;
                } else {
//                    cout << "k + offset = less than 25\n"; 
                    ciphertext += charArray[k + offset]; //add modified character to ciphertext variable
//                    cout << "clear text: " << cleartext[i] << " is found at array location: " << charArray[k] << "\n"; // Print character
//                    cout << "clear text: " << cleartext[i] << " will become cipher text: " << charArray[k + offset] << "\n"; // Print character
                    break;
                }
            } 
        }
    }


    //print cipher text
    cout << "\ninput text: " << cleartext << "\n" << "output text: " << ciphertext << "\n"; //output the original text and the new modified text

//    cout << "the number of characters in the output text is: " << size(ciphertext) << "\n"; //check to make sure all info was taken in and processed


    // exit the program
    return 0;
}
