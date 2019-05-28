CREATE TABLE substitut (
    id_aliment SMALLINT AUTO_INCREMENT NOT NULL,
    name_aliment VARCHAR(150) NOT NULL,
    category SMALLINT UNSIGNED NOT NULL,
    store TEXT,
    grade TEXT NOT NULL,
    link TEXT,
    description TEXT,
    PRIMARY KEY (id_aliment),
    CONSTRAINT fk_category FOREIGN KEY(category) REFERENCES Aliment(category),
    UNIQUE INDEX (name_aliment, category,grade(1))
)