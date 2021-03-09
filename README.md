# AIOps2021复赛评测脚本

## 主要内容

[example](example/)目录提供了Python样例程序，说明如何消费Kafka、输出答案。

同时，提供了评分demo，以及可供测试的选手答案和标准答案。

注意：文件答案格式，仅供该仓库的评分程序使用，选手依然需要使用样例程序中的方式进行答案提交。

## 评分demo使用方式

为多个队伍打分。
- 执行`python assemble.py --answer sample_answer.json --result-dir result --team-list team.csv`获得不同队伍的分数。
- 使用`--score`参数选择不同的评分方式。

