CREATE TABLE User(
    user_id INT PRIMARY KEY,
    token BLOB,
    tag BLOB,
    nonce BLOB
);

INSERT INTO User(user_id, token, tag, nonce) VALUES(1,NULL,NULL,NULL);

--dummy user to test the application working