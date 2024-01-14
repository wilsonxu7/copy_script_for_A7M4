import os
import shutil

def copy_files():
    # 获取当前目录
    current_path = os.getcwd()

    # 构建目标路径
    destination_path = os.path.join(current_path, "筛选后")

    # 构建copy_list文件夹路径
    copy_list_folder_path = os.path.join(current_path, "copy_list")

    # 存储copy_list文件夹下的文件名
    match_name_list = []

    # 检查copy_list文件夹是否存在
    if not os.path.exists(copy_list_folder_path):
        print(f"copy_list文件夹 {copy_list_folder_path} 不存在")
        return

    # 获取copy_list文件夹下的文件名
    match_name_list = [f.split(".")[0] for f in os.listdir(copy_list_folder_path) if os.path.isfile(os.path.join(copy_list_folder_path, f))]

    # 检查目标路径是否存在，不存在则创建
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        print(f"目标路径 {destination_path} 不存在，已创建")

    # 获取当前目录下的文件名
    current_folder_files = [f.split(".")[0] for f in os.listdir(current_path) if f != "copy_list" and not os.path.isdir(f)]

    # 记录copy_list文件夹中有但没有匹配到的文件名
    unmatched_copy_list_files = set(match_name_list)

    for file_name in current_folder_files:
        # 在match_name_list中查找匹配的文件名
        if file_name in match_name_list:
            # 从unmatched_copy_list_files中移除匹配成功的文件名
            unmatched_copy_list_files.discard(file_name)

            # 构建源ARW文件路径
            arw_source_path = os.path.join(current_path, f"{file_name}.ARW")

            # 构建目标ARW文件路径
            arw_destination_path = os.path.join(destination_path, f"{file_name}.ARW")

            # 复制ARW文件
            if os.path.exists(arw_source_path):
                shutil.copy(arw_source_path, arw_destination_path)
                print(f"ARW文件 {file_name}.ARW 复制成功到 {destination_path}")

            # 构建源JPG文件路径
            jpg_source_path = os.path.join(current_path, f"{file_name}.JPG")

            # 构建目标JPG文件路径
            jpg_destination_path = os.path.join(destination_path, f"{file_name}.JPG")

            # 复制JPG文件
            if os.path.exists(jpg_source_path):
                shutil.copy(jpg_source_path, jpg_destination_path)
                print(f"JPG文件 {file_name}.JPG 复制成功到 {destination_path}")
        else:
            print(f"文件名 {file_name} 没有匹配成功")

    # 将在copy_list文件夹中有但没有匹配到的文件名输出到unmatched_copy_list.txt
    unmatched_copy_list_file_path = "unmatched_copy_list.txt"
    with open(unmatched_copy_list_file_path, "w") as unmatched_copy_list_file:
        unmatched_copy_list_file.write("\n".join(unmatched_copy_list_files))
    print(f"copy_list文件夹中有但没有匹配到的文件名已记录到 {unmatched_copy_list_file_path}")

# 调用函数进行复制
copy_files()
