-- delete the table if it exists
DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS shootouts;


CREATE TABLE results (
    date            varchar(128),
    home_team       varchar(128),
    away_team       varchar(128),
    home_score      int,
    away_score      int,
    tournament      varchar(128),
    city            varchar(128),
    country         varchar(128),
    neutral         varchar(128)
);


CREATE TABLE shootouts (
    date            varchar(128),
    home_team       varchar(128),
    away_team       varchar(128),
    winner          varchar(128)
);

-- load table

\copy results FROM 'results.csv' DELIMITER ',' CSV HEADER;
\copy shootouts FROM 'shootouts.csv' DELIMITER ',' CSV HEADER;
