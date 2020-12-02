# adventOfCode2020
Ted's further adventures in python and the Advent Of Code 2020


# How to setup your environment
We are using Linux, python3 (3.8.6) and a python virtual enviroment. This whole setup is based on the tutorial found at: https://realpython.com/python-virtual-environments-a-primer/

## Install VSCode packages
```
cd ~/tmp
git clone https://aur.archlinux.org/visual-studio-code-bin.git
cd visual-studio-code-bin/
makepkg -si
```
  
## Enable the python virtual environment
`python -m venv env`

In order to activate this vitrual environment in the shell, run the following command
`source env/bin/activate`

To deactivate it run `deactivate`

## Required Python Packages
The file requirements.txt has the list of required python packages. Install the packages with the command: `pip install -r requirements.txt`

## Configure VSCode 
### Extensions
Use the File -> Preferences -> Extensions menu option to open the extensions panel. Search for the extension name and push the green install button. You may have to reload VSCode. Install the following extensions:
* Python  
* Code-Runner

### Settings
* Add the python virtual environment to VSCode  
Type the settings key (crtl ,) to open the settings window in VSCode. Or use the File -> Preferences -> Settings menu option. This will open two panels: User Settings and Workspace Settings. Click on Workspace Settings.
Search for _python.pythonpath_ and then enter the following: `env/bin/python`

* Change the default python command that Code-Runner uses to your virtual python environment
Open the workspace settings file located in .vscode/settings.json and add the json snippet:
```
"code-runner.executorMap": {
        "python":  "env/bin/python",
    }
```

* Configure VSCode to use the python unittest framework
Open the workspace settings file located in .vscode/settings.json and add the json snippet:
```
 "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./test",
        "-p",
        "*_test.py"
    ],
    "python.testing.pyTestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.flake8Enabled": false,
    "python.linting.enabled": true
```

* Turn off Code Lens in the editor 
`"editor.codeLens": false`

## Running unit tests in the terminal
~~python -m unittest discover -s ./test -p *_test.py~~

## Bibliography
* https://adventofcode.com/2020
* https://realpython.com/python-virtual-environments-a-primer/
* https://lobotuerto.com/blog/how-to-install-visual-studio-code-in-manjaro-linux/