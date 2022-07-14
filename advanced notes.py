
from msvcrt import open_osfhandle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
 
import json
 
app = QApplication([])
 
'''Application interface'''


data = {
"Note name" :
{
"text" : "Very important note text",
"tags" : ["draft", "thoughts"]
    }
}


#with open("f.json", "r") as file:
    #data = json.load(file)


#application window parameters
notes_win = QWidget()
notes_win.setWindowTitle('Advanced notes')
notes_win.resize(900, 600)
 
#application window widgets
list_notes = QListWidget()
list_notes_label = QLabel('List of notes')
 
button_note_create = QPushButton('Create note') #a window appears with the field "Enter note name"
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')
 
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Enter tag...')
field_text = QTextEdit()
button_add = QPushButton('Add to note')
button_del = QPushButton('Untag from note')
button_search = QPushButton('Search notes by tag')
list_tags = QListWidget()
list_tags_label = QLabel('List of tags')
 
#arranging widgets by layout
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
 
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)
 
col_2.addLayout(row_3)
col_2.addLayout(row_4)
 
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def update():
    global data
    list_notes.clear()
    with open('f.json', 'r') as file:
        notes= json.load(file)
    for i in data:
        list_notes.addItem(i)
def lisft():
    global data
    list_notes.clear()
    with open("f.json", "r") as file:
        data = json.load(file)
    for i in data:
        list_notes.addItem(i)
def show_note():
    lisft()
    #receiving text from the note with highlighted title and displaying it in the edit field
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(data[key]["text"])
    list_tags.clear()
    list_tags.addItems(data[key]["tags"])

def create_note():
    global data
    note_name, ok = QInputDialog.getText(notes_win,'Add note', 'Note name:')
    data[note_name] = {'text':"", 'tags':[]}
    with open("f.json", "w") as file:
        json.dump(data, file)
    lisft()
def del_note():
    if list_notes.selectedItems():
        
        key = list_notes.selectedItems()[0].text()
        del data[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(data)
        with open("f.json", "w") as file:
            json.dump(data, file)
        lisft()

def show_note():
    #receiving text from the note with highlighted title and displaying it in the edit field
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(data[key]["text"])
    list_tags.clear()
    list_tags.addItems(data[key]["tags"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        data[key]["text"] = field_text.toPlainText()
        with open("f.json", "w") as file:
            json.dump(data, file, sort_keys=True, ensure_ascii=False)
        print(data)
    else:
        print("Note to save is not selected!")


        
        
  
button_note_create.clicked.connect(create_note)
button_note_del.clicked.connect(del_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)



#show_note()
lisft()
update()
save_note()
#run the application
notes_win.show()
app.exec_()
