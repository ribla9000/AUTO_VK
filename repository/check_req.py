import os


def check_requirements():
    try:
        os.system("sudo apt install pip -y")
        os.system("pip install -r requirements.txt -f -y")
    except:
        os.system("pip3 install -r requirements.txt -f -y")
    
    try:
        try:
            os.system("sudo apt install libgl1-mesa-glx -f -y")
            os.system("sudo dpkg -i --force-depends src/google-chrome-stable_current_amd64.deb")
            os.system("sudo apt-get install -f -y")
            os.system("sudo apt update -y")
            os.system("sudo apt install chromium -y")
            os.system("sudo apt upgrade -y")
            os.system("sudo apt --fix-broken install -y")
            
        except:
            os.system("apt install libgl1-mesa-glx -f -y")
            os.system("dpkg -i --force-depends src/google-chrome-stable_current_amd64.deb")
            os.system("apt-get install -f -y")
            os.system("apt update -y")
            os.system("apt install chromium -y")
            os.system("apt upgrade -y")
            os.system("apt --fix-broken install -y")
    
    except Exception as e:
        print(e)
    return
