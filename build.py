import subprocess

subprocess.run("pyside6-uic ui/main.ui -o ui_main.py", shell=True)
subprocess.run("pyside6-rcc main.qrc -o main_rc.py", shell=True)