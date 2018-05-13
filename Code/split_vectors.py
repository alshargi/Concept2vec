# -*- coding: utf-8 -*-


'''
first  200 = Dpidia     Glove
second 300 = Wikipedia  Glove(sum)
third  300 = Wikipedia  Glove(avg)

'''

all_data = []
file1 = open('task2/Settlement-Glove_DBpediaw200.csv',"w") 
file2 = open('task2/Settlement-GloveSUMw300.csv',"w") 
file3 = open('task2/Settlement-GloveAVGw300.csv',"w") 

with open('task2/Settlement_ok.csv.txt') as f:
    for line in f:
        b = line.split('\t')
        file1.writelines("{}\t{}\n".format(b[0],b[1]))  
        file2.writelines("{}\t{}\n".format(b[0],b[2]))    
        file3.writelines("{}\t{}".format(b[0],b[3]))    

 
file1.close() 
file2.close() 
file3.close() 
