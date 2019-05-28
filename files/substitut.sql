CREATE TABLE IF NOT EXISTS substitut (
    id_aliment SMALLINT AUTO_INCREMENT NOT NULL,
    category SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id_aliment),
    CONSTRAINT fk_substit_cat FOREIGN KEY(category) REFERENCES Category(id_category),
    UNIQUE INDEX (category)
)
Engine = InnoDB;