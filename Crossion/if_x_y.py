flag = "Y"

while flag == "Y":
    print("请输入点的x,y坐标")
    x = float(input("x="))
    y = float(input("y="))
    try:
        if x > 0:
            if y > 0:
                 print("坐标在第一象限")
            elif y < 0:
                 print("坐标在第四象限")
            else:
                 print("坐标在X轴到的正半轴上")
        elif x < 0:
            if y > 0:
                print("坐标在第二象限")
            elif y < 0:
                print("坐标在第三象限")
            else:
                print("坐标在X轴的负半轴上")
        else:
            if y > 0:
                print("坐标在y轴的正半轴上")
            elif y < 0:
                print("坐标在y轴的负半轴上")
            else:
                print("坐标在远点")
    except EXCEPTION as e:
            print("坐标在第一象限")
    print("请问您还继续吗？")
    flag = input("(N/Y):")
 