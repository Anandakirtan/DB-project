import telebot
import re
import psycopg2

conn = psycopg2.connect(user="postgres", dbname="Sports", password="2281488", host="localhost")
cur = conn.cursor()

while True:
    a = input("Введите запрос\n")
    if (a == "exit") :
        break;
    if (a == "?") :
        print("Введите:\n"
              "exit, чтобы завершить работу\n"
              "teams, чтобы увидеть список команд\n"
              "players, чтобы увидеть список игроков\n"
              "tournaments, чтобы увидеть список турниров\n"
              "sponsors, чтобы увидеть список спонсоров\n"
              "team *teamname*, чтобы увидеть состав *teamname*\n"
              "sponsor *sponsor*, чтобы увидеть все, что спонсирует *sponsor*\n"
              "best players, чтобы увидеть игроков, выигравших хотя бы 90% игр в хорошем порядке\n"
              "best teams, чтобы увидеть игроков, выигравших хотя бы 60% игр в хорошем порядке\n"
              "richest players, чтобы увидеть 10 игроков, выигравших больше остальных\n"
              "teams in *tournament*, чтобы увидеть все команды, участвующие в *tournament*"
              "team in tournaments *teamname*, чтобы увидеть все турниры, в которых участвует команда")
        continue
    if (a == "teams") :
        cur.execute("SELECT name FROM teams ORDER BY name")
    if (a == "players") :
        cur.execute("SELECT name FROM players ORDER BY name")
    if (a == "tournaments") :
        cur.execute("SELECT name FROM tournaments ORDER BY name")
    if (a == "sponsors") :
        cur.execute("SELECT name FROM sponsors ORDER BY name")
    if (len(a) > 3 and a[0] + a[1] + a[2] + a[3] == "team") :
        team = ""
        for i in range(5, len(a)) :
            team += a[i]
        cur.execute("SELECT players.name FROM players JOIN teams ON (players.team_id = teams.team_id) "
                    "WHERE teams.name = '{0}' ORDER BY players.name".format(team))
    # if (len(a) > 6 and a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] == "sponsor") :
    #     sponsor = ""
    #     for i in range(8, len(a)) :
    #         sponsor += a[i]
    #     cur.execute("SELECT name FROM sponsors JOIN teams JOIN tournaments JOIN players ON sponsor_id "
    #                 "WHERE sponsors.name = '{0}' ORDER BY name".format(sponsor))
    if (a == "best players") :
        cur.execute("SELECT name FROM players WHERE winrate >= 90 ORDER BY winrate DESC")
    if (a == "best teams") :
        cur.execute("SELECT name FROM teams WHERE winrate >= 60 ORDER BY winrate DESC")
    if (a == "richest players") :
        cur.execute("SELECT name, last_year_prize_money FROM players ORDER BY last_year_prize_money DESC LIMIT 10")
    if (a == "richest teams") :
        cur.execute("SELECT name, last_year_prize_money FROM teams ORDER BY last_year_prize_money DESC LIMIT 10")
    if (a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7]== "teams in") :
        tournament = ""
        for i in range(9, len(a)):
            tournament += a[i]
        cur.execute("SELECT teams.name FROM teams JOIN participations ON (teams.team_id = participations.team_id) "
                    "JOIN tournaments ON (participations.tournament_id = tournaments.tournament_id)"
                    "WHERE tournaments.name = '{0}' ORDER BY teams.name".format(tournament))
    if (a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6]== "team in") :
        team = ""
        for i in range(20, len(a)):
            team += a[i]
        cur.execute("SELECT tournaments.name FROM teams JOIN participations ON (teams.team_id = participations.team_id) "
                    "JOIN tournaments ON (participations.tournament_id = tournaments.tournament_id)"
                    "WHERE teams.name = '{0}' ORDER BY tournaments.name".format(team))
    ans = cur.fetchall()
    for row in ans:
        print(row)
