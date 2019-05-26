import os
import os.path

basepath="C:\\Users\\Borealis\\Desktop\\NSCR\\crop_project\\additional TRAINING_ours"

for file_l1 in os.listdir(basepath):
    basepath_l1 = os.path.join(basepath,file_l1)
    for file_l2 in os.listdir(basepath_l1):
        basepath_l2=os.path.join(basepath_l1,file_l2)
        for file_l3 in os.listdir(basepath_l2):
            basepath_l3=os.path.join(basepath_l2,file_l3)
            for file_l4 in os.listdir(basepath_l3):
                basepath_l4=os.path.join(basepath_l3,file_l4)
                new_name=file_l3+ '_' + file_l4
                old_path = os.path.join(basepath_l3,file_l4)
                new_path = os.path.join(basepath_l2,new_name)
                # print("Old Path: {0} \n New Path: {1}".format(old_path,new_path))
                os.rename(old_path,new_path)
                            