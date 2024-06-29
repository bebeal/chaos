import re
import random

input_file = 'Dictionaries.py'

out_f = open('testoutput.txt', 'w+')
in_f = open(input_file, 'r')

option = lambda section_num, question_num, answer_option, answer: '''    <div class="inputGroup">
        <input type="radio" id="A''' + str(section_num) + '_' + str(question_num) + '_' + str(answer_option) + '" name="Q' + str(section_num) + '_' + str(question_num) + '''">
        <label for="A''' + str(section_num) + '_' + str(question_num) + '_' + str(answer_option) + '">{{< highlight python >}}' + answer + '''{{< / highlight >}}</label>
    </div>\n'''

# seems okay https://stackoverflow.com/questions/9889635/regular-expression-to-return-all-characters-between-two-special-characters
pat = r'(?<=@).+?(?=@)'

# just made it up, prob better ways but this was easy enough
'''
Comment Tagging Format
#@ @SECTION NUMBER@ @QUESTION NUMBER@ @CORRECT ANSWER@ @ANSWER CHOICE 1@ @ANSWER CHOICE 2@ ...
'''

# skip to the first question avoiding imports and misc code
line = in_f.readline()
while line and not line.startswith('#@'):
    line = in_f.readline()

# loop until the last question
while line and line.startswith('#@'):
    # parse comment tag
    result = [x for x in re.findall(pat, line[2:]) if x != ' ']
    section_num = result[0]
    question_num = result[1]
    correct_answer = result[2]
    answer_choices = [i for i in result[2:]]
    random.shuffle(answer_choices)
    answer_index = answer_choices.index(correct_answer)

    # read code and write w markdown
    out_f.write('<div>\n' + str(question_num) + '. What is output by the following code\n</div>\n\n```python\n')
    line = in_f.readline()
    while line and not line.startswith('#@'):
        line = line.rstrip()
        if len(line) != 0:
            out_f.write(line + '\n')
        line = in_f.readline()
    out_f.write('```\n\n')

    # write out html/js stuff to a new file
    out_f.write('<div class=question>\n')
    for i in range(len(answer_choices)):
        out_f.write(option(section_num, question_num, i, answer_choices[i]))
    out_f.write('<br>\n<button id="submit' + str(section_num) + '_' + str(question_num) + '" onclick="submitAnswer(\''+ str(section_num) + '_' + str(question_num) + '\', ' + str(answer_index) + ')">submit</button>\n<div id="result' + str(section_num) + '_' + str(question_num) + '" style="display:inline;"></div>\n</div><br>\n\n')