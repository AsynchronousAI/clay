# author: @AsynchronousAI
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

    languages = {
        "python": {
            "name": "python",
            "extension": ".py",
            "command": "python @file @args",
            "install": makeInstall("python", "python", "python", "python")
        },
        "php": {
            "name": "php",
            "extension": ".php",
            "command": "php @file @args",
            "install": makeInstall("php", "php", "php", "php")
        },
        "javascript": {
            "name": "javascript",
            "extension": ".js",
            "command": "node @file @args",
            "install": makeInstall("node", "nodejs", "node", "nodejs")
        },
        "java": {
            "name": "java",
            "extension": ".java",
            "command": "java @file @args",
            "install": makeInstall("java", "java", "java", "java")
        },
        "c": {
            "name": "c",
            "extension": ".c",
            "command": "gcc @file -o @file.out && @file.out @args",
            "install": makeInstall("gcc", "gcc", "gcc", "gcc")
        },
        "c++": {
            "name": "c++",
            "extension": ".cpp",
            "command": "g++ @file -o @file.out && @file.out @args",
            "install": makeInstall("g++", "g++", "g++", "g++")
        },
        "c#": {
            "name": "c#",
            "extension": ".cs",
            "command": "csc @file && @file.exe @args",
            "install": makeInstall("csc", "csc", "csc", "csc")
        },
        "go": {
            "name": "go",
            "extension": ".go",
            "command": "go run @file @args",
            "install": makeInstall("go", "go", "go", "go")
        },
        "ruby": {
            "name": "ruby",
            "extension": ".rb",
            "command": "ruby @file @args",
            "install": makeInstall("ruby", "ruby", "ruby", "ruby")
        },
        "swift": {
            "name": "swift",
            "extension": ".swift",
            "command": "swift @file @args",
            "install": makeInstall("swift", "swift", "swift", "swift")
        },
        "kotlin": {
            "name": "kotlin",
            "extension": ".kt",
            "command": "kotlinc @file -include-runtime -d @file.jar && java -jar @file.jar @args",
            "install": makeInstall("kotlinc", "kotlin", "kotlin", "kotlin")
        },
        "rust": {
            "name": "rust",
            "extension": ".rs",
            "command": "rustc @file && @file @args",
            "install": makeInstall("rustc", "rust", "rust", "rust")
        },
        "lua": {
            "name": "lua",
            "extension": ".lua",
            "command": "lua @file @args",
            "install": makeInstall("lua", "lua", "lua", "lua")
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
        if lang["extension"] == extension:
            language = lang
            break
    if language == None:
        print(red("Invalid script extension."))
        return
    # check if the language is installed
    if utilExists(language["name"]) == False:
        print("Language not installed. Installing...")
        language["install"]()
    # run the script
    runCommand(language["command"].replace("@file", script).replace("@args", " ".join(sys.argv[2:])), True)
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
def run():
    if exists("project.json") == True: 
        with open('project.json', 'r') as f:
          package = (json.load(f))
          script = package["script"]
        data = {
            "requests": ["void"],
            "data": ["void"],    
            "return": ["void"]
        }
        with open("Runlogs.json", "w") as file:
            json.dump(data, file)

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
        if technique == "":
            technique = input("How would you like to install the package? (npm, git, cargo, gem, pip, go, luaRocks, url): ")
        if technique == "npm":
            if utilExists("npm") == False:
                print("npm is required to install this package. You can install it from https://npmjs.com, We tried to install it for you, but this version of clay doesn't have npm support yet.")
            if not name:
                name = input("Package name: ")
            add(name, "npm")
            print("Installing "+name+"...")
            os.system("npm install "+name)

            if exists("package.json") == True:
                os.remove("package.json")
            if exists("package-lock.json") == True:
                os.remove("package-lock.json")
            if exists("bun.lock") == True:
                os.remove("bun.lock")
            if exists("bun.lockb") == True:
                os.remove("bun.lockb")

            # rather than keeping the items in node_modules, we will keep the items in dependencies and delete the node_modules folder
            # move the items in node_modules to dependencies
            os.system("mv node_modules/* dependencies")

            # delete node_modules
            shutil.rmtree("node_modules")

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
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

            if not name:
                url = input("Git URL: ")
            add(url, "git")
            print("Installing "+url+"...")
            os.system("git clone "+url+" dependencies/"+url.split("/")[-1])

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
            #    f.write(json.dumps(json.load(x).dependencies.append("git:"+url)))
        elif technique == "url":
            if not name:
                url = input("URL: ")
            add(url, "url")
            print("Installing "+url+"...")
            os.system("curl "+url+" > dependencies/"+url.split("/")[-1])

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
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

            if not name:
                name = input("Package name: ")
            add(name, "luaRocks")
            print("Installing "+name+"...")
            os.system("luarocks install "+name+" --tree=dependencies/"+name)

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
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
        
            if not name:
                name = input("Package name: ")
            add(name, "pip")
            print("Installing "+name+"...")
            os.system("pip install "+name+" --target dependencies/"+name)

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
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

            if not name:
                name = input("Package name: ")
            add(name, "gem")
            print("Installing "+name+"...")
            os.system("gem install "+name+" --install-dir dependencies/"+name)

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
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
            if not name:
                name = input("Package name: ")
            add(name, "cargo")
            print("Installing "+name+"...")
            os.system("cargo install "+name+" --root dependencies/"+name)

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
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
            if not name:
                name = input("Package name: ")
            add(name, "go")
            print("Installing "+name+"...")
            os.system("go get "+name+" dependencies/"+name)

            #with open('project.json', 'w') as f:
            #    x = open("project.json", "r")
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
            run()
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