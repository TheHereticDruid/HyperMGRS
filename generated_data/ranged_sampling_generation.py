import argparse
import numpy as np
import subprocess

parser = argparse.ArgumentParser(description='Generate training data via sampling of a uniform distribution of expected values')
parser.add_argument('--input_file', help='Input file to generate data for')

args = parser.parse_args()

data = []

with open(args.input_file) as fp:
    for line in fp:
        sample = line.split(",")
        if len(sample) == 4:
            br = float(sample[3]) - float(sample[2])
            lb = float(sample[2]) - br
            ub = float(sample[3]) + br
            sample_values = np.random.uniform(lb, ub, 10)
            for sv in sample_values:
                if sv <= float(sample[2]):
                    label = 0
                elif sv <= float(sample[3]):
                    label = 1
                else:
                    label = 2
                data.append(sample[0:2]+[str(sv), str(label)])
        elif len(sample) == 7:
            br = (float(sample[6]) - float(sample[3])) / 3.0
            lb = float(sample[3]) - br
            ub = float(sample[6]) + br
            sample_values = np.random.uniform(lb, ub, 10)
            for sv in sample_values:
                if sv <= float(sample[3]):
                    label = 0
                elif sv <= float(sample[4]):
                    label = 1
                elif sv <= float(sample[5]):
                    label = 2
                elif sv <= float(sample[6]):
                    label = 3
                else:
                    label = 4
                data.append(sample[0:3]+[str(sv), str(label)])

with open(args.input_file.split("/")[-1].split(".")[0]+"Generated.csv", "w") as fp:
    for d in data:
        fp.write(",".join(d)+"\n")

subprocess.run(["shuf", "--output="+args.input_file.split("/")[-1].split(".")[0]+"Shuffled.csv", args.input_file.split("/")[-1].split(".")[0]+"Generated.csv"])