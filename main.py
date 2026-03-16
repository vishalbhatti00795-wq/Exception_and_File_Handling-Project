from pathlib import Path
import os
def create_folder():
    try:
        name = input('please tell your folder name:- ')
        p = Path(name)
        p.mkdir()
        print('folder created successfully')
    except Exception as e:
        print(f"Sorry an error occured as {e}!")


def read_file_folder():
    p = Path("")
    items = list(p.rglob('*'))
    for i,v in enumerate(items):
        print(f'{i + 1} : {v}')


def update_folder():
    try:
        read_file_folder()
        old_name = input('please tell your folder you want to update:- ')
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input('please tell your new folder name:- ')
            new_p = Path(new_name)
            p.rename(new_p)
            print('Your folder name is updated successfully')
    except Exception as e:
        print(f"Sorry an error occured as {e}!")
    else:
        print('No such folder exists')


def del_folder():
    try:
        read_file_folder()
        name = input('please tell which folder you want to delete:- ')
        p = Path(name)
        if p.exists() and p.is_dir():
            p.rmdir()
            print('folder deleted successfully')

        else:
            print('No such folder exists')

    except Exception as e:
        print(f"Sorry an error occured as {e}!")

def create_file():
    try:
        read_file_folder()
        name = input('please tell your file name:- ')
        p = Path(name)
        if not p.exists():
            with open(name, 'w') as fs:
                data = input('Write what want in file:- ')
                fs.write(data)
            print('file created successfully')

        else:
            print('Sorry this name file already exists')
    except Exception as e:
        print(f"Sorry an error occured as {e}!")


def read_file():
    try:
        read_file_folder()
        name = input('please tell your file name:- ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name, 'r') as fs:
                content = fs.read()
                print('Your file content is:- ')
                print(content)

        else:
            print('No such file exists')
    except Exception as e:
        print(f"Sorry an error occured as {e}!")


def update_file():
    try:
        read_file_folder()
        name = input('please tell your file name:- ')
        p = Path(name)
        if p.exists() and p.is_file():
            print('Options')
            print('1. For renaming the file')
            print('2. For appending something in the file')
            print('3. For overwriting the file content')

            choice = int(input('Enter your choice: '))
            if choice == 1:
                new_name = input('please tell your new file name with extension:- ')
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print('Your file name is changed successfully')

                else:
                    print('Sorry this name file already exists')

            if choice == 2:
                with open(name, 'a') as fs:
                    data = input('Write what want to append in the file:- ')
                    fs.write(" " + data)
                print('Data appended successfully')

            if choice == 3:
                with open(name, 'w') as fs:
                    data = input('Write what want to overwrite in the file:- ')
                    fs.write(" " + data)
                print('Data overwrite successfully')

    except Exception as e:
        print(f"Sorry an error occured as {e}!")


def delete_file():
    try:
        read_file_folder()
        name = input('please tell your file name with extension you want to delete:- ')
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print('file deleted successfully')

        else:
            print('Sorry no such file exists')

    except Exception as e:
        print(f"Sorry an error occured as {e}!")


while True:
    print('Options:- ')

    print('1. Create a folder')
    print('2. Read files and folders')
    print('3. Update the folder')
    print('4. Delete the folder')
    print('5. Create a file')
    print('6. Read a file')
    print('7. Update a file')
    print('8. Delete a file')
    print('0. Exit the program')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        create_folder()

    if choice == 2:
        read_file_folder()

    if choice == 3:
        update_folder()

    if choice == 4:
        del_folder()

    if choice == 5:
        create_file()

    if choice == 6:
        read_file()

    if choice == 7:
        update_file()

    if choice == 8:
        delete_file()