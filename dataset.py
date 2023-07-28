import os
import shutil
from sklearn.model_selection import train_test_split


def split_dataset(dataset_folder,output_folder):
    # 数据集文件夹路径

    # 获取所有图片文件和标注文件的路径
    image_files = [file for file in os.listdir(dataset_folder) if file.endswith(".jpg")]
    annotation_files = [file for file in os.listdir(dataset_folder) if file.endswith(".txt")]

    # 确保图片和标注文件对应
    image_files.sort()
    annotation_files.sort()

    # 将数据集切分为训练集、验证集和测试集
    train_files, temp_files = train_test_split(image_files, test_size=0.3, random_state=42)
    valid_files, test_files = train_test_split(temp_files, test_size=0.2, random_state=42)

    # 创建目标文件夹，用于保存切分后的数据集
    train_folder = os.path.join(output_folder, "train")
    valid_folder = os.path.join(output_folder, "valid")
    test_folder = os.path.join(output_folder, "test")

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(valid_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # 将切分后的文件复制到对应的文件夹
    for file in train_files:
        shutil.copy(os.path.join(dataset_folder, file), os.path.join(train_folder, file))
        shutil.copy(os.path.join(dataset_folder, file.replace(".jpg", ".txt")), os.path.join(train_folder, file.replace(".jpg", ".txt")))

    for file in valid_files:
        shutil.copy(os.path.join(dataset_folder, file), os.path.join(valid_folder, file))
        shutil.copy(os.path.join(dataset_folder, file.replace(".jpg", ".txt")), os.path.join(valid_folder, file.replace(".jpg", ".txt")))

    for file in test_files:
        shutil.copy(os.path.join(dataset_folder, file), os.path.join(test_folder, file))
        shutil.copy(os.path.join(dataset_folder, file.replace(".jpg", ".txt")), os.path.join(test_folder, file.replace(".jpg", ".txt")))

    print("数据集切分完成！")


def generate_yaml_from_txt(input_file, output_file,dataset_dir):
    # Read the input txt file and extract non-empty lines
    with open(input_file, "r",encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    # Write the YAML content to the output file
    with open(output_file, "w",encoding="utf-8") as f:
        f.write(f"train: {dataset_dir}/train\n")
        f.write(f"val: {dataset_dir}/valid\n")
        f.write(f"test: {dataset_dir}/test\n")
        f.write("# number of classes\n")
        f.write(f"nc: {len(lines)}\n\n")
        f.write("# class names\n")
        f.write("names:\n")
        for idx, line in enumerate(lines):
            f.write(f"  {idx}: {line}\n")


def create_symlink(source, target):
    try:
        os.symlink(source, target)
        print(f"Created symlink: {target} -> {source}")
    except OSError as e:
        print(f"Failed to create symlink: {target} -> {source}")
        print(f"Error: {e}")


def copy_directory(source, destination):
    try:
        shutil.copytree(source, destination)
        print("Directory copied successfully.")
    except FileExistsError:
        print(f"Destination directory '{destination}' already exists.")
    except Exception as e:
        print(f"An error occurred while copying: {e}")
# split_dataset('./yolo/obj_train_data','./yolo')

# # Example usage
# input_txt_file = "./yolo/obj.names"  # Replace with the path to your input txt file
# output_yaml_file = "output.yaml"  # Replace with the desired path for the output yaml file
#
# generate_yaml_from_txt(input_txt_file, output_yaml_file,'d:/download/tmp/yolov8-test/yolo')
