/* This copy of the database exists as a backup and debugger */
DROP DATABASE IF EXISTS etymological;

CREATE DATABASE etymological;

use etymological;

DROP TABLE IF EXISTS wordhistory;

CREATE TABLE wordhistory (
    WordText VARCHAR(255),
    NLTKTag VARCHAR(255),
    Etymological VARCHAR(255)
);

INSERT INTO wordhistory
    (WordText, NLTKTag, Etymological)
VALUES
    ('I', 'PRP', 'German')
    ,('see', 'VBP', 'German')
    ,('it', 'PRP', 'German')
    ,('I', 'DET', 'French')
    ,('see', 'DET', 'French')
;