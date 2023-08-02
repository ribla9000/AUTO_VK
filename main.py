from endpoints.check_req import check_req


def main():
    try:
        from endpoints.gui import run_choose_prof
        run_choose_prof()
    except:
        check_req()
        try:
            from endpoints.gui import run_choose_prof
            run_choose_prof()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()






