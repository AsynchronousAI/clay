# author: @AsynchronousAI
# version: 0.0.1
# license: MIT



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
from time import sleep
import platform
# variables
commands = []
runInstall = True
path = os.getcwd()
# run functions
def execute(script):
    print(magenta("Compiling "+script+"...\n\n"))

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
        runJS(script)
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
        return
def utilExists(name):
    return find_executable(name) is not None
def runCommand(command, isRun = False):
    #print("Running command: "+command)
    status = os.system(command)
    if isRun:
        if status != 0:
            print(red("\n\nFailed to run script. Error code: "+str(status)+"\n\n", ["bold"]))

    return status
# build
def buildAll():
    buildPython()
    buildLua()
    #buildRuby()
    #buildSwift()
    buildJS()
    #buildC()
    #buildCpp()
    #buildCS()
    #buildJava()
    #buildGo()
    buildRust()
    #buildKotlin()
    #buildPHP()
    #buildDart()
    pass
def buildSelf():
    # compile clay.py 
    pass

def buildJS():
    if utilExists("bun") == False:
        print("Bun.js (clay edition) is not installed. Installing...")
        # build ./clayJS
def buildLua():
    if utilExists("luajit") == False:
        print("Lua (clay edition) is not installed. Installing...")
        # build ./clayLua
        if utilExists("make") == False:
            print("Make is required to install Lua (clay edition).")
        else:
            # cd ./clayLua
            os.chdir("./clayLua")
            if sys.platform == "darwin":
                osx = (platform.uname().release).rsplit('.', 1)[0]
                status = runCommand("MACOSX_DEPLOYMENT_TARGET="+osx+" make && sudo make install")   
            else:
                status = runCommand("make && sudo make install")
            
            if status == 0:      
                status = runCommand("sudo make install")
                if status == 0:
                    status = runCommand("ln -sf luajit-2.1.0-beta3 /usr/local/bin/luajit")
                    if status == 0:
                        print(magenta("\nSuccessfully installed Lua (clay edition)!\n\n\n"))
                        return True
        print(red("\n\nFailed to install Lua (clay edition).\n Exit status: "+str(status)+"\n\n", ["bold"]))
        print(yellow("help: this may be because your platform is not supported. get more help at https://AsynchronousAI.github.io/clay/forum\n\n"))
        os.chdir(path)
        return False
def buildPython():
    os.chdir("./clayPython")
    if utilExists("python3") == False:
        print("The python interpreter is required to install Python (clay edition).")
        return
    else:
        if utilExists("pypy") == False:
            os.system("python -mpip install cffi")
            
