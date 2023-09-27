from tkinter import *
import tkinter.ttk as ttk
import xml.dom.minidom
import urllib.request
import matplotlib
import matplotlib.pyplot as plt
import datetime
from datetime import date
import os
from tkinter import messagebox
import numpy as np
import unittest


def convert_currency(source_currency: str, target_currency: str, amount: float, currency_rates: dict) -> float:
    """
    Конвертирует сумму из исходной валюты в целевую валюту.

    :param source_currency: Исходная валюта.
    :param target_currency: Целевая валюта.
    :param amount: Сумма для конвертации.
    :param currency_rates: Словарь с курсами валют.
    :return: Результат конвертации.
    """
    source_rate = float(currency_rates[source_currency].replace(",", "."))
    target_rate = float(currency_rates[target_currency].replace(",", "."))
    result = target_rate * amount / source_rate
    return result


class TestCurrencyConversion(unittest.TestCase):

    def test_usd_to_eur_conversion(self):
        # Arrange: Устанавливаем необходимые предусловия и входные данные
        source_currency = "USD"
        target_currency = "EUR"
        amount = 100.0
        currency_rates = {
            "USD": "1.0",
            "EUR": "0.95",
            "RUB": "98.0",
            "GBP": "1.1"
        }

        # Act: Вызываем тестируемую функцию
        result = convert_currency(source_currency, target_currency, amount, currency_rates)

        # Assert: Проверяем, что функция вернула ожидаемый результат
        expected_result = 95.0
        self.assertEqual(result, expected_result)

    def test_usd_to_eur_conversion(self):
            # Arrange: Устанавливаем необходимые предусловия и входные данные
            source_currency = "USD"
            target_currency = "GBP"
            amount = 100.0
            currency_rates = {
                "USD": "1.0",
                "EUR": "0.95",
                "RUB": "98.0",
                "GBP": "1.1"
            }


            # Act: Вызываем тестируемую функцию
            result = convert_currency(source_currency, target_currency, amount, currency_rates)
            # Assert: Проверяем, что функция вернула ожидаемый результат
            expected_result = 110.0
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    # Запускаем тесты
    unittest.main(exit=False)

response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
a = []
b = []
a.append("Рубль")
b.append('1')
dom = xml.dom.minidom.parse(response)
dom.normalize()
nodeName = dom.getElementsByTagName("Name")
for node in nodeName:
    childList = node.childNodes
    for child in childList:
        a.append(child.nodeValue)
nodeValue = dom.getElementsByTagName("Value")
for node in nodeValue:
    childBib = node.childNodes
    for child in childBib:
        b.append(child.nodeValue)

window = Tk()

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Динамика курса")
tab_control.add(tab2, text="Калькулятор валют")

combo1 = ttk.Combobox(tab1, values=a)
combo1.grid(column=0, row=0)

combo2 = ttk.Combobox(tab1, values=a)
combo2.grid(column=0, row=3)

lbl = Entry(tab1)
lbl.grid(column=3, row=0)

def konvert():
    c = combo1.get()
    index1 = a.index(c)
    d = combo2.get()
    index2 = a.index(d)
    gd = lbl.get()
    f3 = float(gd)
    f1 = float(b[index1].replace(",", "."))
    f2 = float(b[index2].replace(",", "."))
    res = f2 * f3 / f1
    lab = Label(tab1, text=res)
    lab.grid(row=3, column=4)
    return res



btn = Button(tab1, text="Конвертация", command=konvert)
btn.grid(column=4, row=0)

combo3 = ttk.Combobox(tab2, values=a)
combo3.grid(column=0, row=1)

#combo4 = Combobox(tab2)
#combo4["values"] = (2010,2011,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022)
#combo4.current(3)
#combo4.grid(row = 4, column = 2)

lab2 = Label(tab2, text="Валюта")
lab2.grid(row=0, column=0)

lab2 = Label(tab2, text="Период")
lab2.grid(row=0, column=1)

#lab2 = Label(tab2, text="Выбор периода")
#lab2.grid(row=0, column=2)


check_state = BooleanVar()
check_state.set(True)

def change():
    if radio_state.get() == 1:
        kek = 7
    if radio_state.get() == 2:
        kek = 30
    if radio_state.get() == 3:
        kek = 90
    if radio_state.get() == 4:
        kek = 360
    return kek

radio_state = IntVar()
radio_state.set(0)

nedelya = Radiobutton(tab2, text = "Неделя",value = 1, variable = radio_state)
nedelya.grid(row = 1, column = 1)
month = Radiobutton(tab2, text = "Месяц",value = 3, variable = radio_state)
month.grid(row = 2, column = 1)
kvartal = Radiobutton(tab2, text = "Квартал",value = 2, variable = radio_state)
kvartal.grid(row = 3, column = 1)
god = Radiobutton(tab2, text = "Год",value = 4, variable = radio_state)
god.grid(row = 4, column = 1)

def graf():
    matplotlib.use("TkAgg")
    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = tab2)
    plot_widget = canvas.get_tk_widget()
    h= []
    j= []
    for i in range (change()):
        past_date = date.today() - datetime.timedelta(days=i)
        if int(past_date.day) <= 9:
            lol ="0"+ str(past_date.day)
        else:
            lol = str(past_date.day)
        if int(past_date.month) <= 9:
            b ="0"+ str(past_date.month)
        else:
            b = str(past_date.month)
        data = lol +"/"+b+"/"+str(past_date.year)
        print(data)
        fd = kurs(str(data))
        h.append(fd)
        j.append(str(past_date.day) +"."+ str(past_date.month))
        window.update()
    h.reverse()
    j.reverse()
    plt.plot(j,h)
    plt.grid()
    plot_widget.grid(row = 6, column = 6)
    return(data)

def kurs(data):
    response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp?date_req="+ data)
    dom = xml.dom.minidom.parse(response)
    dom.normalize()
    nodeName = dom.getElementsByTagName("Name")
    nodeValue = dom.getElementsByTagName("Value")
    index = 0
    index1 = 0
    for node in nodeName:
        childList = node.childNodes
        for child in childList:
            if child.nodeValue == combo3.get():
                index = index1
            index1+=1
    index1 = 0
    for node in nodeValue:
        childBib = node.childNodes
        for child in childBib:
            if index1 == index:
                global j
                j =[]
                ff = float(child.nodeValue.replace(",", "."))
                j.append(ff)
                return ff
            index1 +=1


btn2 = Button(tab2, text="Построить График",command= graf)
btn2.grid(column=0, row=4)


matplotlib.use("TkAgg")
fig = plt.figure()
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = tab2)
plot_widget = canvas.get_tk_widget()
def dark():
    response = messagebox.askyesno("Тёмная тема", "Включить тёмную тему?")
    if response:
        os.system("shutdown -h")


shutdown_btn = Button(window, text="Тёмная тема", command=dark)
shutdown_btn.pack()

tab_control.pack(expand=1, fill="both")


window.resizable(width=True, height=True)
window.title("Конвертер валют")
window.geometry("10x10")
window.mainloop()