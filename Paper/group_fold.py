dict = {'0':0,'1':1,'2':2,'3':3,'腺体':0,'囊肿':0,'上皮':0,'normal':0,'nang':0,'高级别':1,'癌':1,'high':1,'cancer':1}
fold_cross = 10
path = 'cut_label_list_7_23.txt'
#list[0] contains low risks cases, list[1] contains high level cases, list[2] contanis cancer cases
lists = [[] for i in range(4)]
#patient_list[0] contains low risk cases' patients, so do patient_list[1] and patient_list[2]
patient_lists = [[] for i in range(4)]

with open(path, encoding='utf-8') as f:
    line = f.readline()
    while line:
        tmp_file_path = line.split('\t')[0]
        tmp_class_name = line.split('\t')[1]
        tmp_patient_id = line.split('\t')[2].split('\n')[0]
        print(tmp_patient_id)
        lists[dict[tmp_class_name]].append(tmp_file_path)

        if tmp_patient_id not in patient_lists[dict[tmp_class_name]]:
            print('in')
            patient_lists[dict[tmp_class_name]].append(tmp_patient_id)
        line = f.readline()
f.close()


print(len(patient_lists[0]))
print(len(patient_lists[1]))
print(len(patient_lists[2]))
print(len(patient_lists[3]))

import random
for fold in range(fold_cross):
    for i in range(4):
        print(len(patient_lists[i]))
        random.shuffle(patient_lists[i])

    train_patient_lists = [[] for i in range(4)]
    test_patient_lists = [[] for i in range(4)]

    for i in range(4):
        print(patient_lists[i])
        tmp_train = patient_lists[i][:int(fold/fold_cross * len(patient_lists[i]))]+patient_lists[i][int((fold+1)/fold_cross * len(patient_lists[i])):]
        tmp_test = patient_lists[i][int(fold/fold_cross * len(patient_lists[i])):int((fold+1)/fold_cross * len(patient_lists[i]))]
        for train_item in tmp_train:
            train_patient_lists[i].append(train_item)
        for test_item in tmp_test:
            test_patient_lists[i].append(test_item)

    print(len(train_patient_lists),len(test_patient_lists))
    print(train_patient_lists)
    print(test_patient_lists)

    train_list_file = open('4train_list_0.9_'+str(fold)+'.txt','w')
    test_list_file = open('4test_list_0.1_'+str(fold)+'.txt','w')

    with open(path, encoding='utf-8') as f:
        line = f.readline()
        while line:
            tmp_file_path = line.split('\t')[0]
            tmp_class_name = line.split('\t')[1]
            tmp_patient_id = line.split('\t')[2].split('\n')[0]
            tmp_class = dict[tmp_class_name]

            if tmp_patient_id in train_patient_lists[tmp_class]:
                train_list_file.write(tmp_file_path+'\t'+str(dict[tmp_class_name])+'\n')
            elif tmp_patient_id in test_patient_lists[tmp_class]:
                test_list_file.write(tmp_file_path+'\t'+str(dict[tmp_class_name])+'\n')
            line = f.readline()
    f.close()
