CREATE TABLE IF NOT EXISTS aliment (
    id_aliment SMALLINT AUTO_INCREMENT NOT NULL,
    name_aliment VARCHAR(150) NOT NULL,
    substitut_of VARCHAR(150),
    category SMALLINT UNSIGNED NOT NULL,
    store TEXT,
    grade TEXT NOT NULL,
    description TEXT,
    link TEXT,
    favorite TINYINT,
    PRIMARY KEY (id_aliment),
    CONSTRAINT fk_category FOREIGN KEY(category) REFERENCES Category(id_category),
    UNIQUE INDEX (name_aliment)
)
ENGINE = InnoDB;