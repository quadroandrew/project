/* This is a copy of the given SQL from Berry's Sanskrit program */
DROP DATABASE IF EXISTS etymological;

CREATE DATABASE etymological;
-- ALTER DATABASE etymological CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use etymological;

DROP table if exists wordhistory;

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