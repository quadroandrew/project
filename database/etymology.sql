/* This is a copy of the given SQL from Berry's Sanskrit program */
-- DROP DATABASE IF EXISTS etymological;

CREATE DATABASE etymological;
ALTER DATABASE etymological CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use etymological;

-- DROP table if exists wordhistory;

CREATE TABLE wordhistory (
    WordText TEXT(65535),
    NLTKTag TEXT(65535),
    Etymological TEXT(65535)
);

INSERT INTO wordhistory
    (WordText, NLTKTag, Etymological)
VALUES
    ('.', '.', 'The full stop symbol derives from the Greek punctuation introduced by Aristophanes of Byzantium in the 3rd century bce. In practice, scribes mostly employed the terminal dot; the others fell out of use and were later replaced by other symbols. From the 9th century onwards, the full stop began appearing as a low mark (instead of a high one), and by the time printing began in Western Europe, the lower dot was regular and then universal.')
    ,('I', 'DET', 'test: bad data')
    ,('see', 'DET', 'test: bad data')
;
