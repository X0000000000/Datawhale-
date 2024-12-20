import os
with open('训练集.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    #删除空行
    lines = [line for line in lines if line.strip()]

    #在行首位加上“”
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = '"' + lines[i] + '"\n'

#在每一句话前面加入序号，如果有就不用看到这里,鼠标选中
# for i in range(len(lines)):和lines[i] = str(i+1) + lines[i]，按下Ctrl+?,取消注释，并运行
    # for i in range(len(lines)):
    #     lines[i] = str(i+1) + lines[i]
    #在每一行前面加上output：
    for i in range(len(lines)):
        lines[i] = '"output":' + lines[i]
    for i in range(len(lines)):
        lines[i] = '"instruction" : "  ",'+'\n'+'"input":"  " , '+'\n' + lines[i]
    #在每一行前后加入{}
    for i in range(len(lines)):
        lines[i] = '{' +'\n' + lines[i] + '}'+','
    for i in range(len(lines)):
        lines[i] = lines[i] +'\n'
    #删除最后一个逗号
    lines[-1] = lines[-1][:-1]
    #将所有行写入到新的文件中：
    with open('训练集_output.txt', 'w', encoding='utf-8') as new_file:
        new_file.writelines(lines)
    print('训练集_output.txt文件已生成！')
