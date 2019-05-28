CREATE TABLE substitut (
    id_aliment SMALLINT AUTO_INCREMENT NOT NULL,
    name_aliment VARCHAR(150) NOT NULL,
    category SMALLINT UNSIGNED NOT NULL,
    store TEXT,
    grade TEXT NOT NULL,
    description TEXT,
    link TEXT,
    PRIMARY KEY (id_aliment),
    CONSTRAINT fk_substit_cat FOREIGN KEY(category) REFERENCES Aliment(category),
    UNIQUE INDEX (category)
)
Engine = InnoDB;