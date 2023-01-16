# author: @AsynchronousAI00
# version: 0.0.1
# license: MIT

# libraries
import os
import json
from os.path import exists
import sys
from distutils.spawn import find_executable
import threading
import json
import shutil
from multiprocessing import Process
from subprocess import call
from time import sleep
import platform
# variables
commands = []
runInstall = True
path = os.getcwd()
# colors
def black(text, styles = []):
    return color(text, 30, styles)
def red(text, styles = []):
    return color(text, 31, styles)
def green(text, styles = []):
    return color(text, 32, styles)
def yellow(text, styles = []):
    return color(text, 33, styles)
def blue(text, styles = []):
    return color(text, 34, styles)
def magenta(text, styles = []):
    return color(text, 35, styles)
def cyan(text, styles = []):
    return color(text, 36, styles)
def white(text, styles = []):
    return color(text, 37, styles)
def color(text, color, styles = []):
    style = ""
    for s in styles:
        if s == "bold":
            style += "1;"
        elif s == "underline":
            style += "4;"
        elif s == "reverse":
            style += "7;"
        elif s == "concealed":
            style += "8;"
    return "\033["+style+str(color)+"m"+text+"\033[0m"
# run functions
def save(key, value):
    # save the value to the key and make it pernamant
    
    # check if the key exists
    if exists("data.json") == False:
        # create the file
        open("data.json", "w+").write("{}")
    # load the file
    data = json.loads(open("data.json", "r").read())
    # add the key and value
    data[key] = value
    # save the file
    open("data.json", "w+").write(json.dumps(data))
def load(key):
    # load the value from the key
    # check if the key exists
    if exists("data.json") == False:
        # create the file
        open("data.json", "w+").write("{}")
    # load the file
    data = json.loads(open("data.json", "r").read())
    # return the value
    return data[key]
def mutate(files):
    # take in files which is a list of paths to executable files
    # compile all files into one file

    # create a new file
    pass
