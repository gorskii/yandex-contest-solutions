def get_result_code(exit_code, interactor_code, checker_code):
    if interactor_code == 0:
            return 3 if exit_code != 0 else checker_code
    elif interactor_code == 1:
            return checker_code
    elif interactor_code == 4:
            return 3 if exit_code != 0 else 4
    elif interactor_code == 6:
            return 0
    elif interactor_code == 7:
            return 1

    return interactor_code


if __name__ == '__main__':
    exit_code = int(input())
    interactor_code = int(input())
    checker_code = int(input())

    print(get_result_code(exit_code, interactor_code, checker_code))

