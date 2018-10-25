import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\prank")
    print(file_list)
    os.chdir(r"C:\prank")
    # for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789") )  # type: None

rename_files()