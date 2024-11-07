from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis


def clean_sequence(seq):
    return ''.join([aa for aa in seq if aa in 'ACDEFGHIKLMNPQRSTVWY'])


def calculate_gravy(sequence):
    protein_analysis = ProteinAnalysis(sequence)
    return protein_analysis.gravy()


# 读取序列文件 (假设文件名是 "my_protein_sequences.fasta")
input_file = "E:\\ZCJ\\nymdb\\Thermarum\\处理\\ntchuli_pep.fa"
output_file = "E:\\ZCJ\\nymdb\\Thermarum\\处理\\ntzhirongzhishu.csv"

with open(input_file, "r") as file, open(output_file, "w") as output:
    # 写入CSV文件的表头
    output.write("Protein ID,GRAVY Index\n")

    for record in SeqIO.parse(file, "fasta"):
        sequence = str(record.seq)
        cleaned_sequence = clean_sequence(sequence)
        gravy_index = calculate_gravy(cleaned_sequence)
        # 写入CSV文件
        output.write(f"{record.id},{gravy_index}\n")

print(f"GRAVY results have been written to {output_file}")
