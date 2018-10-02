"""
作者:sky
功能:bmr计算
版本:3.0
日期:20181001
"""

def main():
    """
    主函数
    """

    y_or_n = input('是否退出程序（y/n）？')

    while y_or_n == 'n':
        print('请输入一下信息，用空格分割')
        input_str = input('性别 体重（kg） 身高（cm） 年龄：')
        str_list = input_str.split(' ')
        #print(type(str_list))
        try:
            gender = str_list[0]
            # print(type(gender))

            weight = float(str_list[1])
            # print(type(gender))

            height = float(str_list[2])
            # print(type(gender))

            age = int(str_list[3])

            if gender == '男':
                BMR = (13.7*weight)+(5.0*height)-(6.8*age)+66
            elif gender == '女':
                BMR = (9.6*weight)+(1.8*height)-(4.7*age)+655
            else:
                BMR = -1

            if BMR == -1:
                print('不支持此性别类型！')
            else:
                print('您的性别:{1},体重（kg）:{0}, 身高（cm）:{2}, 年龄：{3},基础代谢率:{4}大卡.'.format(weight, gender, height, age, BMR))

        except ValueError:
            print('存在输入值错误，请输入正确的信息。')
        except:
            print('程序异常，请输入正确的信息。')

        y_or_n = input('是否退出程序（y/n）？')


if __name__ == '__main__':
    main()