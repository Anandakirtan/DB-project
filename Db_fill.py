import psycopg2
import random

conn = psycopg2.connect(user="postgres", dbname="Sports", password="2281488", host="localhost")
cur = conn.cursor()
#cur.execute("INSERT INTO players VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});".format())

first_names = []
surnames = []
first_names.append("Sergio")
surnames.append("Aguero")
surnames.append("Busquets")
surnames.append("Ramos")
surnames.append("Santos")
first_names.append("Kevin")
surnames.append("De Bruyne")
surnames.append("Gameiro")
first_names.append("Lionel")
surnames.append("Messi")
first_names.append("Cristiano")
surnames.append("Ronaldo")
first_names.append("Manuel")
surnames.append("Neuer")
first_names.append("Roman")
surnames.append("Fominok")
first_names.append("Xu")
surnames.append("Zhilei")
first_names.append("Alexei")
surnames.append("Berezin")
first_names.append("Artem")
surnames.append("Volvich")
surnames.append("Fomin")
first_names.append("Sergey")
surnames.append("Grankin")
first_names.append("Maksim")
surnames.append("Mikhaylov")
first_names.append("Aleksey")
surnames.append("Verbov")
first_names.append("Bruno")
surnames.append("Rezende")
first_names.append("Erik")
surnames.append("Shoji")
first_names.append("Evgen")
surnames.append("Mostovik")
first_names.append("Bulat")
surnames.append("Shamsutdinov")
first_names.append("Yaroslav")
surnames.append("Chizh")
first_names.append("Anton")
surnames.append("Chekashev")
foot_names = []
for i in range(0, 300):
    foot_names.append(random.choice(first_names) + ' ' + random.choice(surnames))
volley_names = []
for i in range(0, 200):
    volley_names.append(random.choice(first_names) + ' ' + random.choice(surnames))
dota_names = []
for i in range(0, 150):
    dota_names.append(random.choice(first_names) + ' ' + random.choice(surnames))

disciplines = []
disciplines.append("Football")
disciplines.append("Volleyball")
disciplines.append("Dota 2")

foot_roles = []
foot_roles.append("Striker")
foot_roles.append("Winger")
foot_roles.append("Midfielder")
foot_roles.append("Defender")
foot_roles.append("Goalkeeper")

volley_roles = []
volley_roles.append("Setter")
volley_roles.append("Libero")
volley_roles.append("Middle blocker")
volley_roles.append("Middle hitter")
volley_roles.append("Outside hitter")

dota_roles = []
dota_roles.append("Carry")
dota_roles.append("Support")
dota_roles.append("Offlaner")
dota_roles.append("Midlaner")

country = []
country.append("Russia")
country.append("Brazil")
country.append("Belgium")
country.append("Germany")
country.append("England")
country.append("Ukraine")
country.append("France")
country.append("Spain")
country.append("Argentina")
country.append("USA")
country.append("Japan")
country.append("China")
country.append("Portugal")
country.append("Australia")
country.append("Austria")

foot_teams = []
foot_teams.append("Manchester United")
foot_teams.append("Manchester City")
foot_teams.append("Juventus")
foot_teams.append("Barcelona")
foot_teams.append("Real Madrid")
foot_teams.append("Chelsea")
foot_teams.append("Inter")
foot_teams.append("Bayern")
foot_teams.append("Milan")
foot_teams.append("Liverpool")
foot_teams.append("Tottenham")
foot_teams.append("Napoli")
foot_teams.append("Monako")
foot_teams.append("Atletico Madrid")
foot_teams.append("Spartak")
foot_teams.append("Anderlecht")
dota_teams = []
dota_teams.append("Virtus.Pro")
dota_teams.append("NaVi")
dota_teams.append("IG")
dota_teams.append("OG")
dota_teams.append("EG")
dota_teams.append("Secret")
dota_teams.append("Fnatic")
dota_teams.append("Wings")
dota_teams.append("Faceless")
dota_teams.append("Cloud9")
dota_teams.append("KBU")
volley_teams = []
volley_teams.append("Zenit Kazan")
volley_teams.append("Dinamo Moscow")
volley_teams.append("Yugra")
volley_teams.append("Paris Volley")
volley_teams.append("Trentino")
volley_teams.append("Skra")
volley_teams.append("Sada Cruzeiro")

dates = []
for i in range(0, 60):
    dates.append(str(random.randint(2017, 2022)) + '-' + str(random.randint(1,12)) + '-' + str(random.randint(1, 28)))