def buildRust():
    # At this time rust does not have a clay edition, so we will just install rust
    if utilExists("rustc") == False:
        if sys.platform == "darwin":
            print("Rust is not installed. Installing...")
            if utilExists("brew") == False:
                print("Brew is not installed. Installing...")
                status = runCommand("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)\"")
                if status != 0:
                    print(red("\n\nFailed to install brew. Error code: "+str(status)+"\n\n", ["bold"]))
                    return False
            status = runCommand("brew install rust")
            if status != 0:
                print(red("\n\nFailed to install rust. Error code: "+str(status)+"\n\n", ["bold"]))
                return False
        if sys.platform == "linux":
            print("Rust is not installed. Installing...")
            if utilExists("apt") == False:
                print(red("\n\nFailed to install rust. apt is not installed", ["bold"]))
                return False
            runCommand("sudo apt install rustc")

        if sys.platform == "win32":
            print("Rust is not installed. Installing...")
            if utilExists("choco") == False:
                print("Chocolatey is not installed. Installing...")
                status = runCommand("powershell.exe -Command \"iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))\"")
                if status != 0:
                    print(red("\n\nFailed to install chocolatey. Error code: "+str(status)+"\n\n", ["bold"]))
                    return False
            runCommand("choco install rust")
        return True
    '''
    if utilExists("rustc") == False:
        print("Rust is not installed. Installing...")
        
        # build ./clayRust
        if utilExists("make") == False:
            print("Make is required to install Rust.")
        else:
            # cd ./clayRust
            os.chdir("./clayRust")
            os.system("./configure")
            runCommand("make")          

            # find a directory in clayRust/build/ that has a file that starts with stage
            for root, dirs, files in os.walk("./build"):
                for file in files:
                    if file.startswith("stage") and os.path.exists("./build/"+file+"/bin"):
                        # move items from clayRust/build/stage1/bin to /usr/local/bin
                        # make sure file has a bin folder
                        if sys.platform == "win32":
                            # move files to windows equivelent of bin
                            os.chdir("./build/"+file+"/bin")
                            shutil.move("rustc.exe", "C:/Windows/System32")
                            shutil.move("rustdoc.exe", "C:/Windows/System32")
                            shutil.move("rust-gdb.exe", "C:/Windows/System32")
                            shutil.move("rust-lldb.exe", "C:/Windows/System32")
                            shutil.move("rustup.exe", "C:/Windows/System32")
                            return
                        os.chdir("./build/"+file+"/bin")
                        shutil.move("rustc", "/usr/local/bin")
                        shutil.move("rustdoc", "/usr/local/bin")
                        shutil.move("rust-gdb", "/usr/local/bin")
                        shutil.move("rust-lldb", "/usr/local/bin")
                        shutil.move("rustup", "/usr/local/bin")

                        print(magenta("\nSuccessfully installed Rust (clay edition).\n\n\n"))
                        return

            print(red("\nFailed to install Rust (clay edition).\n\n\n"))
            '''
# languages
def runPython(scriptPath):
    x = buildPython()
    if x == False:
        return

    os.chdir(path)
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "from clayForPython import *\n"+script

    # use the exec function to run the script, ex: exec(open('file.py').read())
    script = "from clayForPython import *\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("python "+scriptPath, True)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runLua(scriptPath):
    x = buildLua()
    if x == False:
        return
    os.chdir(path)
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForLua')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("luajit "+scriptPath+" -b "+scriptPath.replace(".lua", ".o"), True)
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
    runCommand("ruby "+scriptPath, True)
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
    runCommand("swift "+scriptPath, True)
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
    runCommand("gcc "+scriptPath, True)
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
    runCommand("kotlinc "+scriptPath, True)
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
    runCommand("javac "+scriptPath, True)
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
    runCommand("g++ "+scriptPath, True)
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
    runCommand("csc "+scriptPath, True)
    runCommand("mono "+scriptPath.replace(".cs", ""), True)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runRust(scriptPath):
    x = buildRust()
    if x == False:
        return
    os.chdir(path)
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "mod clayForRust as clay\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    # if a file is found ith the name scriptPath.replace(".rs", "")
    runCommand("rustc "+scriptPath, True) 
    # run "./" combined with the file name if on mac or linux but on windows run the "./" combined with the file nme but .rs is replaced with .exe
    if sys.platform == "win32":
        runCommand("./"+scriptPath.replace(".rs", ".exe"), True)
    else:
        runCommand("./"+scriptPath.replace(".rs", ""), True)
    os.chdir(path)
    with open(scriptPath, 'w') as f:
        f.write(orig)
