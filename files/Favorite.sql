CREATE TABLE IF NOT EXISTS Favorite (
    name_aliment VARCHAR(150) NOT NULL,
    substitut_of VARCHAR(150) NOT NULL,
    store TEXT,
    grade TEXT NOT NULL,
    description TEXT,
    link TEXT,
    PRIMARY KEY (name_aliment),
    CONSTRAINT fk_aliment FOREIGN KEY(substitut_of) REFERENCES aliment(name_aliment) ON UPDATE CASCADE
,
    UNIQUE INDEX (name_aliment, substitut_of)
)
ENGINE = InnoDB;