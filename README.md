# HW_1 levenshtein distance evaluating tool
A small python script to compute levenshtein distance between nucleotide sequences.

## Getting Started

This tool allows you to align sequences and gives you the information about levenshtein distance.

### Prerequisites

You need to install python3 with numpy library to run this tool.

### Installing

To install this tool clone this repository to your PC.

```
~$ git clone https://github.com/anton-shikov/HW_1.git
```


## Running and using tool

Using this tool is sa simple as its code is. After downloading repository launch terminal and enter this repository.
Use this following to execute tool:
```
~$ python My_parser_try.py
```
Note! the following command will run programme with default sequences with corresponding output:
```
~$ ('ATG', 'CTA', 2.0)
```
For computing lvenshtein distance for your favourite sequences add flags -sq1 <first sequence> -sq2 <second secuence>.
Example:
  
```
~$ python My_parser_try.py -sq1 ATTT -sq2 ATGGG
~$ ('ATGGG', 'ATTT_', 3.0)
```
Output format: corresponding aligned sequences, separeted by coma, symbol _ reflects gaps if they are presented; the number represents levenshtein distance between sequences with equal penalties for insertions, deletions and mismatches. 

## Author

* **Anton Shikov** - *Initial work* - [anton-shikov](https://github.com/anton-shikov)


## License

This project is free and available for everyone.

## Acknowledgments

Eugene Bakin for python course.
