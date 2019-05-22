CREATE TABLE Aliment (
    barecode SMALLINT(14) UNSIGNED ,
    name_aliment VARCHAR(150) NOT NULL,
    category SMALLINT UNSIGNED NOT NULL,
    store VARCHAR(50),
    grade CHAR(1) NOT NULL,
    description TEXT,
    link TEXT,
    substitut SMALLINT(14) UNSIGNED ,
    PRIMARY KEY (barecode),
    CONSTRAINT fk_category FOREIGN KEY(category) REFERENCES Category(id_category),
    CONSTRAINT fk_subsitut FOREIGN KEY(substitut) REFERENCES Aliment(barecode)
)
ENGINE = InnoDB;