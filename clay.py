# Clay: A global runtime made for all languages and platforms, clay is not a language!
# Supported languages: Python, Lua, Ruby, Swift, JavaScript, TypeScript, C, C++, C#, Java, Go, Rust, Kotlin, PHP, and Dart.
# Supported platforms: Windows, Linux, and macOS.
# Supported package managerds: pip, npm, and cargo, go, pip, luarocks, git, and gem.
# Supported shell languages: python, lua, php, swift, perl

# libraries
import os
import json
from os.path import exists
from simple_colors import *
import sys
from distutils.spawn import find_executable
import threading
import simplejson as json
import json_parser
import shutil
from multiprocessing import Process
from subprocess import call
# variables
commands = []
runInstall = True
# run functions
def execute(script):
    if script.endswith(".py"):
        runPython(script)
    elif script.endswith(".lua"):
        runLua(script)
    elif script.endswith(".rb"):
        runRuby(script)
    elif script.endswith(".swift"):
        runSwift(script)
    elif script.endswith(".js"):
        runJS(script)
    elif script.endswith(".ts"):
        runTS(script)
    elif script.endswith(".c"):
        runC(script)
    elif script.endswith(".cpp"):
        runCpp(script)
    elif script.endswith(".cs"):
        runCS(script)
    elif script.endswith(".java"):
        runJava(script)
    elif script.endswith(".go"):
        runGo(script)
    elif script.endswith(".rs"):
        runRust(script)
    elif script.endswith(".kt"):
        runKotlin(script)
    elif script.endswith(".php"):
        runPHP(script)
    elif script.endswith(".dart"):
        runDart(script)
    else:
        print("Unsupported file type. Supported file types are: Python, Lua, Ruby, Swift, JavaScript, TypeScript, C, C++, C#, Java, Go, Rust, Kotlin, PHP, and Dart.")
def utilExists(name):
    return find_executable(name) is not None
def runCommand(command):
    print("Running command: "+command)
    os.system(command)
    
# languages
def runPython(scriptPath):
    if utilExists("python") == False:
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install lua")
            else:
                print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install python3")
            else:
                print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install python3")
            else:
                print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but you need brew.")
        else:
            print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "from clayForPython import *\n"+script

    # use the exec function to run the script, ex: exec(open('file.py').read())
    script = "from clayForPython import *\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    call(["python", scriptPath])
    with open(scriptPath, 'w') as f:
        f.write(orig)

