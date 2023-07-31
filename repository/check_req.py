import os


def check_requirements():
    try:
        os.system("pip install -r requirements.txt")
    except:
        os.system("pip3 install -r requirements.txt")
    
    try:
        try:
            os.system("sudo dpkg -i --force-depends src/google-chrome-stable_current_amd64.deb")
            os.system("sudo apt-get install -f")
            os.system("sudo apt install chromium-browser")
            os.system("sudo apt update")
        except:
            os.system("dpkg -i --force-depends src/google-chrome-stable_current_amd64.deb")
            os.system("apt-get install -f")
            os.system("apt install firefox chromium-browser")
            os.system("apt update")
    
    except Exception as e:
        print(e)
    return
