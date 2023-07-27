From ultralytics/ultralytics:latest-cpu

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install scikit-learn
COPY dataset.py train.py /usr/src/ultralytics/
