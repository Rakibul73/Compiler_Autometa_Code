# Compiler and Autometa in Python 3<br/>[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) [![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://pypi.org/project/numpy/) [![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)](https://pypi.org/project/scipy/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)](https://pypi.org/project/matplotlib/) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Installations

* **Python 3** can be downloaded from [here](https://www.python.org/downloads/). Make sure to check **Add Python 3.x to PATH** during installation.
* **NumPy**, **SciPy**, and **matplotlib** **etc** libraries can be downloaded and installed using the commands:
```bash
pip install numpy
pip install scipy
pip install matplotlib
pip install library-name
```
or if you have multiple python version installed use this
```bash
py -3.9 -m pip install numpy
py -3.11 -m pip install numpy
.....
```

## Code for Academic Course CIT-412 (Compiler Design and Autometa Theory Sessional)
## `Masud Sir Lab ----------------------------`
<br/>

### Lab 01: Write a program to identify whether a given line is a comment or not.
 [Jupyter File (Identify Python Comment)](./Masud_Sir/identify_python_comment.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [Jupyter File (Identify C Comment with Regex)](./Masud_Sir/identify_c_comment_with_regex.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [Jupyter File (Identify C Comment without Regex)](./Masud_Sir/identify_c_comment_without_regex.ipynb)

<br/>

### Lab 02: Write a program to recognize strings under 'a', 'a*b+', 'abb'.
 [Jupyter File](./Masud_Sir/recognize_string_for_language.ipynb)
<br/>

### Lab 03: Write a program to test whether a given identifier is valid or not.
 [Jupyter File (With Regex)](./Masud_Sir/validate_identifier_with_regex.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [Jupyter File (Without Regex)](./Masud_Sir/validate_identifier_without_regex.ipynb)
<br/>

### Lab 04: Write a program to recognize of tokens from lexemes.
 [Jupyter File (With Regex)](./Masud_Sir/recognize_token_from_lexemes_with_regex.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [Jupyter File (Without Regex)](./Masud_Sir/recognize_token_from_lexemes_without_regex.ipynb)
<br/>

### Lab 05: Write a program to recognize blank, white space, tab, and newline.
 [Jupyter File (Rectangular Shape)](./Masud_Sir/recognize_blank_whitespace_tab_newline.ipynb) 
<br/>

### Lab 06: Write a program to simulate lexical analyzer for validating operators.
 [Jupyter File (With Regex)](./Masud_Sir/lexical_analyzer_validate_operators.ipynb)
<br/>

### Extra Lab: Write a program to simulate lexical analyzer & make tokens.
 [Jupyter File (With Regex)](./Masud_Sir/lexeical_analyzer_making_token.ipynb)
<br/>

### Lab 07: Write a program for constructing of LL (1) parsing. 
 [Jupyter File](./Masud_Sir/constructing_LL(1)_parsing.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [Jupyter File (Alternative)](./Masud_Sir/constructing_LL(1)_parsing_Alternative.ipynb)
<br/>

### Lab 09: Write a program for constructing recursive descent parsing.
 [Jupyter File (With Regex)](./Masud_Sir/recursive_descent_parsing.ipynb)
<br/>

### Extra Lab: Write a program for lexical analyzer + recursive descent parsing.
 [Jupyter File (With Regex)](./Masud_Sir/lexical_analyzer_plus_recursive_decent_parser.ipynb)
<br/>

### Lab 10: Design a Predictive Parser for the following grammar
    G: {E-> TE’, E’ -> +TE’ | 0, T-> FT’, T’-> *FT’|0, F-> (E) | id}.
 [Jupyter File (With Regex)](./Masud_Sir/predictive_parser.ipynb)
<br/>

### Lab 11: Write a program to calculate First and Follow sets of given grammar.
    G: {E-> TE’, E’ -> +TE’ | 0, T-> FT’, T’-> *FT’|0, F-> (E) | id}.
 [Jupyter File](./Masud_Sir/first_follow_sets.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [Jupyter File (Alternative)](./Masud_Sir/First_Follow_sets_Alternative.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [CPP File](./Masud_Sir/first_follow_sets.cpp)
<br/>

### Lab 12: Write a program to implement top-down parsing for a given Grammar.
    G: {E-> TE’, E’ -> +TE’ | 0, T-> FT’, T’-> *FT’|0, F-> (E) | id}.
 [Jupyter File](./Masud_Sir/top_down_parsing.ipynb)
<br/>

### Lab 13: Write a Program to implement bottom-up parsing for a given Grammar.
    G: {E-> TE’, E’ -> +TE’ | 0, T-> FT’, T’-> *FT’|0, F-> (E) | id}.
 [Jupyter File](./Masud_Sir/bottom_up_parsing.ipynb) &nbsp;&nbsp; / &nbsp;&nbsp; [CPP File](./Masud_Sir/bottom_up_parsing.cpp)
<br/>
<br/>

### Lab 14: Write a Program to construct LR (0) parser for a given augmented Grammar.
 [Jupyter File](./Masud_Sir/lr(0)_parser.ipynb)
<br/>
<br/>

### Lab 15: Write a program to construct SLR parser for a given augmented Grammar.
 [Jupyter File](./Masud_Sir/slr_parser.ipynb)
<br/>
<br/>

### Extra Lab: Write a program to detect lexemes from the input statement position = initial + rate * 60 Implement a program for detecting tokens from the input "int a = b + 10c + 7" and a token is either keyword, an identifier, a constant, a string literal, or a symbol
 [Jupyter File](./Masud_Sir/detect_lexemes_token_from_input.ipynb)
<br/>
<hr/>