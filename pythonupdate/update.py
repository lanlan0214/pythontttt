# import os
# import shutil
# import subprocess
# from tkinter import messagebox


# def read_version():
#     try:
#         # 確定本地 version.txt 檔案存在
#         local_version_file = "version.txt"

#         if os.path.exists(local_version_file):
#             # 讀取本地版本號
#             with open(local_version_file, 'r') as file:
#                 local_version = file.readline().strip()
#         else:
#             # 如果找不到本地版本檔案，從指定路徑拉取 version.txt 檔案
#             local_version_file = r"\\192.168.0.180\軟體_\_Tim\_app\Debug\version.txt"
#             if os.path.exists(local_version_file):
#                 # 讀取目標路徑中的版本號
#                 with open(local_version_file, 'r') as file:
#                     local_version = file.readline().strip()
#             else:
#                 # 如果仍找不到版本檔案，提示用戶請詢問工程師
#                 messagebox.showerror("錯誤", "找不到本地版本檔案。請詢問工程師。")
#                 return

#         # 目標路徑中的版本檔案
#         target_version_file = r"\\192.168.0.180\軟體_\_Tim\_app\Debug\version.txt"
#         if os.path.exists(target_version_file):
#             # 讀取目標路徑中的版本號
#             with open(target_version_file, 'r') as target_file:
#                 target_version = target_file.readline().strip()

#             # 比較版本號
#             if target_version >= local_version:
#                 # 如果目標版本較新，替換本地的 version.txt 檔案
#                 shutil.copyfile(target_version_file, local_version_file)
                
#                 # 使用 subprocess 啟動報表app.exe
#                 report_app_path = r"\\192.168.0.180\軟體_\_Tim\_app\Debug\報表app.exe"
                
#                 subprocess.Popen(report_app_path)
#             else:
#                 # 使用 subprocess 啟動報表app.exe
#                 report_app_path = r"\\192.168.0.180\軟體_\_Tim\_app\報表app(自動更新版)\Debug\報表app.exe"
#                 subprocess.Popen(report_app_path)
#         else:
#             messagebox.showerror("錯誤", "找不到目標版本檔案。請詢問工程師。")
#     except Exception as e:
#         messagebox.showerror("錯誤", f"讀取版本號時出現錯誤: {str(e)}")

# if __name__ == "__main__":
#     read_version()

import os
import shutil
import subprocess
from tkinter import messagebox


def read_version():
    try:
        # 確定本地 version.txt 檔案存在
        local_version_file = "version.txt"

        if os.path.exists(local_version_file):
            # 讀取本地版本號
            with open(local_version_file, 'r') as file:
                local_version = file.readline().strip()
        else:
            # 如果找不到本地版本檔案，從指定路徑拉取 version.txt 檔案
            local_version_file = r"\\192.168.0.180\軟體_\_Tim\_app\Debug\version.txt"
            if os.path.exists(local_version_file):
                # 讀取目標路徑中的版本號
                with open(local_version_file, 'r') as file:
                    local_version = file.readline().strip()
            else:
                # 如果仍找不到版本檔案，提示用戶請詢問工程師
                messagebox.showerror("錯誤", "找不到本地版本檔案。請詢問工程師。")
                return

        # 目標路徑中的版本檔案
        target_version_file = r"\\192.168.0.180\軟體_\_Tim\_app\Debug\version.txt"
        if os.path.exists(target_version_file):
            # 讀取目標路徑中的版本號
            with open(target_version_file, 'r') as target_file:
                target_version = target_file.readline().strip()

            # 比較版本號
            if target_version >= local_version:
                # 如果目標版本較新，替換本地的 version.txt 檔案
                shutil.copyfile(target_version_file, local_version_file)
                
                # 將Debug資料夾內容複製到桌面
                debug_folder = r"\\192.168.0.180\軟體_\_Tim\_app\Debug"
                desktop_path = os.path.expanduser("~/Desktop")
                shutil.copytree(debug_folder, os.path.join(desktop_path, "Debug"), dirs_exist_ok=True)
                
                # 使用 subprocess 啟動桌面的報表app.exe
                report_app_path = os.path.join(desktop_path, "Debug", "報表app.exe")
                subprocess.Popen(report_app_path)
            else:
                # 使用 subprocess 啟動報表app.exe (自動更新版)
                report_app_path = r"\\192.168.0.180\軟體_\_Tim\_app\報表app(自動更新版)\Debug\報表app.exe"
                subprocess.Popen(report_app_path)
        else:
            messagebox.showerror("錯誤", "找不到目標版本檔案。請詢問工程師。")
    except Exception as e:
        messagebox.showerror("錯誤", f"讀取版本號時出現錯誤: {str(e)}")

if __name__ == "__main__":
    read_version()
