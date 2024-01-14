# 使用场景：
1. 使用SONY相机拍摄图片后，使用creator将2M的缩略图传输到手机，与伙伴在阿里云盘共享。
2. 小伙伴对满意的图片标注收藏。
3. 旅行结束后，将收藏的图片（2M）返回给我。
4. 通过此脚本进行文件名匹配，并输出，随后将匹配后的图片（高质量JPG & ARW）返回给小伙伴。

# 使用方法：
1. 将需要匹配的图片放入`copy_list`文件夹中。
2. `copy_list`文件夹与`copy.py`文件均放在当前目录下。目录格式如下：
```.
├── DSC00733.ARW
├── DSC00733.JPG
├── DSC00837.ARW
├── DSC01369.ARW
├── DSC01965.ARW
├── copy.py
├── copy_list
│   ├── DSC00733.JPG
│   ├── DSC00837.JPG
│   ├── DSC05744.JPG
│   └── DSC05749.JPG
├── unmatched_copy_list.txt
└── 筛选后
    ├── DSC00733.ARW
    ├── DSC00733.JPG
    └── DSC00837.ARW
```
3. `python copy.py`
4. 筛选结果在"筛选后"文件夹中，`unmatched_copy_list.txt`保存`copy_list`中为匹配成功的文件名。

# 这个python脚本由GPT3.5创作。
1. 这是一个通过匹配文件名（不包含文件格式）的复制脚本。
2. 复制的目标路径（相对路径）是“筛选后”。如果目标目录不存在，则新建。
3. 用于匹配的文件名来自“copy_list”文件夹下的文件。
4. 对当前目录下所有（不包括copy_list文件见）的文件进行文件名匹配（不包含文件格式）。
5. 如果匹配到了，则将则将对应的JPG和ARW的文件复制到目标路径。
6. 将没有匹配成功的文件名保存到 unmatched_copy_fail.txt 中，如果unmatched_copy_fail.txt不存在则新建。
7. 在匹配过程中打印对应日志。
