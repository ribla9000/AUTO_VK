from endpoints.gui import run_choose_prof
from endpoints.check_req import check_req


def main():
    try:
        run_choose_prof()
    except:
        check_req()
    

if __name__ == '__main__':
    main()






