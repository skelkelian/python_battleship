create table if not exists constants (
  name            VARCHAR(64) NOT NULL,
  value           INT
);

INSERT INTO constants VALUES('computer_opponent', 1);

INSERT INTO constants VALUES
('player_opponent', 2),
('easy_difficulty', 1),
('normal_difficulty', 2),
('god_difficulty', 3),
('carrier', 5),
('cruiser', 4),
('destroyer', 3),
('patrol_boat', 2),
('submarine', 1);

INSERT INTO constants VALUES
('horizontal_axis', 1),
('vertical_axis', 2);

SELECT * FROM constants;