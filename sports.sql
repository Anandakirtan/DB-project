CREATE TABLE tournaments (
    name TEXT NOT NULL,
    kind_of_sport TEXT NOT NULL,
    prize_fund INTEGER,
    starts DATE,
    ends DATE,
    organized_by TEXT,
    general_ponsor TEXT,
    country TEXT NOT NULL
);

CREATE TABLE teams (
    name TEXT NOT NULL,
    kind_of_sport TEXT NOT NULL,
    country TEXT NOT NULL,
    manager TEXT,
    owner TEXT,
    general_sponsor TEXT,
    players_number INTEGER,
    budget INTEGER,
    last_year_prize_money INTEGER,
    market_price INTEGER, 
    captain TEXT,
    winrate FLOAT DEFAULT(0),
    next_game_time DATE,
    next_tournament DATE
);

CREATE TABLE players (
    name TEXT NOT NULL,
    kind_of_sport TEXT NOT NULL,
    role TEXT NOT NULL,
    country TEXT NOT NULL,
    team TEXT,
    last_year_prize_money INTEGER,
    age INTEGER,
    winrate FLOAT DEFAULT(0),
    contract INTEGER,
    salary INTEGER,
    next_game_time DATE
);