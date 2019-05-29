CREATE TABLE IF NOT EXISTS Favorite (
    name_aliment VARCHAR(150) NOT NULL,
    category SMALLINT UNSIGNED NOT NULL,
    store TEXT,
    grade TEXT NOT NULL,
    description TEXT,
    link TEXT,
    PRIMARY KEY (name_aliment),
    CONSTRAINT fk_category_favorite FOREIGN KEY(category) REFERENCES Category(id_category),
    UNIQUE INDEX (name_aliment, category,grade(1))
)
ENGINE = InnoDB