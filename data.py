import os
import json

PATH_TRAIN = os.path.join(
    os.getcwd(),
    "data",
    "images",
    "any",
    "train"
)

PATH_TEST = os.path.join(
    os.getcwd(),
    "data",
    "images",
    "any",
    "test"
)

PATH_BEN_TRAIN = os.path.join(
    os.getcwd(),
    "data",
    "imglist",
    "benchmark_any",
    "train_any.txt"
)

PATH_BEN_TEST = os.path.join(
    os.getcwd(),
    "data",
    "imglist",
    "benchmark_any",
    "test_any.txt"
)

with open(PATH_BEN_TRAIN, "w") as f:
    for index, name in enumerate(sorted(os.listdir(PATH_TRAIN))):
        obj = {"label": index, "sc_label": index, "full_label": index}
        for file in sorted(os.listdir(os.path.join(PATH_TRAIN, name))):
            f.write(os.path.join("any", "train", name, file)+ " " + json.dumps(obj) + "\n")
    f.close()

with open(PATH_BEN_TEST, "w") as f:
    for index, name in enumerate(sorted(os.listdir(PATH_TEST))):
        obj = {"label": index, "sc_label": index, "full_label": index}
        for file in sorted(os.listdir(os.path.join(PATH_TEST, name))):
            f.write(os.path.join("any", "test", name, file)+ " " + json.dumps(obj) + "\n")
    f.close()