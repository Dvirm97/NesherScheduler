CREATE TABLE nesher.soldiers (
    id text NOT NULL,
    points bigint DEFAULT 0,
    type_preference text,
    hour_preference text
);

ALTER TABLE ONLY nesher.soldiers
    ADD CONSTRAINT soldiers_pkey PRIMARY KEY (id);


--

