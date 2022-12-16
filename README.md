# Clay
## Supported languages: 
Python, Lua, Ruby, Swift, JavaScript, TypeScript, C, C++, C#, Java, Go, Rust, Kotlin, PHP, and Dart.
## Supported platforms: 
Windows, Linux, and macOS (darwin).
## Supported package managerds: 
pip, npm, and cargo, go, pip, luarocks, git, and gem.
## Supported shell languages: 
python, lua, ruby, swift, javascript, typescript, c, c++, c#, java, go, rust, kotlin, php, and dart.

# Starting
## Install
Head over to releases and download clay.
## Build
- Download the clay source using "git clone"
- Run "python clay.py" or "python3 clay.py" to build open the terminal, you can write commands from here but to get the full functionality you need to build it.
- Run "sbuild" in the terminal
- Wait for it to download, it may ask for your password
- Clay is ready for usage! 
## Embed into python
- Download the clay source using "git clone"
- Create your python script
- Write "import clay"
- Use the api

# Clay functions
For every language clay adds 3 keywords
- send
- recieve
- reply
These keywords is how you will communicated between languages

## Send
Send takes in 2 inputs
- File (What file are you invoking)
- Data (Any information you want to send, default: void)

When send is called it will run the other script and send the data which can be recieved with recieve(), Send returns the value that was given by the reply() function in the other script.

## Recieve
Recieve takes no inputs, recieve returns nothing, Recieve returns the data sent with the Send function.

## Reply
Reply takes in one input, which is the data to be sent.

# Clay CLI 
## New
Run "clay new" to create a new project with a package.json file.
## Add
Add is the reccomended way to add a package/module to your project. Add will add the information to package.json and download it when the script is ran. 
## Remove
Remove is the reccomended way to remove a package/module from your project. Remove will remove the file from package.json
## Install
Install will add the package/module to dependencies and package.json
## Uninstall
Uninstall will remove the package/module from dependecies and package.json
## Pref
"clay pref" is how you can modify the CLI.
## List
List will return all the packages/modules in package.json & dependencies
## Terminal
Open the terminal