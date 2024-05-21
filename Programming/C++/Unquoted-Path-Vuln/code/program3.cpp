#include <iostream>
#include <string>
#include <cstdlib>

#include <iomanip>  // timestamp
#include <ctime>    // timestamp

using namespace std;

int main()
{
    // declaring variables:
    string  pid;

    // print information:
    printf("This Program was created by Christopher Iwen AKA Strat0m\nto find unquoted path vulnerabilities in Windows programs\nyou can download the source code for this at https://github.com/ciwen3/Public/tree/master/C%2B%2B/Unquoted-Path-Vuln \n\n");
    
    // print timestamp from https://en.cppreference.com/w/cpp/chrono/c/localtime
    std::time_t t = std::time(nullptr);
    std::cout << "TimeStamp: " << std::put_time(std::localtime(&t), "%c %Z") << '\n';

    // run commands:
    printf("\n\nUser this command was run as:\n");
    system("whoami");
    printf("\n");
    
    system("whoami /priv");
    printf("\n");
    
    printf("To find the command that called Program.exe run:\n");
    printf("wmic process where name='program.exe' get commandline\n");
    system("wmic process where name='program.exe' get commandline");
    printf("\n");
    
    printf("To find the process ID for the command that called Program.exe run:\n");
    printf("wmic process where name='program.exe' get parentprocessid\n");
    system("wmic process where name='program.exe' get parentprocessid");
    printf("\n");
    
    cout << "type the first number that was returned by the last command: ";
    cin >> pid;
    printf("To find the location of the Program that called Program.exe run:\n");
    printf(("wmic process where processid="+pid+" get commandline\n").c_str());
    system(("wmic process where processid="+pid+" get commandline").c_str());
    printf("\n");
    printf("\n");
    
    cout << "type the second number that was returned by the last command. if none type 0: ";
    cin >> pid;
    printf("To find the location of the Program that called Program.exe run:\n");
    printf(("wmic process where processid="+pid+" get commandline\n").c_str());
    system(("wmic process where processid="+pid+" get commandline").c_str());
    printf("\n");
    printf("\n");
    
    cout << "type the third number that was returned by the last command. if none type 0: ";
    cin >> pid;
    printf(
    printf(("wmic process where processid="+pid+" get commandline\n").c_str());
    system(("wmic process where processid="+pid+" get commandline").c_str());
    printf("\n");
    printf("\n");
    
    printf("To find Installed Programs that have un-quoted path vulnerabilites:\n");
    printf("wmic service get name, pathname, displayname, startmode | findstr /i /v "C:\Windows\\" | findstr /i /v """\n");
    system("wmic service get name, pathname, displayname, startmode | findstr /i /v "C:\Windows\\" | findstr /i /v """");
    printf("\n");
    
    system("pause");
    
    return 0;
}
