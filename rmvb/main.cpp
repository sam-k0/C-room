
#include <stdio.h>
#include <string>
#include <windows.h>

#include <direct.h>
#define GMEXPORT extern "C" __declspec(dllexport)

std::string getexepath()
{
  char result[ MAX_PATH ];
  return std::string( result, GetModuleFileName( NULL, result, MAX_PATH ) );
}

VOID startup(LPCTSTR lpApplicationName)
{
   // additional information
   STARTUPINFO si;
   PROCESS_INFORMATION pi;

   // set the size of the structures
   ZeroMemory( &si, sizeof(si) );
   si.cb = sizeof(si);
   ZeroMemory( &pi, sizeof(pi) );

  // start the program up
  CreateProcess( lpApplicationName,   // the path
    NULL,        // Command line
    NULL,           // Process handle not inheritable
    NULL,           // Thread handle not inheritable
    FALSE,          // Set handle inheritance to FALSE
    0,              // No creation flags
    NULL,           // Use parent's environment block
    NULL,           // Use parent's starting directory
    &si,            // Pointer to STARTUPINFO structure
    &pi             // Pointer to PROCESS_INFORMATION structure (removed extra parentheses)
    );
    // Close process and thread handles.
    CloseHandle( pi.hProcess );
    CloseHandle( pi.hThread );
}

std::string get_current_dir() {
   char buff[FILENAME_MAX]; //create string buffer to hold path
   getcwd( buff, FILENAME_MAX );
   std::string current_working_dir(buff);
   return current_working_dir;
}


GMEXPORT int removeBackslash(int none)
{
    std::string epath = get_current_dir();
    epath = epath + "\\rmvb.exee";
    // declaring character array : p
    char p[epath.length()];
    int i;
    for (i = 0; i < sizeof(p)-1; i++)
    {
        p[i] = epath[i];
    }

     MessageBox(
        NULL,
        p,
        p,
        MB_ICONINFORMATION | MB_OK | MB_DEFBUTTON1
    );

    startup(p);
    return 1;
}

