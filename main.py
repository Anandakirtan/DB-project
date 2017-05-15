import telebot
import re
import psycopg2

conn = psycopg2.connect(user="postgres", dbname="Sports", password="2281488", host="localhost")
cur = conn.cursor()

while input("0 - закончить, 1 - продолжить") != "0":
    a = input("Введите 1, чтобы увидеть список команд\n Введите 2, чтобы увидеть список игроков\n")
    if (a == "1") :
        cur.execute("SELECT name FROM teams")
    if (a == "2") :
        cur.execute("SELECT name FROM players")
    ans = cur.fetchall()
    for row in ans:
        print(row)
