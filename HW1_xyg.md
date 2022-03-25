___作业1___  
___姓名：许芸阁___  
___学号：2019012302___  
___组别：第4组___  
## <font color=008B8B>第1题：</font>
__<font color=008B8B>解释1.gtf文件中第4、5列代表什么，exon长度应该是$5-$4+1还是$5-$4？</font>__

- 第4列“start”代表该序列起始位置的坐标，第5列“end”代表该序列终止位置的坐标，均为从1开始、闭区间。

- exon长度是$5-$4+1，因为$5是序列终止位置的坐标，$4是序列起始位置的坐标，exon的长度是闭区间[$4, $5]的长度，即$5-$4+1。

## <font color=008B8B>第2题：</font>
__<font color=008B8B>列出1.gtf文件中XI号染色体上的后10个CDS（按照每个CDS终止位置的基因组坐标进行sort）。</font>__
- 命令：
 
```j
cat 1.gtf | awk '$1 =="XI" && $3 =="CDS"' | sort -k 5 -n | tail
```


- 结果：
```
 XI ensembl CDS 631152 632798 . + 0 gene_id "YKR097W"; gene_version "1"; transcript_id "YKR097W"; transcript_version "1"; exon_number "1"; gene_name "PCK1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "PCK1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR097W"; protein_version "1";   
 XI ensembl CDS 633029 635179 . - 0 gene_id "YKR098C"; gene_version "1"; transcript_id "YKR098C"; transcript_version "1"; exon_number "1"; gene_name "UBP11"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "UBP11"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR098C"; protein_version "1"; 
 XI ensembl CDS 635851 638283 . + 0 gene_id "YKR099W"; gene_version "1"; transcript_id "YKR099W"; transcript_version "1"; exon_number "1"; gene_name "BAS1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "BAS1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR099W"; protein_version "1";   
 XI ensembl CDS 638904 639968 . - 0 gene_id "YKR100C"; gene_version "1"; transcript_id "YKR100C"; transcript_version "1"; exon_number "1"; gene_name "SKG1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SKG1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR100C"; protein_version "1";   
 XI ensembl CDS 640540 642501 . + 0 gene_id "YKR101W"; gene_version "1"; transcript_id "YKR101W"; transcript_version "1"; exon_number "1"; gene_name "SIR1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SIR1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR101W"; protein_version "1";   
 XI ensembl CDS 646356 649862 . + 0 gene_id "YKR102W"; gene_version "1"; transcript_id "YKR102W"; transcript_version "1"; exon_number "1"; gene_name "FLO10"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "FLO10"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR102W"; protein_version "1"; 
 XI ensembl CDS 653080 656733 . + 0 gene_id "YKR103W"; gene_version "1"; transcript_id "YKR103W"; transcript_version "1"; exon_number "1"; gene_name "NFT1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "NFT1"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR103W"; protein_version "1";   
 XI ensembl CDS 656836 657753 . + 0 gene_id "YKR104W"; gene_version "1"; transcript_id "YKR104W"; transcript_version "1"; exon_number "1"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "YKR104W"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR104W"; protein_version "1";                  
 XI ensembl CDS 658719 660464 . - 0 gene_id "YKR105C"; gene_version "1"; transcript_id "YKR105C"; transcript_version "1"; exon_number "1"; gene_name "VBA5"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "VBA5"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR105C"; protein_version "1";   
 XI ensembl CDS 661442 663286 . + 0 gene_id "YKR106W"; gene_version "1"; transcript_id "YKR106W"; transcript_version "1"; exon_number "1"; gene_name "GEX2"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "GEX2"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "YKR106W"; protein_version "1";   
```
*～完整的结果见[这里](https://github.com/Xuyunge/hw_xyg/blob/master/HW1_xyg.md)～*
## <font color=008B8B>第3题：</font>
__<font color=008B8B>统计1.gtf文件中IV号染色体上各类feature（1.gtf文件的第3列，有些注释文件中还应同时考虑第2列）的数目，并按升序排列。</font>__
- 命令：
```j
cat 1.gtf | grep -v '^#' | awk '$1 =="IV" ' | cut -f 3 | sort | uniq -c | sort -n
```
- 结果：
```
853 start_codon
853 stop_codon
886 gene
886 transcript
895 CDS
933 exon
```