sponsors = []
sponsors.append("Etihad Airways")
sponsors.append("Fly Emirates")
sponsors.append("Intel")
sponsors.append("AMD")
sponsors.append("Yandex")
sponsors.append("Nvidia")
sponsors.append("Steelseries")
sponsors.append("Razor")
sponsors.append("Volzhanka")
sponsors.append("Adidas")
sponsors.append("Nike")
sponsors.append("Gazprom")
sponsors.append("Valve")
sponsors.append("EA")

tournaments = []
ran1 = []
ran1.append("International")
ran1.append("World")
ran1.append("Euro")
ran1.append("American")
ran1.append("African")
ran1.append("Asia")
ran1.append("Universe")
ran1.append("Champions")
ran2 = []
ran2.append("Cup")
ran2.append("League")
ran2.append("Championship")
ran2.append("Tournament")
for i in range(0, 30):
    tournaments.append(random.choice(ran1) + random.choice(ran2))

j = 0
for i in sponsors:
    cur.execute("""
                INSERT INTO sponsors (sponsor_id, name) VALUES({0}, '{1}');""".format(j, i))
    j += 1

j = 0
for i in tournaments:
    cur.execute("""
        INSERT INTO tournaments (tournament_id, name, kind_of_sport, prize_fund, starts, ends, general_sponsor_id,
        country) VALUES({0}, '{1}', '{2}', {3}, '{4}', '{5}', {6}, '{7}');
        """.format(
            j, i, random.choice(disciplines), random.randint(1, 1000000),
            random.choice(dates), random.choice(dates), random.randint(0, len(sponsors) - 1), random.choice(country)))
    j += 1

j = 0
for i in foot_teams:
    cur.execute("""
        INSERT INTO teams (team_id, name, kind_of_sport, country, general_sponsor_id, last_year_prize_money, winrate)
        VALUES({0}, '{1}', '{2}', '{3}', {4}, {5}, {6});
        """.format(
            j, i, "football", random.choice(country), random.randint(0, len(sponsors) - 1),
            random.randint(0, 10000000), random.randint(0, 101)))
    j += 1
for i in volley_teams:
    cur.execute("""
            INSERT INTO teams (team_id, name, kind_of_sport, country, general_sponsor_id, last_year_prize_money, winrate)
            VALUES({0}, '{1}', '{2}', '{3}', {4}, {5}, {6});
            """.format(
        j, i, "volleyball", random.choice(country), random.randint(0, len(sponsors) - 1),
        random.randint(0, 10000000), random.randint(0, 101)))
    j += 1
for i in dota_teams:
    cur.execute("""
            INSERT INTO teams (team_id, name, kind_of_sport, country, general_sponsor_id, last_year_prize_money, winrate)
            VALUES({0}, '{1}', '{2}', '{3}', {4}, {5}, {6});
            """.format(
        j, i, "dota", random.choice(country), random.randint(0, len(sponsors) - 1),
        random.randint(0, 10000000), random.randint(0, 101)))
    j += 1

j = 0
for i in foot_names:
    cur.execute("""
        INSERT INTO players (player_id, name, kind_of_sport, role, country, team_id, last_year_prize_money,
        winrate, sponsor_id, next_game_time) VALUES({0}, '{1}', '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, '{9}');
        """.format(
            j, i, "football", random.choice(foot_roles), random.choice(country),
            random.randint(0, len(foot_teams) - 1), random.randint(0, 1000000), random.randint(0, 101),
            random.randint(0, len(sponsors) - 1), random.choice(dates)))
    j += 1
for i in volley_names:
    cur.execute("""
        INSERT INTO players (player_id, name, kind_of_sport, role, country, team_id, last_year_prize_money,
        winrate, sponsor_id, next_game_time) VALUES({0}, '{1}', '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, '{9}');
        """.format(
            j, i, "volleyball", random.choice(volley_roles), random.choice(country),
            random.randint(len(foot_teams), len(foot_teams) + len(volley_teams) - 1), random.randint(0, 1000000),
            random.randint(0, 101), random.randint(0, len(sponsors) - 1), random.choice(dates)))
    j += 1
for i in dota_names:
    cur.execute("""
        INSERT INTO players (player_id, name, kind_of_sport, role, country, team_id, last_year_prize_money,
        winrate, sponsor_id, next_game_time) VALUES({0}, '{1}', '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, '{9}');
        """.format(
            j, i, "dota", random.choice(dota_roles), random.choice(country),
            random.randint(len(foot_teams) + len(volley_teams),
            len(foot_teams) + len(volley_teams) + len(dota_teams) - 1), random.randint(0, 1000000),
            random.randint(0, 101), random.randint(0, len(sponsors) - 1), random.choice(dates)))
    j += 1

for i in range(1, 1000000):
    cur.execute("""
        INSERT INTO participations (tournament_id, team_id) VALUES({0}, {1});
        """.format(random.randint(0, 20), random.randint(0, 20)))
conn.commit()
