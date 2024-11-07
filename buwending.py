from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import csv

# 输入文件名和输出文件名
input_file = "E:\\ZCJ\\nymdb\\Thermarum\\处理\\ntchuli_pep.fa"
output_file = "E:\\ZCJ\\nymdb\\Thermarum\\处理\\ntbuwending.csv"

# 读取蛋白质序列
sequences = list(SeqIO.parse(input_file, "fasta"))
 
# 创建一个列表来保存计算结果
results = []

# 逐一计算每个序列的不稳定系数
for seq_record in sequences:
    seq = str(seq_record.seq)  # 将序列转换为字符串
    protein_analysis = ProteinAnalysis(seq)
    instability_index = protein_analysis.instability_index()
    results.append([seq_record.id, instability_index])

# 将结果写入CSV文件
with open(output_file, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Protein ID", "Instability Index"])
    csvwriter.writerows(results)

print("批量计算完成，结果已保存到", output_file)
