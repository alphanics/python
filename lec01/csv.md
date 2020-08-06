# CSV

* CSV : Comma Separated Values
* CSV : Plain Text

```csv
column1,column2,column3,column4
data11,data12,data13,data14
data21,data22,data23,data24
data31,data32,data33,data34
data41,data42,data43,data44
```

## csv 파일 읽기
```python
import csv
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
``` 
   
```python
import csv
with open('data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for col in reader:
        print(col[0], " : ",col[1], " : ", col[2], " : ", col[3])        
```        

```python
import csv
with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for line in reader:
        print(line["column1"], line["column2"],line["column3"],line["column4"])                
```



## CSV 쓰기
```python
import csv
data = [['column1','column2'],['data11','data12'],['data21','data22']]
csv_file = open('data1.csv', 'w')
with csv_file:
   writer = csv.writer(csv_file)
   writer.writerows(data)
   print("Done")
```   

