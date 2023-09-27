from endpoints.check_req import check_req, install_google_chrome


def main():
    try:
        install_google_chrome()
        from endpoints.gui import run_choose_prof
        run_choose_prof()
    except:
        install_google_chrome()
        check_req()
        try:
            from endpoints.gui import run_choose_prof
            run_choose_prof()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()






