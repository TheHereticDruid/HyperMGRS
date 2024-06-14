### Generating Data
File here, `ranged_sampling_generation.py`, is intended to generate two sets of files given an input data file. Given that there are very few variations for input here, exception handling is minimal. 

In general the format to run the file is as follows:
```
python ranged_sampling_generation.py --input_file <Relative path to the input file>
```

If one wants to provide the file called `WastedAssessmentParametersCleaned.csv` in the directory `initial_data`, one can use the following command:
```
python ranged_sampling_generation.py --input_file ../initial_data/WastedAssessmentParametersCleaned.csv
```

The command will generate two files in the current directory, one ending with `-Generated`, which generates currently 10 samples per data sample, and one ending with `-Shuffled`, which is the same file, but shuffled for training.