from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)
from random import shuffle
import sys

# define the questions and answers
questions = [
    {
        'question': 'The state language of Brazil',
        'options': ['English', 'Portuguese', 'Spanish', 'Brazilian'],
        'answer': 'Portuguese'
    },
    {
        'question': 'Which color does not appear on the American flag?',
        'options': ['Red', 'White', 'Blue', 'Green'],
        'answer': 'Green'
    },
    {
        'question': 'A traditional residence of the Yakut people',
        'options': ['Urasa', 'Yurt', 'Igloo', 'Hut'],
        'answer': 'Yurt'
    },
    {
        'question': 'When WW2 Started',
        'options': ['1940', '1939', '1821', 'No War'],
        'answer': '1939'
    },
    {
        'question': 'When The Queen Died',
        'options': ['2021', '2022', '2020', '2023'],
        'answer': '2022'
    },
    {
        'question': 'When Covid-19 started',
        'options': ['2021', '2022', '2023', '2020'],
        'answer': '2020'
    },
    {
        'question': 'When Fortnite Released',
        'options': ['2018', '2022', '2023', '2017'],
        'answer': '2017'
    },
    {
        'question': 'Is Iphone the best phone ever',
        'options': ['Samsung is', 'Idk', 'No', 'Yes'],
        'answer': 'Samsung is'
    }
]

# shuffle the questions
shuffle(questions)

# create the application and main window
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')

# create the widgets
question_label = QLabel()
option_group_box = QGroupBox("Answer options")
option_layout = QVBoxLayout()
option_button_group = QButtonGroup()
answer_button = QPushButton('Answer')
result_group_box = QGroupBox("Test result")
result_label = QLabel('Are you correct or not?')
correct_label = QLabel('The answer will be here!')

# add the options to the layout and button group
for _ in range(4):
    option_button = QRadioButton()
    option_layout.addWidget(option_button)
    option_button_group.addButton(option_button)

# add the layouts to the option group box
option_layout.addStretch(1)
option_group_box.setLayout(option_layout)

# add the widgets to the layout
main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(option_group_box)
result_layout = QVBoxLayout()
result_layout.addWidget(result_label, alignment=(Qt.AlignLeft | Qt.AlignTop))
result_layout.addWidget(correct_label, alignment=Qt.AlignHCenter, stretch=2)
result_group_box.setLayout(result_layout)
result_group_box.hide()
main_layout.addWidget(result_group_box)
main_layout.addWidget(answer_button)
main_layout.setSpacing(5)
window.setLayout(main_layout)

# initialize the current question and score
current_question = 0
score = 0


# define the functions for showing and checking the answer
def show_result():
    option_group_box.hide()
    result_group_box.show()
    answer_button.setText('Next question')


def show_question():
    option_group_box.show()
    result_group_box.hide()
    answer_button.setText('Answer')
    option_button_group.setExclusive(False)
    for button in option_button_group.buttons():
        button.setChecked(False)
    option_button_group.setExclusive(True)


def check_answer():
    global score
    global current_question
    selected_button = option_button_group.checkedButton()
    if selected_button is not None:
        selected_text = selected_button.text()
        if selected_text == questions[current_question]['answer']:
            score += 1
            show_result()
            correct_label.setText('Correct!')
            result_label.setText(
                f'You answered question {current_question + 1} correctly.'
            )
        else:
            correct_label.setText('Incorrect!')
            result_label.setText(
                f"The correct answer was: {questions[current_question]['answer']}"
            )
        current_question += 1

def next_question():
    global current_question
    if current_question < len(questions):
        # display the next question
        question_label.setText(questions[current_question]['question'])
        options = questions[current_question]['options']
        option_button_group.setExclusive(True)
        for button, option in zip(option_button_group.buttons(), options):
            button.setText(option)
            shuffle(options)
        for button, option in zip(option_button_group.buttons(), options):
            button.setText(option)
            show_question()
    else:
        # show the final score
        question_label.setText('Final score:')
        option_group_box.hide()
        result_group_box.show()
        result_label.setText('You answered {} out of {} questions correctly.'.format(score, len(questions)))
        correct_label.hide()
        answer_button.hide()


answer_button.clicked.connect(check_answer)
answer_button.clicked.connect(next_question)


next_question()


window.show()
sys.exit(app.exec_())

