import os
import subprocess
import re
import time

invalid_chars = re.compile(r"[&/]")
with open('subjects.txt') as f:
    for subject in f:
        time.sleep(5)  # 等待5秒
        if invalid_chars.search(subject): # 删去带& /的
            print("fail:%s" % subject)
        else:
            subject = subject.strip()
            try:
                command = f"python .\\getNgrams.py {subject} -corpus=eng_2019 -startYear=1500 -endYear=2019 -smoothing=3 -csv -quit -noprint"
                # os.system(command)
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError:
                # print(f"运行命令失败: {command}")
                # print(f"错误信息: {e}")
                print("fail:%s"%subject)