def runLua(scriptPath):
    if utilExists("lua") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install lua")
            else:
                print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install lua")
            else:
                print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install lua")
            else:
                print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but you need brew.")
        else:
            print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForLua')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("lua "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runRuby(scriptPath):
    if utilExists("ruby") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install ruby")
            else:
                print("Ruby is required to run this script. You can install it from https://ruby.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install ruby")
            else:
                print("Ruby is required to run this script. You can install it from https://ruby.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install ruby")
            else:
                print("Ruby is required to run this script. You can install it from https://ruby.org, We tried to install it for you, but you need brew.")
        else:
            print("Ruby is required to run this script. You can install it from https://ruby.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForRuby')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("ruby "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runSwift(scriptPath):
    if utilExists("swift") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install swift")
            else:
                print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install swift")
            else:
                print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install swift")
            else:
                print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but you need brew.")
        else:
            print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForSwift')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("swift "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runC(scriptPath):
    if utilExists("gcc") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install gcc")
            else:
                print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install gcc")
            else:
                print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install gcc")
            else:
                print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but you need brew.")
        else:
            print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "#include <clayForC.h>\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("gcc "+scriptPath)
    runCommand("./a.out")
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runKotlin(scriptPath):
    if utilExists("kotlinc") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install kotlin")
            else:
                print("Kotlin is required to run this script. You can install it from https://kotlinlang.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install kotlin")
            else:
                print("Kotlin is required to run this script. You can install it from https://kotlinlang.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install kotlin")
            else:
                print("Kotlin is required to run this script. You can install it from https://kotlinlang.org, We tried to install it for you, but you need brew.")
        else:
            print("Kotlin is required to run this script. You can install it from https://kotlinlang.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForKotlin')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("kotlinc "+scriptPath)
    runCommand("kotlin "+scriptPath.replace(".kt", ""))
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runJava(scriptPath):
    if utilExists("javac") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install java")
            else:
                print("Java is required to run this script. You can install it from https://java.com, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install java")
            else:
                print("Java is required to run this script. You can install it from https://java.com, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install java")
            else:
                print("Java is required to run this script. You can install it from https://java.com, We tried to install it for you, but you need brew.")
        else:
            print("Java is required to run this script. You can install it from https://java.com, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForJava')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("javac "+scriptPath)
    runCommand("java "+scriptPath.replace(".java", ""))
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runCpp(scriptPath):
    if utilExists("g++") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install gcc")
            else:
                print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install gcc")
            else:
                print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install gcc")
            else:
                print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but you need brew.")
        else:
            print("GCC is required to run this script. You can install it from https://gcc.gnu.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForCpp')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("g++ "+scriptPath)
    runCommand("./a.out")
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runCS(scriptPath):
    if utilExists("csc") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install csc")
            else:
                print("C# is required to run this script. You can install it from https://dotnet.microsoft.com, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install csc")
            else:
                print("C# is required to run this script. You can install it from https://dotnet.microsoft.com, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install csc")
            else:
                print("C# is required to run this script. You can install it from https://dotnet.microsoft.com, We tried to install it for you, but you need brew.")
        else:
            print("C# is required to run this script. You can install it from https://dotnet.microsoft.com, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForCsharp')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("csc "+scriptPath)
    runCommand("mono "+scriptPath.replace(".cs", ""))
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runHTML(scriptPath):
    if utilExists("firefox") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install firefox")
            else:
                print("Firefox is required to run this script. You can install it from https://firefox.com, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install firefox")
            else:
                print("Firefox is required to run this script. You can install it from https://firefox.com, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install firefox")
            else:
                print("Firefox is required to run this script. You can install it from https://firefox.com, We tried to install it for you, but you need brew.")
        else:
            print("Firefox is required to run this script. You can install it from https://firefox.com, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForHTML')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("firefox "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runRust(scriptPath):
    if utilExists("rustc") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install rust")
            else:
                print("Rust is required to run this script. You can install it from https://rust-lang.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install rust")
            else:
                print("Rust is required to run this script. You can install it from https://rust-lang.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install rust")
            else:
                print("Rust is required to run this script. You can install it from https://rust-lang.org, We tried to install it for you, but you need brew.")
        else:
            print("Rust is required to run this script. You can install it from https://rust-lang.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForRust')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("rustc "+scriptPath)
    runCommand("./a.out")
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runJS(scriptPath):
    if utilExists("node") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install nodejs")
            else:
                print("Node is required to run this script. You can install it from https://nodejs.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install nodejs")
            else:
                print("Node is required to run this script. You can install it from https://nodejs.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install nodejs")
            else:
                print("Node is required to run this script. You can install it from https://nodejs.org, We tried to install it for you, but you need brew.")
        else:
            print("Node is required to run this script. You can install it from https://nodejs.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForJS')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("node "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runTS(scriptPath):
    if utilExists("tsc") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install typescript")
            else:
                print("TypeScript is required to run this script. You can install it from https://typescriptlang.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install typescript")
            else:
                print("TypeScript is required to run this script. You can install it from https://typescriptlang.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install typescript")
            else:
                print("TypeScript is required to run this script. You can install it from https://typescriptlang.org, We tried to install it for you, but you need brew.")
        else:
            print("TypeScript is required to run this script. You can install it from https://typescriptlang.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForTS')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("tsc "+scriptPath)
    runCommand("node "+scriptPath.replace(".ts", ".js"))
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runDart(scriptPath):
    if utilExists("dart") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install dart")
            else:
                print("Dart is required to run this script. You can install it from https://dart.dev, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install dart")
            else:
                print("Dart is required to run this script. You can install it from https://dart.dev, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install dart")
            else:
                print("Dart is required to run this script. You can install it from https://dart.dev, We tried to install it for you, but you need brew.")
        else:
            print("Dart is required to run this script. You can install it from https://dart.dev, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForDart')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("dart "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runGo(scriptPath):
    if utilExists("go") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install golang")
            else:
                print("Go is required to run this script. You can install it from https://golang.org, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install golang")
            else:
                print("Go is required to run this script. You can install it from https://golang.org, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install golang")
            else:
                print("Go is required to run this script. You can install it from https://golang.org, We tried to install it for you, but you need brew.")
        else:
            print("Go is required to run this script. You can install it from https://golang.org, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForGo')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("go run "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runPHP(scriptPath):
    if utilExists("php") == False:
        # Check operating system
        if sys.platform == "win32":
            # Check if they have choclatey installed
            if utilExists("choco") == True:
                runCommand("choco install php")
            else:
                print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but you need choco.")
        elif sys.platform == "linux":
            # Check if they have apt installed
            if utilExists("apt") == True:
                runCommand("sudo apt install php")
            else:
                print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but you need apt.")
        elif sys.platform == "darwin":
            # Check if they have brew installed
            if utilExists("brew") == True:
                runCommand("brew install php")
            else:
                print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but you need brew.")
        else:
            print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but we couldn't detect your operating system.")
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForPHP')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("php "+scriptPath)
    with open(scriptPath, 'w') as f:
        f.write(orig)    

# commands
def help():
    print(blue("clay", ['bold'])+": the only runtime you need, supports hundreds of languages while maintaining dazzling speeds.\n\nCommands:\n "+blue("clay new", ['bold'])+" \t\t\t\t create a new project \n "+yellow("clay run", ['bold'])+" \t\t\t\t run a command in the project \n "+green("clay install", ['bold'])+" \t\t\t\t install a package in the project \n "+green("clay uninstall", ['bold'])+" \t\t\t uninstall a package in the project \n "+green("clay list", ['bold'])+" \t\t\t\t list all packages in the project  \n "+green("clay clear", ['bold'])+" \t\t\t\t clear all packages in the project \n "+green("clay add", ['bold'])+" \t\t\t\t add a package in the package.json file \n "+green("clay remove", ['bold'])+" \t\t\t\t remove a package in the package.json file \n "+ magenta("clay help", ['bold'])+" \t\t\t\t show this message \n "+magenta("clay pref", ['bold'])+" \t\t\t\t configurate a package or clay \n\n Options: \n "+black("--version", ['dim'])+" \t\t\t\t show the version number")
    main()
def void():
    runInstall = False
    print("Blocked")
    main()
def add(nm="void", p="void"):
    called = nm == "void" and p == "void"
    # check if package.json exists
    if not exists("package.json"):
        print("No package.json file found. Run "+blue("clay new", ['bold'])+" to create a new project.")
        main()
    else:
        # read package.json
        if nm == "void":
            nm = input("Package name: ")
        if p == "void":
            p = input("Package provider: ")
        
        with open('package.json', 'r') as f:
            dataTable = json.loads(f.read())
        
        # append nm into dataTable.dependencies (dict)
        # dataTable['dependencies'][""]({"name": nm, "provider": p})
        # ADD LATER
    if called:
        main()
def remove(nm):
    # check if package.json exists
    if not exists("package.json"):
        print("No package.json file found. Run "+blue("clay new", ['bold'])+" to create a new project.")
        main()
    else:
        # read package.json
        with open('package.json', 'r') as f:
            dataTable = json.loads(f.read())
        # find a item in dataTable.dependencies with name nm
        for i in dataTable['dependencies']:
            if i.name == nm:
                dataTable['dependencies'].remove(i)
        
        
        # write package.json
        with open('package.json', 'w') as f:
            f.write(json.dumps(dataTable))

    main()

def new():
    cwd = os.getcwd()
    name = input("Project name (identifier for your project): ")
    script = input("Script name (which file to run on start): ")
    version = input("Version (current version, recommended: 1.0.0): ")
    author = input("Author (developers): ")
    description = input("Description (information about your project): ")

    print("Creating new project in "+cwd)

    dataTable = {
        "name": name,
        "version": version,
        "author": author,
        "description": description,
        "script": script,
        "dependencies": {}
    }
    if not exists("dependencies"):
        os.mkdir("dependencies")

    if not exists(script):
        with open(script, 'w') as f:
            f.write("")

    with open('package.json', 'w') as f:
        f.write(json.dumps(dataTable))

    main()

def shell():
    lang = input("Language: ")

    print("Click "+blue("CTRL+C", ['bold'])+" to exit the shell. Or you can terminate the terminal.")
    print("The shell lets you use the original version of the language, Not with the clay additions.")
    if lang == "python":
        if utilExists("python") == False:
            # Check operating system
            if sys.platform == "win32":
                # Check if they have choclatey installed
                if utilExists("choco") == True:
                    os.system("choco install python")
                else:
                    print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but you need choco.")
            elif sys.platform == "linux":
                # Check if they have apt installed
                if utilExists("apt") == True:
                    os.system("sudo apt install python")
                else:
                    print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but you need apt.")
            elif sys.platform == "darwin":
                # Check if they have brew installed
                if utilExists("brew") == True:
                    os.system("brew install python")
                else:
                    print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but you need brew.")
            else:
                print("Python is required to run this script. You can install it from https://python.org, We tried to install it for you, but we couldn't detect your operating system.")
        os.system("python")
    elif lang == "php":
        if utilExists("php") == False:
            # Check operating system
            if sys.platform == "win32":
                # Check if they have choclatey installed
                if utilExists("choco") == True:
                    os.system("choco install php")
                else:
                    print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but you need choco.")
            elif sys.platform == "linux":
                # Check if they have apt installed
                if utilExists("apt") == True:
                    os.system("sudo apt install php")
                else:
                    print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but you need apt.")
            elif sys.platform == "darwin":
                # Check if they have brew installed
                if utilExists("brew") == True:
                    os.system("brew install php")
                else:
                    print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but you need brew.")
            else:
                print("PHP is required to run this script. You can install it from https://php.net, We tried to install it for you, but we couldn't detect your operating system.")
        os.system("php -a")
    elif lang == "swift":
        if utilExists("swift") == False:
            # Check operating system
            if sys.platform == "win32":
                # Check if they have choclatey installed
                if utilExists("choco") == True:
                    os.system("choco install swift")
                else:
                    print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but you need choco.")
            elif sys.platform == "linux":
                # Check if they have apt installed
                if utilExists("apt") == True:
                    os.system("sudo apt install swift")
                else:
                    print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but you need apt.")
            elif sys.platform == "darwin":
                # Check if they have brew installed
                if utilExists("brew") == True:
                    os.system("brew install swift")
                else:
                    print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but you need brew.")
            else:
                print("Swift is required to run this script. You can install it from https://swift.org, We tried to install it for you, but we couldn't detect your operating system.")
        os.system("swift")
    elif lang == "perl":
        if utilExists("perl") == False:
            # Check operating system
            if sys.platform == "win32":
                # Check if they have choclatey installed
                if utilExists("choco") == True:
                    os.system("choco install perl")
                else:
                    print("Perl is required to run this script. You can install it from https://perl.org, We tried to install it for you, but you need choco.")
            elif sys.platform == "linux":
                # Check if they have apt installed
                if utilExists("apt") == True:
                    os.system("sudo apt install perl")
                else:
                    print("Perl is required to run this script. You can install it from https://perl.org, We tried to install it for you, but you need apt.")
            elif sys.platform == "darwin":
                # Check if they have brew installed
                if utilExists("brew") == True:
                    os.system("brew install perl")
                else:
                    print("Perl is required to run this script. You can install it from https://perl.org, We tried to install it for you, but you need brew.")
            else:
                print("Perl is required to run this script. You can install it from https://perl.org, We tried to install it for you, but we couldn't detect your operating system.")
        os.system("perl -del")
    elif lang == "lua":
        if utilExists("lua") == False:
            # Check operating system
            if sys.platform == "win32":
                # Check if they have choclatey installed
                if utilExists("choco") == True:
                    os.system("choco install lua")
                else:
                    print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but you need choco.")
            elif sys.platform == "linux":
                # Check if they have apt installed
                if utilExists("apt") == True:
                    os.system("sudo apt install lua")
                else:
                    print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but you need apt.")
            elif sys.platform == "darwin":
                # Check if they have brew installed
                if utilExists("brew") == True:
                    os.system("brew install lua")
                else:
                    print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but you need brew.")
            else:
                print("Lua is required to run this script. You can install it from https://lua.org, We tried to install it for you, but we couldn't detect your operating system.")
        os.system("lua")
    else:
        print("Unknown language.")
    
    main()
def run():
    if exists("package.json") == True: 
        with open('package.json', 'r') as f:
          script = (json.load(f))["script"]
        data = {
            "requests": ["void"],
            "data": ["void"],    
            "return": ["void"]
        }
        with open("Runlogs.json", "w") as file:
            json.dump(data, file)

        threadrunning = True
    
        def onChange(data):
                # convert data to a table
            if data:
                data = json_parser.parse(data)
                if len(data["requests"]) == 0:
                    return
                # get last value of requests
                last = data["requests"][len(data["requests"])-1]

                if last == "void":
                    return
                execute(last)
            
        def routine():
            last = ""
            while threadrunning == True:
                with open("Runlogs.json", "r") as file:
                   data = (file.read())
                if data == last:
                    pass
                else:
                    thread = threading.Thread(target=onChange, args=(data,))
                    thread.start()
                last = data

        thread = threading.Thread(target=routine)
        thread.start()
        if exists(script) == True:
            execute(script)
        else:
            print("Script not found. Try running "+blue("clay new", ['bold'])+" again to reconfigure.")

        
        os.remove("Runlogs.json")
        threadrunning = False
    else:
        print("No project found, try running "+blue("clay new", ['bold'])+" first.")
    main()
def compile():
    # TODO: Setup compiler
    pass

def install():
    if exists("package.json") == True:
        technique = input("How would you like to install the package? (npm, git, cargo, gem, pip, go, luaRocks, url): ")
        if technique == "npm":
            if utilExists("npm") == False:
                if sys.platform == "win32":
                    if utilExists("choco") == True:
                        print("npm is not installed, installing it for you... (this may take a while)")
                        os.system("choco install npm")
                    else:
                        print("npm is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "darwin":
                    if utilExists("brew") == True:
                        print("npm is not installed, installing it for you... (this may take a while)")
                        os.system("brew install npm")
                    else:
                        print("npm is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "linux":
                    if utilExists("apt") == True:
                        print("npm is not installed, installing it for you... (this may take a while)")
                        os.system("apt install npm")
                    else:
                        print("npm is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                

            
            name = input("Package name: ")
            add(name, "npm")
            print("Installing "+name+"...")
            os.system("npm install "+name+" --prefix dependencies")

            os.remove("dependencies/package.json")
            os.remove("dependencies/package-lock.json")

            # rather than keeping the items in node_modules, we will keep the items in dependencies and delete the node_modules folder
            # move the items in node_modules to dependencies
            os.system("mv dependencies/node_modules/* dependencies")

            # delete node_modules
            shutil.rmtree("dependencies/node_modules")

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("npm:"+name)))
        elif technique == "git":
            if utilExists("git") == False:
                if sys.platform == "win32":
                    if utilExists("choco") == True:
                        print("git is not installed, installing it for you... (this may take a while)")
                        os.system("choco install git")
                    else:
                        print("git is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "darwin":
                    if utilExists("brew") == True:
                        print("git is not installed, installing it for you... (this may take a while)")
                        os.system("brew install git")
                    else:
                        print("git is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "linux":
                    if utilExists("apt") == True:
                        print("git is not installed, installing it for you... (this may take a while)")
                        os.system("apt install git")
                    else:
                        print("git is not installed, and clay cannot install it for you. Please install it manually.")
                        return

            url = input("Git URL: ")
            add(url, "git")
            print("Installing "+url+"...")
            os.system("git clone "+url+" dependencies/"+url.split("/")[-1])

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("git:"+url)))
        elif technique == "url":
            url = input("URL: ")
            add(url, "url")
            print("Installing "+url+"...")
            os.system("curl "+url+" > dependencies/"+url.split("/")[-1])

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("url:"+url)))
        elif technique == "luaRocks" :
            if utilExists("luarocks") == False:
                if sys.platform == "win32":
                    if utilExists("choco") == True:
                        print("luarocks is not installed, installing it for you... (this may take a while)")
                        os.system("choco install luarocks")
                    else:
                        print("luarocks is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "darwin":
                    if utilExists("brew") == True:
                        print("luarocks is not installed, installing it for you... (this may take a while)")
                        os.system("brew install luarocks")
                    else:
                        print("luarocks is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "linux":
                    if utilExists("apt") == True:
                        print("luarocks is not installed, installing it for you... (this may take a while)")
                        os.system("apt install luarocks")
                    else:
                        print("luarocks is not installed, and clay cannot install it for you. Please install it manually.")
                        return

            name = input("Package name: ")
            add(name, "luaRocks")
            print("Installing "+name+"...")
            os.system("luarocks install "+name+" --tree=dependencies/"+name)

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("luaRocks:"+name)))
        elif technique == "pip":
            if utilExists("pip") == False:
                if sys.platform == "win32":
                    if utilExists("choco") == True:

                        print("pip is not installed, installing it for you... (this may take a while)")
                        os.system("choco install pip")
                    else:
                        print("pip is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "darwin":
                    if utilExists("brew") == True:

                        print("pip is not installed, installing it for you... (this may take a while)")
                        os.system("brew install pip")
                    else:
                        print("pip is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "linux":
                    if utilExists("apt") == True:
                        print("pip is not installed, installing it for you... (this may take a while)")
                        os.system("apt install pip")
                    else:
                        print("pip is not installed, and clay cannot install it for you. Please install it manually.")
                        return
        
            name = input("Package name: ")
            add(name, "pip")
            print("Installing "+name+"...")
            os.system("pip install "+name+" --target dependencies/"+name)

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("pip:"+name)))
        elif technique == "gem":
            if utilExists("gem") == False:
                if sys.platform == "win32":
                    if utilExists("choco") == True:
                        print("gem is not installed, installing it for you... (this may take a while)")
                        os.system("choco install gem")
                    else:
                        print("gem is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "darwin":
                    if utilExists("brew") == True:
                        print("gem is not installed, installing it for you... (this may take a while)")
                        os.system("brew install gem")
                    else:
                        print("gem is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "linux":
                    if utilExists("apt") == True:
                        print("gem is not installed, installing it for you... (this may take a while)")
                        os.system("apt install gem")
                    else:
                        print("gem is not installed, and clay cannot install it for you. Please install it manually.")
                        return

            name = input("Package name: ")
            add(name, "gem")
            print("Installing "+name+"...")
            os.system("gem install "+name+" --install-dir dependencies/"+name)

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("gem:"+name)))
        elif technique == "cargo":
            if utilExists("cargo") == False:
                if sys.platform == "win32":
                    if utilExists("choco") == True:
                        print("cargo is not installed, installing it for you... (this may take a while)")
                        os.system("choco install cargo")
                    else:
                        print("cargo is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "darwin":
                    if utilExists("brew") == True:
                        print("cargo is not installed, installing it for you... (this may take a while)")
                        os.system("brew install rust")
                    else:
                        print("cargo is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "linux":
                    if utilExists("apt") == True:
                        print("cargo is not installed, installing it for you... (this may take a while)")
                        os.system("apt install cargo")
                    else:
                        print("cargo is not installed, and clay cannot install it for you. Please install it manually.")
                        return
            name = input("Package name: ")
            add(name, "cargo")
            print("Installing "+name+"...")
            os.system("cargo install "+name+" --root dependencies/"+name)

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("cargo:"+name)))
        elif technique == "go":
            if utilExists("go") == False:
                if sys.platform == "win32":
                    if utilExists("choco") == True:
                        print("go is not installed, installing it for you... (this may take a while)")
                        os.system("choco install go")
                    else:
                        print("go is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "darwin":
                    if utilExists("brew") == True:
                        print("go is not installed, installing it for you... (this may take a while)")
                        os.system("brew install go")
                    else:
                        print("go is not installed, and clay cannot install it for you. Please install it manually.")
                        return
                elif sys.platform == "linux":
                    if utilExists("apt") == True:
                        print("go is not installed, installing it for you... (this may take a while)")
                        os.system("apt install go")
                    else:
                        print("go is not installed, and clay cannot install it for you. Please install it manually.")
                        return
            name = input("Package name: ")
            add(name, "go")
            print("Installing "+name+"...")
            os.system("go get "+name+" dependencies/"+name)

            #with open('package.json', 'w') as f:
            #    x = open("package.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("go:"+name)))
        else:
            print("Invalid technique.")

    else:
        print("No project found, try running "+blue("clay new", ['bold'])+" first.")
    main()
def uninstall():
    name = input("Package name: ")
    #remove(name) TODO: add this
    # check if dependencies folder exists
    if os.path.exists("dependencies"):
        # check if package exists
        if os.path.exists("dependencies/"+name):
            # remove package
            shutil.rmtree("dependencies/"+name)
            print("Package "+name+" uninstalled.")
        else:
            print("Package "+name+" not found.")
    main()
def list():
    # check if dependencies folder exists

    if os.path.exists("dependencies"):
        # list dependencies folder
        print("Listing dependencies...")
        print(os.listdir("dependencies"))
    else:
        print("Dependencies folder does not exist, have you tried running "+blue("clay new", ['bold'])+" yet?")

    main()
def version():
    print("Version 0.0.1")
    main()
def clear():
    # check if dependencies folder exists

    if os.path.exists("dependencies"):
        # clear dependencies folder
        shutil.rmtree("dependencies")

        # create dependencies folder
        os.mkdir("dependencies")

        print("Dependencies folder cleared.")
    else:
        print("Dependencies folder does not exist, have you tried running "+blue("clay new", ['bold'])+" yet?")

    main()

def pref():
    pass


# Main function
def main():
    command = input("clay> ")
    if command == "new":
        new()
    if command == "add":
        add()
    if command == "remove":
        remove()
    elif command == "run":
        run()
    elif command == "install":
        install()
    elif command == "uninstall":
        uninstall()
    elif command == "list":
        list()
    elif command == "help":
        help()
    elif command == "--version":
        version()
    elif command == "exit":
        sys.exit("Exiting Clay terminal...")
    elif command == "clear":
        clear()
    elif command == "shell":
        shell()
    elif command == "pref":
        pref()
    elif command == "ignore":
        void()

    else:
        print("Invalid command, try "+blue("clay help", ['bold']))
        main()

if __name__ == "__main__":
    print("Use "+blue("clay help", ['bold'])+" to get started, or "+blue("clay exit", ['bold'])+" to exit the clay terminal.")
    main()