# HyperMGRS
## An attempt at generating hyperplanes for key physical child growth 

### Introduction
This project is to generate some method by which one can easily classify a child's physical attributes into nutritional classes. The data used here is from [this governmental platform](https://www.poshantracker.in/PTCalculator), which itself claims to collect it from a WHO report, [The WHO **M**ulticentre **G**rowth **R**eference **S**tudy](https://www.who.int/tools/child-growth-standards/who-multicentre-growth-reference-study). The goal is to produce separating planes (or hyperplanes as the case may be) between different classifications for stunting or wasting or being underweight.

### Installation
You will need `python3` installed with `venv` as well. Install the packages in `requirements.txt` as follows:
```
python install -r requirements.txt
```

### Execution
Currently all that is supported is generating training data, please look at [this readme file](generated_data/README.md)

### TODO
- Plan this out better
- Document better
- ~~Collect and clean data provided as PDF files~~
- ~~Generate further data by simple sampling methods~~
- Attempt to generate hyperplanes via simple methods, to be listed below
- Attempt to also generate confidence scores for predictions
- Consider other kinds of problem statements, such as extrapolation
- Error handling for all files