def execute(script):
    def makeInstall(util, win, darwin, linux):
        def val():
            if utilExists(util) == False:
                # Check operating system
                if sys.platform == "win32":
                    # Check if they have choclatey installed
                    if utilExists("choco") == True:
                        runCommand("choco install "+win)
                    else:
                        print("choco missing")
                elif sys.platform == "linux":
                    # Check if they have apt installed
                    if utilExists("apt") == True:
                        runCommand("sudo apt install "+linux)
                    else:
                        print("apt missing")
                elif sys.platform == "darwin":
                    # Check if they have brew installed
                    if utilExists("brew") == True:
                        runCommand("brew install "+darwin)
                    else:
                        print("brew missing")
                else:
                    print("We couldn't detect your operating system.")
        return val
    if sys.platform == "win32":
        fileRun = "start @xfile.exe && del @xfile.exe"
    else:
        fileRun = "./@xfile && rm @xfile"
    languages = {
        1: {
            "name": "python",
            "extension": ".py",
            "command": "python @file @args",
            "install": makeInstall("python", "python", "python", "python"),
            "lib": "import lib/clayBindings/clay as clay"
        },
        2: {
            "name": "php",
            "extension": ".php",
            "command": "php @file @args",
            "install": makeInstall("php", "php", "php", "php"),
            "lib": "require_once 'lib/clayBindings/clay.php';"
        },
        3: {
            "name": "javascript",
            "extension": ".js",
            "command": "node @file @args",
            "install": makeInstall("node", "nodejs", "node", "nodejs"),
            "lib": "require('lib/clayBindings/clay.js');"
        },
        4: {
            "name": "java",
            "extension": ".java",
            "command": "java @file @args",
            "install": makeInstall("java", "java", "java", "java"),
            "lib": "import lib/clayBindings/clay;"
        },
        5: {
            "name": "c",
            "extension": ".c",
            "command": "gcc @file -o @file.out && @file.out @args",
            "install": makeInstall("gcc", "gcc", "gcc", "gcc"),
            "lib": "#include <lib/clayBindings/clay.h>"
        },
        6: {
            "name": "c++",
            "extension": ".cpp",
            "command": "g++ @file -o @file.out && @file.out @args",
            "install": makeInstall("g++", "g++", "g++", "g++"),
            "lib": "#include <lib/clayBindings/clay.h>"
        },
        7: {
            "name": "c#",
            "extension": ".cs",
            "command": "csc @file && "+fileRun,
            "install": makeInstall("csc", "csc", "csc", "csc"),
            "lib": "using lib/clayBindings/clay;"
        },
        7: {
            "name": "go",
            "extension": ".go",
            "command": "go run @file @args",
            "install": makeInstall("go", "go", "go", "go"),
            "lib": "import lib/clayBindings/clay"

        },
        8: {
            "name": "ruby",
            "extension": ".rb",
            "command": "ruby @file @args",
            "install": makeInstall("ruby", "ruby", "ruby", "ruby"),
            "lib": "require 'lib/clayBindings/clay'"

        },
        9: {
            "name": "swift",
            "extension": ".swift",
            "command": "swift @file @args",
            "install": makeInstall("swift", "swift", "swift", "swift"),
            "lib": "import lib/clayBindings/clay"
        },
        10: {
            "name": "kotlin",
            "extension": ".kt",
            "command": "kotlinc @file -include-runtime -d @file.jar && java -jar @file.jar @args",
            "install": makeInstall("kotlinc", "kotlin", "kotlin", "kotlin"),
            "lib": "import lib/clayBindings/clay"
        },
        11: {
            "name": "rust",
            "extension": ".rs",
            "command": "rustc @file && "+fileRun,
            "install": makeInstall("rustc", "rust", "rust", "rust"),
            "lib": "extern crate lib/clayBindings/clay;"
        },
        12: {
            "name": "lua",
            "extension": ".lua",
            "command": "lua @file @args",
            "install": makeInstall("lua", "lua", "lua", "lua"),
            "lib": "clay = require 'lib/clayBindings/clay'"
        },
        13: {
            "name": "perl",
            "extension": ".pl",
            "command": "perl @file @args",
            "install": makeInstall("perl", "perl", "perl", "perl"),
            "lib": "require 'lib/clayBindings/clay'"
        },
        14: {
            "name": "bash",
            "extension": ".sh",
            "command": "bash @file @args",
            "install": makeInstall("bash", "bash", "bash", "bash"),
            "lib": "source lib/clayBindings/clay"
        },
        15: {
            "name": "powershell",
            "extension": ".ps1",
            "command": "powershell @file @args",
            "install": makeInstall("powershell", "powershell", "powershell", "powershell"),
            "lib": "Import-Module lib/clayBindings/clay"
        },  
        16: {
            "name": "haskell",
            "extension": ".hs",
            "command": "runhaskell @file @args",
            "install": makeInstall("runhaskell", "haskell", "haskell", "haskell"),
            "lib": "import lib/clayBindings/clay"
        },
        17: {
            "name": "elixir",
            "extension": ".ex",
            "command": "elixir @file @args",
            "install": makeInstall("elixir", "elixir", "elixir", "elixir"),
            "lib": "import lib/clayBindings/clay"
        },
        18: {
            "name": "r",
            "extension": ".r",
            "command": "Rscript @file @args",
            "install": makeInstall("Rscript", "r-base", "r-base", "r-base"),
            "lib": "source('lib/clayBindings/clay')"
        },
        19: {
            "name": "d",
            "extension": ".d",
            "command": "dmd @file && "+fileRun,
            "install": makeInstall("dmd", "dmd", "dmd", "dmd"),
            "lib": "import lib/clayBindings/clay"
        },
        20: {
            "name": "dart",
            "extension": ".dart",
            "command": "dart @file @args",
            "install": makeInstall("dart", "dart", "dart", "dart"),
            "lib": "import 'lib/clayBindings/clay'"
        },
        

    }

    # check if the script is a file
    if os.path.isfile(script) == False:
        print(red("Script not found."))
        return
    # check if the script is a valid extension
    extension = os.path.splitext(script)[1]
    language = None
    for lang in languages:
        if languages[lang]["extension"] == extension:
            language = languages[lang]
            break
    if language == None:
        print(red("Invalid script extension."))
        return
    # check if the language is installed
    if not utilExists(language["name"]):
        language["install"]()
    # run the script
    
    # duplicate lib to the script directory
    if os.path.exists("lib") == False:
        print(red("Clay is damaged. Please reinstall."))
        return
    else:
        shutil.copytree("lib", os.path.dirname(script)+"/lib")

    # make the script start with the lib
    with open(script, "r") as f:
        scriptCode = f.read()
    with open(script, "w") as f:
        f.write(language["lib"]+"\n"+scriptCode)

    runCommand(language["command"].replace("@file", script).replace("@xfile", script.split(".")[0]).replace("@args", " ".join(sys.argv[2:])), True)
    with open(script, "w") as f:
        f.write(scriptCode)
    shutil.rmtree(os.path.dirname(script)+"/lib")
