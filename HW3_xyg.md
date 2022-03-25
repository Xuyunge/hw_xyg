___作业3___  
___姓名：许芸阁___  
___学号：2019012302___  
___组别：第4组___  

## <font color=violetred>bash脚本</font>

```j
#!/bin/bash

path="/Users/xyg/bash_homework"
REQ_DIR=`ls "$path"`

for val in $REQ_DIR
do
if [ -f "${path}/${val}" ];then
echo "$val" >> ./filename.txt
elif [ -d "${path}/${val}" ];then
echo "$val" >> ./dirname.txt
else  # 补充
echo "error: $val"
fi
done

exit 0
```
_<font color=violetred>注：生成的filename.txt和dirname.txt在当前目录(./)下。</font>_

## <font color=violetblu>filename.txt</font>

a.txt
a1.txt
b.filter_random.pl
b1.txt
bam_wig.sh
c.txt
c1.txt
chrom.size
d1.txt
dir.txt
e1.txt
f1.txt
human_geneExp.txt
if.sh
image
insitiue.txt
mouse_geneExp.txt
name.txt
number.sh
out.bw
random.sh
read.sh
test.sh
test.txt
test3.sh
test4.sh
wigToBigWig

## <font color=violetblu>dirname.txt</font>

RBP_map
a-docker
app
backup
bin
biosoft
c1-RBPanno
datatable
db
download
e-annotation
exRNA
genome
git
highcharts
home
hub29
ibme
l-lwl
map2
mljs
module
mogproject
node_modules
perl5
postar.docker
postar2
postar_app
rout
script
script_backup
software
tcga
test
tmp
tmp_script
var
x-rbp
