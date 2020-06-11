import os



if __name__ == '__main__':
    dir_name = input()
    abs_dir_path = os.path.join(os.path.abspath("."), dir_name)
    if os.path.exists(abs_dir_path):
        print("path: {} already exist".format(abs_dir_path))
        exit(0)

    os.mkdir(os.path.join(os.path.abspath("."), dir_name))

    with open(os.path.join(abs_dir_path, "solution.py"), "w") as f1:
        pass

    with open(os.path.join(abs_dir_path, "README.md"), "w") as f2:
        pass