def utilExists(name):
    return find_executable(name) is not None
def runCommand(command, isRun = False):
    #print("Running command: "+command)
    status = os.system(command)
    if isRun:
        if status != 0:
            print(red("\n\nFailed to run script. Error code: "+str(status)+"\n\n", ["bold"]))

    return status
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
    if script.startswith("require('clayForPHP')") == False:
        script = "require('clayForPHP')\n"+script
    with open(scriptPath, 'w') as f:
        f.write(script)
    runCommand("php "+scriptPath, True)
    with open(scriptPath, 'w') as f:
        f.write(orig)    

# commands
def help():
    print(blue("clay", ['bold'])+": the only runtime you need, supports hundreds of languages while maintaining dazzling speeds.\n\nCommands:\n "+blue("clay new", ['bold'])+" \t\t\t\t create a new project \n "+yellow("clay run", ['bold'])+" \t\t\t\t run a command in the project \n "+green("clay install", ['bold'])+" \t\t\t\t install a package in the project \n "+green("clay uninstall", ['bold'])+" \t\t\t uninstall a package in the project \n "+green("clay list", ['bold'])+" \t\t\t\t list all packages in the project  \n "+green("clay clear", ['bold'])+" \t\t\t\t clear all packages in the project \n "+green("clay add", ['bold'])+" \t\t\t\t add a package in the project.json file \n "+green("clay remove", ['bold'])+" \t\t\t\t remove a package in the project.json file \n "+ magenta("clay help", ['bold'])+" \t\t\t\t show this message \n "+magenta("clay pref", ['bold'])+" \t\t\t\t configurate a package or clay \n\n Options: \n "+black("--version", ['dim'])+" \t\t\t\t show the version number")
    main()
def void():
    runInstall = False
    print("Blocked")
    main()
def add(nm="void", p="void"):
    called = nm == "void" and p == "void"
    # check if project.json exists
    if not exists("project.json"):
        print("No project.json file found. Run "+blue("clay new", ['bold'])+" to create a new project.")
        main()
    else:
        # read project.json
        if nm == "void":
            nm = input("Package name: ")
        if p == "void":
            p = input("Package provider: ")
        
        with open('project.json', 'r') as f:
            dataTable = json.loads(f.read())
        
        # append nm into dataTable.dependencies (dict)
        # dataTable['dependencies'][""]({"name": nm, "provider": p})
        # ADD LATER
    if called:
        main()
def remove(nm):
    # check if project.json exists
    if not exists("project.json"):
        print("No project.json file found. Run "+blue("clay new", ['bold'])+" to create a new project.")
        main()
    else:
        # read project.json
        with open('project.json', 'r') as f:
            dataTable = json.loads(f.read())
        # find a item in dataTable.dependencies with name nm
        for i in dataTable['dependencies']:
            if i.name == nm:
                dataTable['dependencies'].remove(i)
        
        
        # write project.json
        with open('project.json', 'w') as f:
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
        "dependencies": {},
        "scripts": {},
        "files": {},
    }
    if not exists("dependencies"):
        os.mkdir("dependencies")

    if not exists(script):
        with open(script, 'w') as f:
            f.write("")

    with open('project.json', 'w') as f:
        f.write(json.dumps(dataTable))

    main()
