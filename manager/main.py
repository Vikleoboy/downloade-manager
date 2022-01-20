import os
import shutil



def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

downlode_folder_path = get_download_path()

ext_list = [('apps', ['.exe' ,'.msi']) , ('Pdfs',['.pdf']) , ('Pics' , ['.jpg', '.png' , '.jpeg' , '.gif'] ) , ('Videos' , ['.mp4' , '.mkv']) ]

print(downlode_folder_path)
for i in os.listdir(downlode_folder_path):
    file = os.path.splitext(i)
    dose_not_exist = False
    dir_name = []
    # print(file)
    # print(file[-1])
    for u in ext_list:
        try:
            if file[-1] in  u[-1]:
                print('doing ')
                os.mkdir(os.path.join(downlode_folder_path , u[0]))
                dir_name.append(u[0])
                os.rename(os.path.join(downlode_folder_path , i) , os.path.join(downlode_folder_path , u[0] , i ) )
                dose_not_exist = False
            else :
                dose_not_exist = True
        except FileExistsError :
            os.rename(os.path.join(downlode_folder_path , i) , os.path.join(downlode_folder_path , u[0] , i ) )
    if dose_not_exist :
        try:
            os.mkdir(os.path.join(downlode_folder_path , file[-1].replace('.','') ))
            dir_name.append(file[-1].replace('.',''))
            os.rename(os.path.join(downlode_folder_path , i) , os.path.join(downlode_folder_path , file[-1].replace('.','') , i ) )
        except FileExistsError : 
            try :
                os.rename(os.path.join(downlode_folder_path , i) , os.path.join(downlode_folder_path , file[-1].replace('.','') , i ) )
            except FileNotFoundError :
                continue
            



