# Clay
## Supported languages: 
| File | Language                       |
| ----- | ----------------------------- |
| .js   | JSX + JavaScript              |
| .jsx  | JSX + JavaScript              |
| .ts   | TypeScript + JavaScript       |
| .tsx  | TypeScript + JSX + JavaScript | 
| .mjs  | JavaScript                    |
| .cjs  | JavaScript                    |
| .mts  | TypeScript                    |
| .cts  | TypeScript                    |
| .toml | TOML                          |
| .css  | CSS                           |
| .env  | Env                           |
| .\*   | file                          |
| .lua  | Lua                           |
| .py   | Python                        |
| .rs   | Rust                          |

## Supported platforms: 
Windows, Linux, and macOS (darwin).
## Supported package managerds: 
pip, npm, and cargo, go, pip, luarocks, git, and gem.
## Supported shell languages: 
python, lua, ruby, swift, javascript, typescript, c, c++, c#, java, go, rust, kotlin, php, and dart.

# Starting
## Requirements
- [Makefile](https://www.gnu.org/software/make/)
- [Xcode](https://developer.apple.com/xcode/) (macOS only) (version 1.0.0+)
- [LLVM](https://github.com/llvm/llvm-project/releases)
- [GCC](https://gcc.gnu.org/install/)

## Install
Head over to releases and download clay.
## Build
- Download the clay source using ```git clone```
- Run ```python clay.py``` or ```python3 clay.py``` to open the terminal, you can write commands from here but it is reccomended to build it.
- Run ```sbuild``` in the terminal
- Wait for it to download, it may ask for your password
- Clay is ready for usage! 
## Embed into python
- Download the clay source using ```git clone```
- Create your python script
- Write ```import clay```
- Use the api

# Clay functions
For every language clay adds 3 keywords
- ```send(file, data)```
- ```recieve(libname)```
- ```reply(data)```
These keywords is how you will communicated between languages

## Send
Send takes in 2 inputs
- File (What file are you invoking)
- Data (Any information you want to send, default: void)

When send is called it will run the other script and send the data which can be recieved with ```recieve()```, Send returns the value that was given by the ```reply()``` function in the other script.

## Recieve
Recieve takes no inputs, recieve returns nothing, Recieve returns the data sent with the Send function.

Recieve can also recieve from clay libraries.
Use ``recieve("clay/libraryName")`` the following will return libraryName library built into clay. Use ```recieve("libraryName")``` to get a dependency

## Reply
Reply takes in one input, which is the data to be sent.

# Clay CLI 
## New
Run ``clay new`` to create a new project with a package.json file.
## Add
Add is the reccomended way to add a package/module to your project. Add will add the information to package.json and download it when the script is ran. 
## Remove
Remove is the reccomended way to remove a package/module from your project. Remove will remove the file from package.json
## Install
Install will add the package/module to dependencies and package.json
## Uninstall
Uninstall will remove the package/module from dependecies and package.json
## Pref
``clay pref`` is how you can modify the CLI.
## List
List will return all the packages/modules in package.json & dependencies
## Terminal
Open the terminal
## Exit
Exit is a command that only works in the terminal, otherwise it will produce an error. 

The exit command allows you to exit from the terminal.
## Help
Provides a guide of all commands
## sbuild
``clay sbuild`` only works on a non-built terminal, using this command will build clay. 

Read the above building documentation to learn more about sbuild.
## Version
``clay --version`` will return the version of clay you are running on
## Shell
Opens the shell for any language.

# Tutorial: Making a discord bot with Lua
This tutorial will introduce you to packages. 

## Making your project
Run ``clay new``

Name your project "DiscordBot", and make the script name "index.lua". You can fill the rest of the options to your liking.

Wait for index.lua, package.json, and the dependecies folder to be added.
## Installing discord.py
Run ``clay add``

For the first option write "pip".

For the second option write "discord.py".

The file will be added to package.json and when the project is ran it will install the dependency.
## Begin programming
Open index.lua and write the following
"local discord = request("discord.py")"
The script will import discord.py as discord. 

Now lets create the client.
```lua
local client = discord.Client
```
This client is how we will control the bot.

Now lets add some functions
```lua
function client.on_ready(self)
    print("Logged in")
end
```
This function will print "Logged in" when the bot logs in.

```lua
function client.on_message(self, message)
   if message.content == "ping" then
      message.channel.send("pong")
   end
end
```
## Finshing the script
```lua
intents = discord.Intents.default()
intents.message_content = True
client = MyClient({intents=intents})
client.run('token')
```
Add the following and test the script.

You should get a discord bot that when you write "ping" it will reply "pong".