def publish():
    print(magenta("Publising project to clay registry...", ['bold']))
 
    # check if project.json exists
    if not exists("project.json"):
        print("No project.json file found. Run "+blue("clay new", ['bold'])+" to create a new project.")
        main()
    else:
        # read project.json
        with open('project.json', 'r') as f:
            dataTable = json.loads(f.read())
        # check if name is set
        if dataTable['name'] == "":
            print("You need to set a name in project.json")
            main()
        else:
            # check if version is set
            if dataTable['version'] == "":
                print("You need to set a version in project.json")
                main()
            else:
                # check if author is set
                if dataTable['author'] == "":
                    print("You need to set an author in project.json")
                    main()
                else:
                    # check if description is set
                    if dataTable['description'] == "":
                        print("You need to set a description in project.json")
                        main()
                    else:
                        # check if script is set
                        if dataTable['script'] == "":
                            print("You need to set a script in project.json")
                            main()
                        else:
                            # check if dependencies is set
                            if dataTable['dependencies'] == {}:
                                print("You need to set dependencies in project.json")
                                main()
                            else:
                                # check if scripts is set
                                if dataTable['scripts'] == {}:
                                    print("You need to set scripts in project.json")
                                    main()
                                else:
                                    # check if files is set
                                    if dataTable['files'] == {}:
                                        print("You need to set files in project.json")
                                        main()
                                    else:
                                        # check if dependencies are installed
                                        if not exists("dependencies"):
                                            print("You need to install dependencies before publishing.")
                                            main()
                                        else:
                                            # check if script exists
                                            if not exists(dataTable['script']):
                                                print("You need to set a script in project.json")
                                                main()
                                            else:
                                                # check if files exists
                                                if not exists("files"):
                                                    print("You need to set files in project.json")
                                                    main()
                                                else:
                                                    # check if all files exists
                                                    for i in dataTable['files']:
                                                        if not exists(i):
                                                            print("You need to set files in project.json")
                                                            main()

    # delete dependencies folder
    if exists("dependencies"):
        shutil.rmtree("dependencies")     

    if not exists("publish.txt"):
        with open('publish.txt', 'w') as f:
            f.write("")
    
    # upload to github
    if not utilExists("gh"):
        print("You need to install gh to publish your project.")
        main()
    else:   
        os.system("gh repo create")
        os.system("gh repo clone "+dataTable['name'])
        os.system("gh repo fork "+dataTable['name'])
        os.system("gh repo view "+dataTable['name'])
        os.system("gh repo view "+dataTable['name']+" --web")
        os.system("gh repo view "+dataTable['name']+" --clone")
        os.system("gh repo view "+dataTable['name']+" --ssh")
        os.system("gh repo view "+dataTable['name']+" --http")
        os.system("gh repo view "+dataTable['name']+" --git")
        os.system("gh repo view "+dataTable['name']+" --releases")
        os.system("gh repo view "+dataTable['name']+" --issues")
        os.system("gh repo view "+dataTable['name']+" --pr")
        os.system("gh repo view "+dataTable['name']+" --wiki")
        os.system("gh repo view "+dataTable['name']+" --size")
        os.system("gh repo view "+dataTable['name']+" --stars")
        os.system("gh repo view "+dataTable['name']+" --forks")
        os.system("gh repo view "+dataTable['name']+" --topics")
        os.system("gh repo view "+dataTable['name']+" --license")
        os.system("gh repo view "+dataTable['name']+" --default-branch")
        os.system("gh repo view "+dataTable['name']+" --visibility")
        os.system("gh repo view "+dataTable['name']+" --template")
        os.system("gh repo view "+dataTable['name']+" --archived")
        os.system("gh repo view "+dataTable['name']+" --empty")
        os.system("gh repo view "+dataTable['name']+" --private")
        os.system("gh repo view "+dataTable['name']+" --parent")
        os.system("gh repo view "+dataTable['name']+" --source")
        os.system("gh repo view "+dataTable['name']+" --network")
        os.system("gh repo view "+dataTable['name']+" --mirror")
        os.system("gh repo view "+dataTable['name']+" --homepage")
        os.system("gh repo view "+dataTable['name']+" --description")
        os.system("gh repo view "+dataTable['name']+" --created")
        os.system("gh repo view "+dataTable['name']+" --pushed")                                         
