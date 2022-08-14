/* This is a copy of the given SQL from Berry's Sanskrit program */

CREATE DATABASE etymological;
ALTER DATABASE etymological CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use etymological;

CREATE TABLE wordhistory (
    index int,
    WordText varchar(255),
    NLTKTag varchar(255),
    Etymological varchar(255)
);

INSERT INTO wordhistory
    (index, WordText, NLTKTag, Etymological)
VALUES
    (1, "I", "PRP", "German"),
    (2, "see", "VBP", "German"),
    (3, "it", "PRP", "German"),
    (4, "I", "DET", "French"),
    (5, "see", "DET", "French")
;