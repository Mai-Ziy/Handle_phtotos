from PIL import Image, ImageEnhance
import os
a = input("请输入待转化文件路径（F://photo/01.png）:")
Input_picture_path = a

b = input("请输入转化文件存放路径（F://photo/）:")
Output_path_assitant = b

c = input("请输入生成图片名字（1.jpg/0.png）:")
Out_picture_name = c

#合并路径—打印存放路径
path_list = [Output_path_assitant,Out_picture_name]
Out_picture_path = ''
for path in path_list:
    Out_picture_path = os.path.join(Out_picture_path, path)
print(Out_picture_path)


#图片处理函数
def change4_4(Input_path,Output_path):
    ran = Image.open(Input_path)
# imageCode.load()
    sharp_img = ImageEnhance.Contrast(ran).enhance(2.0).convert('L')
    sharp_img.load()
    sharp_img.save(Output_path)

    return
change4_4(Input_picture_path,Out_picture_path)
