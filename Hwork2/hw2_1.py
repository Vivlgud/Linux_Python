"""
Задание 1.
Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
"""

from checkers import checkout

folder_out = "/home/user/out"
folder_ext = "/home/user/folder1"

def test_step1():
    res1 = checkout("cd {};7z x arx2.7z".format(folder_out,folder_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext), "test")
    assert res1, "test1 FAIL"

def test_step2():
    assert (checkout("cd {};7z l arx2.7z".format(folder_out), "test")), "test2 FAIL"