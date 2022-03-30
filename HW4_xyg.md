___作业4___  
___姓名：许芸阁___  
___学号：2019012302___  
___组别：第4组___  
## 
```bash
# 加载镜像，前往文件所在目录
docker exec -it bioinfo_tsinghua bash
cd /home/test/mapping/

# Mapping
bowtie -v 2 -m 10 --best --strata BowtieIndex/YeastGenome -f THA2.fa -S THA2.sam
bowtie -v 1 -m 10 --best --strata bowtie-src/indexes/e_coli -q e_coli_500.fq -S e_coli_500.sam

# .sam转.bed
perl sam2bed.pl THA2.sam > THA2.bed
perl sam2bed.pl e_coli_500.sam > e_coli_500.bed

# 按条件筛选
grep -v chrV THA2.bed > THA2_without_chrV.bed
grep $'chrXII\t' THA2.bed > THA2_chrXII.bed

# 得到上一步中输出的两个文件的长度
wc -l THA2_without_chrV.bed    # 915行
wc -l THA2_chrXII.bed   # 169行
```
