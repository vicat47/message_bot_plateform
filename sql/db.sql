CREATE TABLE IF NOT EXISTS bots
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(7),
    type INT(1) NOT NULL,
    token TEXT(64) NOT NULL,
    chat_id TEXT(32),
    secret TEXT(67)
);
