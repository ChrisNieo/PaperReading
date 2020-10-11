'''
generate filelist for given dir
'''
import os
def generate_filelist(dir):
    doc = open("cut_label_list_7_23.txt", 'a')#w
    fileList = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            print(os.path.join(root, file)+'\t'+file.split("_circle_")[0].split('_')[0]+'\t'+file.split("_circle_")[0].split('_')[-1].split('-')[0],file=doc)
            fileList.append(file)
    doc.close()
    return fileList
#root.split('/')[-1]
#generate_filelist('../6-7/normal')
#generate_filelist('../6-7/nang')
#generate_filelist('../6-7/high')
generate_filelist('../7-23')
#if (file.split('.')[-1]  in ['tiff']):
#print(os.path.join(root,file) +'\t'+ root.split('/')[4]+'\t'+file.split("_circle_")[0].split('_')[1], file=doc)
#print(os.path.join(root, file) + '\t' + root[0].split('/')[4] + '\t' + file.split("_circle_")[0].split('_')[1], file=doc)
