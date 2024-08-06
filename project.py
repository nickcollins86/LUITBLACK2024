import os

def get_files_info():
    files_info = []
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            file_info = {
                'name': filename,
                'size': os.path.getsize(filename)
            }
            files_info.append(file_info)
    return files_info

if __name__ == "__main__":
    files_info = get_files_info()
    for file_info in files_info:
        print(file_info)