def runJS(scriptPath):
    x = buildJS()
    if x == False:
        return
    with open(scriptPath, 'r') as f:
          script = f.read()
    orig = script
    script = "require('clayForJS')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("bun run "+scriptPath, True)
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
    runCommand("dart "+scriptPath, True)
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
    runCommand("go run "+scriptPath, True)
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
    runCommand("php "+scriptPath, True)
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
        buildPython()
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
       buildLua()
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

        global threadrunning 
        threadrunning = True
        global threadsrunning 
        threadsrunning = 0

        # check if any files have the same name as eachother, if so then output an error
        files = os.listdir()
        for file in files:
            if file:
                if files.count(file) > 1:
                    print(red("\nError: Multiple files with the same name.\n"))
                    return
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
            threadsrunning = 0
            while threadrunning == True:
                # check if Runlogs.json exists
                if exists("Runlogs.json") == False:
                    # wait until it exists
                    while exists("Runlogs.json") == False:
                        pass

                os.chdir(path)
                with open("Runlogs.json", "r") as file:
                   data = (file.read())
                if data == last:
                    pass
                else:
                    threadsrunning += 1
                    thread = threading.Thread(target=onChange, args=(data,))
                    thread.start()
                    # wait for thread to finish
                    thread.join()
                    threadsrunning -= 1
                last = data

        thread = threading.Thread(target=routine)
        thread.start()
        if exists(script) == True:
            execute(script)
        else:
            print("Script not found. Try running "+blue("clay new", ['bold'])+" again to reconfigure.")

        if threadsrunning > 0:
            while threadsrunning > 0:
                pass
        threadrunning = False
        threadsrunning = 0
        sleep(0.5)
        os.remove("Runlogs.json")
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
            if utilExists("clayJS") == False:
                print("ClayJS is not installed. Installing...")
                buildJS()

            name = input("Package name: ")
            add(name, "npm")
            print("Installing "+name+"...")
            os.system("clayJS install "+name+" --prefix dependencies")

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
    ### CATEGORIES
    def langConfig():
        pass
    def compilers():
        print("Select a compiler:")
        print("1. JS")
        print("2. Go")
        print("3. Zig")
        print("4. Moonscript")
        print("5. Lua")
        print("6. Go")
        print("7. Brainf*ck")
        print("8. Go")
        print("9. Swift")
        print("10. Rust")
        print("11. Dart")
        print(red("\n12. Exit"))
        option = input("")
        if int(option) <= 11:
            langConfig(option)
        elif option == "12":
            main()
        else:
            print(red("Invalid response.", ["bold"]))
            compilers()
    ### ASK FOR INPUT
    print("Select a category:\n\n")
    print("1. Compilers")
    print("2. Packages")
    print("3. Account")
    print( red ("\n4. Exit"))
    option = input("")
    if option == "1":
        compilers()
    elif option == "2":
        pass
    elif option == "3":
        print("You currently arent logged in. Would you like to login (y/n)")
        u = input("Username: ")
        p = input("Password:")
    elif option == "4":
        main()
    else:
        print(red("Invalid response.", ["bold"]))
        pref()

def todo():
    print("Add package support, Add python (recieve) support, add built in builder.")

def massBuild():
    print("The following command will install all of clays's dependencies, even the ones that are not needed for the current project. This may take multiple hours. \n\n Are you sure you want to continue? (y/n)")
    answer = input("")
    if answer == "y":
        print("\nThis may take a while...\n")
        buildAll()
    elif answer == "n":
        print("Aborting...")
    else:
        print("Invalid answer, aborting...")
    main()
# Main function
terminall = False
def main():
    # check for apt if they are on linux, check for choco if they are on windows, check for brew if they are on darwin
    if sys.platform == "win32":
        if utilExists("choco") == False:
            print("Chocolatey is not installed, and it is a requirement. Please install it manually.")
            return
    elif sys.platform == "darwin":
        if utilExists("brew") == False:
            print("Homebrew is not installed, and it is a requirement. Please install it manually.")
            return
    elif sys.platform == "linux":
        if utilExists("apt") == False:
            print("apt is not installed, and it is a requirement. Please install it manually.")
            return
    if terminall == True:
        terminal()
def terminal():
    terminall = True
    command = input("clay> ")
    if command == "new":
        new()
    if command == "add":
        add()
    if command == "remove":
        remove()
    if command == "build":
        massBuild()
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
    terminall = True
    terminal()
