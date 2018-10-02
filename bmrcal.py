"""
作者:sky
功能:bmr计算
版本:1.0
日期:20181001
"""

def main():
    """
    主函数
    """

    y_or_n = input('是否退出程序（y/n）？')

    while y_or_n == 'n':
        gender = input('请输入性别：')
        # print(type(gender))

        weight = float(input('请输入体重（kg）：'))
        # print(type(gender))

        height = float(input('请输入身高（cm）：'))
        # print(type(gender))

        age = int(input('请输入年纪：'))
        # print(type(gender))

        if gender == '男':
            BMR = (13.7*weight)+(5.0*height)-(6.8*age)+66
        elif gender == '女':
            BMR = (9.6*weight)+(1.8*height)-(4.7*age)+655
        else:
            BMR = -1

        if BMR == -1:
            print('不支持此性别类型！')
        else:
            print('此人BMR（基础代谢率）为', BMR)

        y_or_n = input('是否退出程序（y/n）？')


if __name__ == '__main__':
    main()