import copy
import os
import os.path


def find_dir(target_path, type):
    start_current_dir = os.path.abspath(os.getcwd())

    migration_dir_list = []
    while not migration_dir_list:
        file_list = os.listdir()
        migration_dir_list = [i for i in file_list if i == target_path]
        if migration_dir_list:
            break
        else:
            os.chdir(os.path.dirname(os.getcwd()))

            continue

    for dir_s in migration_dir_list:
        if os.path.isdir(dir_s):
            migrations = dir_s
            break
        else:
            continue

    os.chdir(migrations)
    work_dir = os.getcwd()
    work_dir = os.path.normcase(work_dir)
    work_dir = os.path.normpath(work_dir)
    result_target_path = os.path.realpath(work_dir)

    file_list = os.listdir()
    file_list = [i for i in file_list if i[-4:] == type]

    os.chdir(start_current_dir)

    return result_target_path, file_list


def search_str_in_file(file_name, search):
    with open(os.path.join(file_name)) as f:
        read = f.readline()
        if search in read:
            return True
    return False


def main():
    migration_dir_str, file_list = find_dir('Migrations', '.sql')

    while True:
        search_str = input('Введите строку для поиска:')
        count = 0
        founded_files = []
        for file_name in file_list:
            if search_str_in_file(os.path.join(migration_dir_str, file_name), search_str):
                count += 1
                founded_files.append(file_name)
            else:
                continue

        file_list = copy.deepcopy(founded_files)

        if count > 10:
            choice = input('Много совпадений: Вывести весь список -1 , только количество - 2')
            if choice == '1':
                for f_name in founded_files:
                    print(f_name)
            elif choice == '2':
                print('Всего:', count)
            else:
                print('неизвестная команда попробуйте снова')
        elif count == 0:
            print('Ничего не найдено')
            break
        else:
            for f_name in founded_files:
                print(f_name)


if __name__ == '__main__':
    main()
