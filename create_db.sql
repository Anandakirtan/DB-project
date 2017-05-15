CREATE TABLE tournaments (
    tournamnet_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kind_of_sport TEXT NOT NULL,
    prize_fund INTEGER,
    starts DATE,
    ends DATE,
    general_sponsor_id INTEGER REFERENCES sponsors(sponsor_id),
    country TEXT NOT NULL
);

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kind_of_sport TEXT NOT NULL,
    country TEXT NOT NULL,
    general_sponsor_id INTEGER REFERENCES sponsors(sponsor_id),
    last_year_prize_money INTEGER,
    winrate FLOAT DEFAULT(0),
    next_tournament_id INTEGER REFERENCES tournament(tournament_id)
);

CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    kind_of_sport TEXT NOT NULL,
    role TEXT,
    country TEXT NOT NULL,
    team_id INTEGER REFERENCES teams(team_id),
    last_year_prize_money INTEGER,
    winrate INTEGER DEFAULT(0),
    sponsor_id INTEGER REFERENCES sponsors(sponsor_id),
    next_game_time DATE,
    next_tournament tournament_id REFERENCES tournaments(tournament_id)
);

CREATE TABLE sponsors (
    sponsors_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);