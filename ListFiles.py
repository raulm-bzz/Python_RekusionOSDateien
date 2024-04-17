import os

files = []
counter = 0


def scan(start_path:str="C:/", filetype=None):
    global counter
    for file in os.listdir(start_path):
        try:
            if os.path.isdir(f"{start_path}/{file}"):
                scan(start_path=f"{start_path}/{file}", filetype=filetype)
            else:
                if filetype and file.endswith(filetype):
                    files.append([file, start_path])
                    counter += 1
                    print(counter)
                elif filetype is None:
                    files.append([file, start_path])
                    counter += 1
                    print(counter)
        except PermissionError:
            pass
        except FileNotFoundError:
            pass


scan(filetype=input("Filetype (leave blank for all) >"))
print("fangt ah sortiere")
files = sorted_list = sorted(files, key=lambda x: x[0])
print("fangt ah schribe")
with open("filelist.txt", "w") as f:
    for i, file in enumerate(files):
        try:
            for attribute in file:
                f.write(f"{file[0]};{file[1]}")
            print(f"Wrote {i} filenames")
        except UnicodeEncodeError:
            pass
input("Done")
