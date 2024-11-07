from Bio import SeqIO
from Bio.SeqUtils import IsoelectricPoint as IP
import csv

# 输入文件名和输出文件名
input_file = "E:\\ZCJ\\nymdb\\Thermarum\\处理\\ntchuli_pep.fa"
output_file = "E:\\ZCJ\\nymdb\\Thermarum\\处理\\ntdengdiandian.txt"

# 读取蛋白质序列
sequences = list(SeqIO.parse(input_file, "fasta"))

# 创建一个列表来保存计算结果
results = []

# 逐一计算每个序列的等电点
for seq_record in sequences:
    seq = seq_record.seq
    protein_analysis = IP.IsoelectricPoint(seq)
    pI = protein_analysis.pi()
    results.append([seq_record.id, pI])

# 将结果写入CSV文件
with open(output_file, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Protein ID", "Isoelectric Point"])
    csvwriter.writerows(results)

print("批量计算完成，结果已保存到", output_file)
