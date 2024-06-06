from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QVBoxLayout, QWidget, QRadioButton

def register():
    name = name_lineedit.text()
    phone = phone_lineedit.text()
    gender = "Мужской" if male_radio.isChecked() else "Женский"
    birthdate = birthdate_dateedit.date().toString("yyyy-MM-dd")
    passport_data = passport_lineedit.text()
    email = email_lineedit.text()

    # Проверка введенных данных (можно добавить более строгие проверки)
    if not name or not phone or not birthdate or not passport_data or not email:
        QMessageBox.warning(window, "Ошибка", "Заполните все поля.")
        return
    QMessageBox.information(window, "Регистрация", "Вы успешно зарегистрированы!")

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Регистрация")

# Создание виджетов
name_label = QLabel("ФИО:")
name_lineedit = QLineEdit()

phone_label = QLabel("Номер телефона:")
phone_lineedit = QLineEdit()
gender_label = QLabel("Пол:")
male_radio = QRadioButton("Мужской")
female_radio = QRadioButton("Женский")

birthdate_label = QLabel("Дата рождения:")
birthdate_dateedit = QDateEdit()

passport_label = QLabel("Паспортные данные:")
passport_lineedit = QLineEdit()

email_label = QLabel("E-mail:")
email_lineedit = QLineEdit()

register_button = QPushButton("Зарегистрироваться")
register_button.clicked.connect(register)

# Размещение виджетов на форме
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_lineedit)
layout.addWidget(phone_label)
layout.addWidget(phone_lineedit)
layout.addWidget(gender_label)
layout.addWidget(male_radio)
layout.addWidget(female_radio)
layout.addWidget(birthdate_label)
layout.addWidget(birthdate_dateedit)
layout.addWidget(passport_label)
layout.addWidget(passport_lineedit)
layout.addWidget(email_label)
layout.addWidget(email_lineedit)
layout.addWidget(register_button)

central_widget = QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
app.exec_()