def shell(lang):
    if lang == "":
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
def run(runscript):
    if exists("project.json") == True: 
        with open('project.json', 'r') as f:
          package = (json.load(f))
          script = package["script"]
          scripts = package["scripts"]
        if runscript != "" and runscript != None and runscript != " ":
            if runscript in scripts:
                command = scripts[runscript]
            else:
                print(red("Script "+runscript+" not found.", ['bold']))
                main()
            
            # if the command doesnt start with %, then run it with os.system
            if command[0] != "%":
                os.system(command)
                return
            else:
                # check if the file after the % exists
                if os.path.exists(command[1:]):
                    # if it does, run it
                    execute(command[1:])
                    return
                else:
                    print(red("File "+command[1:]+" not found.", ['bold']))
                    main()

        # if dist folder exists clear it
        if os.path.exists("dist"):
            shutil.rmtree("dist")

        global threadrunning 
        threadrunning = True
        global threadsrunning 
        threadsrunning = 0

        # execute() main script
        print(magenta("Running "+script+"...", ['bold']))
        execute(script)
    else:
        print("No project found, try running "+blue("clay new", ['bold'])+" first.")
    main()
def compile():
    # TODO: Setup compiler
    pass
def install(name, technique):
    # if dependencies folder doesnt exist, create it
    if not os.path.exists("dependencies"):
        os.mkdir("dependencies")
    if exists("project.json") == True:
        # check if package exists
        if os.path.exists("dependencies/"+name):
            print("Package "+name+" already exists.")
        else:
            # download package
            techniques = {
                # %name is the package name, save it to dependencies/, for npm also move all of the items from node_modules to dependencies and delete node_modules
                "npm": "npm install %name --prefix dependencies && mv dependencies/node_modules/* dependencies && rm -rf dependencies/node_modules",
                "pip": "pip install %name --target dependencies",
                "git": "git clone %name dependencies/%name",
                "zip": "wget %name -O dependencies/%name.zip && unzip dependencies/%name.zip -d dependencies/%name && rm dependencies/%name.zip",
                "tar": "wget %name -O dependencies/%name.tar && tar -xvf dependencies/%name.tar -C dependencies/%name && rm dependencies/%name.tar",
                "deb": "wget %name -O dependencies/%name.deb && dpkg -x dependencies/%name.deb dependencies/%name && rm dependencies/%name.deb",
                "rpm": "wget %name -O dependencies/%name.rpm && rpm2cpio dependencies/%name.rpm | cpio -idmv && rm dependencies/%name.rpm",
                "apk": "wget %name -O dependencies/%name.apk && apk add --allow-untrusted dependencies/%name.apk && rm dependencies/%name.apk",
                "exe": "wget %name -O dependencies/%name.exe && wine dependencies/%name.exe && rm dependencies/%name.exe",
                "msi": "wget %name -O dependencies/%name.msi && wine dependencies/%name.msi && rm dependencies/%name.msi",
                "dmg": "wget %name -O dependencies/%name.dmg && hdiutil attach dependencies/%name.dmg && rm dependencies/%name.dmg",
                "pkg": "wget %name -O dependencies/%name.pkg && installer -pkg dependencies/%name.pkg -target / && rm dependencies/%name.pkg",
                "jar": "wget %name -O dependencies/%name.jar && java -jar dependencies/%name.jar && rm dependencies/%name.jar",
                "py": "wget %name -O dependencies/%name.py && python dependencies/%name.py && rm dependencies/%name.py",
                "sh": "wget %name -O dependencies/%name.sh && sh dependencies/%name.sh && rm dependencies/%name.sh",
                "bat": "wget %name -O dependencies/%name.bat && cmd /c dependencies/%name.bat && rm dependencies/%name.bat",
                "ps1": "wget %name -O dependencies/%name.ps1 && powershell dependencies/%name.ps1 && rm dependencies/%name.ps1",
                "luarocks": "luarocks install %name --tree dependencies",
                "gem": "gem install %name --install-dir dependencies",
                "cpan": "cpan %name",
                "pear": "pear install %name",
                "composer": "composer require %name --working-dir dependencies",
                "cargo": "cargo install %name --root dependencies",
                "go": "go get %name",
                "rust": "rustup install %name",
                "crystal": "crystal deps install %name",
                "nimble": "nimble install %name",
                "nim": "nim c %name",
                "dub": "dub fetch %name",
                "d": "dub run %name",
                "nim": "nim c %name",
                "nimble": "nimble install %name",
                "wally": "wally install %name",
                "yarn": "yarn add %name --prefix dependencies",
                "apt": "apt install %name",
                "apt-get": "apt-get install %name",
                "choco": "choco install %name",
                "brew": "brew install %name",
                }
            installation = {
                # example: "packageManager": {choco: "command", apt: "command", brew: "command", utilName: "utilName"}, if it doesnt exist in a platform set to "blocked"
                "npm": {"choco": "npm", "apt": "npm", "brew": "npm", "utilName": "npm"},
                "pip": {"choco": "pip", "apt": "pip", "brew": "pip", "utilName": "pip"},
                "git": {"choco": "git", "apt": "git", "brew": "git", "utilName": "git"},
                "zip": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "unzip"},
                "tar": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "tar"},
                "deb": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "dpkg"},
                "rpm": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "rpm2cpio"},
                "apk": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "apk"},
                "exe": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "wine"},
                "msi": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "wine"},
                "dmg": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "hdiutil"},
                "pkg": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "installer"},
                "jar": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "java"},
                "py": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "python"},
                "sh": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "sh"},
                "bat": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "cmd"},
                "ps1": {"choco": "wget", "apt": "wget", "brew": "wget", "utilName": "powershell"},
                "luarocks": {"choco": "luarocks", "apt": "luarocks", "brew": "luarocks", "utilName": "luarocks"},
                "gem": {"choco": "gem", "apt": "gem", "brew": "gem", "utilName": "gem"},
                "cpan": {"choco": "cpan", "apt": "cpan", "brew": "cpan", "utilName": "cpan"},
                "pear": {"choco": "pear", "apt": "pear", "brew": "pear", "utilName": "pear"},
                "composer": {"choco": "composer", "apt": "composer", "brew": "composer", "utilName": "composer"},
                "cargo": {"choco": "cargo", "apt": "cargo", "brew": "cargo", "utilName": "cargo"},
                "go": {"choco": "go", "apt": "go", "brew": "go", "utilName": "go"},
                "rust": {"choco": "rustup", "apt": "rustup", "brew": "rustup", "utilName": "rustup"},
                "crystal": {"choco": "crystal", "apt": "crystal", "brew": "crystal", "utilName": "crystal"},
                "nimble": {"choco": "nimble", "apt": "nimble", "brew": "nimble", "utilName": "nimble"},
                "nim": {"choco": "nim", "apt": "nim", "brew": "nim", "utilName": "nim"},
                "dub": {"choco": "dub", "apt": "dub", "brew": "dub", "utilName": "dub"},
                "d": {"choco": "d", "apt": "d", "brew": "d", "utilName": "d"},
                "nim": {"choco": "nim", "apt": "nim", "brew": "nim", "utilName": "nim"},
                "nimble": {"choco": "nimble", "apt": "nimble", "brew": "nimble", "utilName": "nimble"},
                "wally": {"choco": "wally", "apt": "wally", "brew": "wally", "utilName": "wally"},
                "yarn": {"choco": "yarn", "apt": "yarn", "brew": "yarn", "utilName": "yarn"},
                "pipenv": {"choco": "pipenv", "apt": "pipenv", "brew": "pipenv", "utilName": "pipenv"},
                "poetry": {"choco": "poetry", "apt": "poetry", "brew": "poetry", "utilName": "poetry"},
                "pipx": {"choco": "pipx", "apt": "pipx", "brew": "pipx", "utilName": "pipx"},
                "pipenv": {"choco": "pipenv", "apt": "pipenv", "brew": "pipenv", "utilName": "pipenv"}
            }

            # check if package is in the list
            if technique in installation and technique in techniques:
                # check if package is installed
                if utilExists(installation[technique]["utilName"]):
                    # install package
                    print("Installing "+name+"...")
                    if sys.platform == "win32":
                        if installation[technique]["choco"] == "blocked":
                            print(red("This package cannot be installed on Windows."))
                        os.system("choco install "+installation[technique]["choco"])
                    elif sys.platform == "linux":
                        if installation[technique]["apt"] == "blocked":
                            print(red("This package cannot be installed on Linux."))
                        os.system("sudo apt install "+installation[technique]["apt"])
                    elif sys.platform == "darwin":
                        if installation[technique]["brew"] == "blocked":
                            print(red("This package cannot be installed on macOS."))
                        os.system("brew install "+installation[technique]["brew"])

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
    def langConfig(lang):
        if lang == "1":
            print("JS")
            lang = "js"
        elif lang == "2":
            print("Go")
            lang = "go"
        elif lang == "3":
            print("Zig")
            lang = "zig"
        elif lang == "4":
            print("Moonscript")
            lang = "moonscript"
        elif lang == "5":
            print("Lua")
            lang = "lua"
        elif lang == "6":
            print("Go")
            lang = "go"
        elif lang == "7":
            print("Brainf*ck")
            lang = "brainfuck"
        elif lang == "8":
            print("Go")
            lang = "go"
        elif lang == "9":
            print("Swift")
            lang = "swift"
        elif lang == "10":
            print("Rust")
            lang = "rust"
        elif lang == "11":
            print("Dart")
            lang = "dart"
        elif lang == "12":
            print("Perl")
            lang = "perl"
        elif lang == "13":
            print("Python")
            lang = "python"
        elif lang == "14":
            print("C")
            lang = "c"
        elif lang == "15":
            print("C++")
            lang = "cpp"
        elif lang == "16":
            print("C#")
            lang = "csharp"
        elif lang == "17":
            print("Java")
            lang = "java"
        elif lang == "18":
            print("Kotlin")
            lang = "kotlin"
        elif lang == "19":
            print("Ruby")
            lang = "ruby"
        elif lang == "20":
            print("PHP")
            lang = "php"
        else:
            print("Invalid response.")
            langConfig(lang)
        

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
        print("12. Perl")
        print("13. Python")
        print("14. C")
        print("15. C++")
        print("16. C#")
        print("17. Java")
        print("18. Kotlin")
        print("19. Ruby")
        print("20. PHP")
        
        print(red("\n21. Exit"))
        option = input("")
        if int(option) <= 20:
            langConfig(option)
        elif option == "21":
            pref()
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
    try:
        # if sys.argv is nil then run help
        if len(sys.argv) < 2:
            help()
        elif sys.argv[1] == "--version":
            version()
        elif sys.argv[1] == "help":
            help()
        elif sys.argv[1] == "terminal":
            if terminall == False:
                print("Use "+blue("clay help", ['bold'])+" to get started, or "+blue("clay exit", ['bold'])+" to exit the clay terminal.")
            terminall = True
            terminal()
        elif sys.argv[1] == "new":
            new()
        elif sys.argv[1] == "add":
            add()
        elif sys.argv[1] == "remove":
            remove()
        elif sys.argv[1] == "build":
            massBuild()
        elif sys.argv[1] == "run":
            run(sys.argv[2])
        elif sys.argv[1] == "install":
            install(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "uninstall":
            uninstall()
        elif sys.argv[1] == "list":
            list()
        elif sys.argv[1] == "help":
            help()
        elif sys.argv[1] == "--version":
            version()
        elif sys.argv[1] == "exit":
            print(yellow("You are not in the clay terminal", ['bold']))
        elif sys.argv[1] == "clear":
            clear()
        elif sys.argv[1] == "shell":
            shell()
        elif sys.argv[1] == "pref":
            pref()
        elif sys.argv[1] == "ignore":
            void()
        else:
            print("Invalid command "+sys.argv[0]+", try "+blue("clay help", ['bold']))
    except KeyboardInterrupt:
        sys.exit(red("\n\nExiting clay", ['bold']))