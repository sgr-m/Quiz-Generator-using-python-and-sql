use quiz;
CREATE TABLE quiz_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    participant_name VARCHAR(255) NOT NULL,
    score INT NOT NULL
);
