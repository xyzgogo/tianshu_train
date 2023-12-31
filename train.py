from ultralytics import YOLO

from dataset import *

import argparse


# 数据集路径   /dataset/YOLO
# 模型路径    /modeldir
# --train_model_out=/workspace/model-out
# train_out=/workspace/out
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# pip install scikit-learn ultralytics

def data_process():
    # 数据集切分
    split_dataset('/dataset/YOLO/obj_train_data', '/dataset/YOLO')
    generate_yaml_from_txt('/dataset/YOLO/obj.names', '/dataset/YOLO/cfg.yaml', '/dataset/YOLO')


def main():
    parser = argparse.ArgumentParser(description="Example script with long options.")
    # 添加长选项
    parser.add_argument("--epochs", type=int, help="train epochs")
    args, _ = parser.parse_known_args()
    # Load a model
    model = YOLO('/modeldir/yolov8n.pt')
    # Train the model
    model.train(data='/dataset/YOLO/cfg.yaml', epochs=args.epochs, imgsz=640)


if __name__ == "__main__":
    data_process()

    source_path = "/workspace/out"
    os.makedirs(source_path, exist_ok=True)
    target_path = "runs"  # 在当前目录下创建名为 "runs" 的软链接
    create_symlink(source_path, target_path)

    main()

    source_directory = "/workspace/out/detect/train/weights"
    destination_directory = "/workspace/model-out"

    copy_directory(source_directory, destination_directory)
