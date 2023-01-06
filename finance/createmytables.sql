#cat createmytables.sql | sqlite3 kraken.db

CREATE TABLE IF NOT EXISTS "users"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    "username" TEXT NOT NULL, 
    "hash" TEXT NOT NULL, 
    "type" TEXT NOT NULL DEFAULT "viewer");

CREATE UNIQUE INDEX IF NOT EXISTS "username" ON "users"("username");

CREATE TABLE IF NOT EXISTS "actif_games"(
    "game_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    "user_id" TEXT NOT NULL, 
    "game_code" TEXT NOT NULL,
    "date" TEXT NOT NULL, 
    "master" BOOLEAN NOT NULL, 
    "actif_question" INTEGER NOT NULL, 
    "question_time_stamp" TEXT NOT NULL,
    "time_for_each_question" NOT NULL,
    "subject" TEXT NOT NULL,
    "number_of_questions" NOT NULL, );

CREATE TABLE IF NOT EXISTS "actif_players"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    "user_id" TEXT NOT NULL,
    "game_id" INTEGER NOT NULL, 
    "score" INTEGER NOT NULL,
    "progress" INTEGER NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "users" ("id"),
    FOREIGN KEY ("game_id") REFERENCES "actif_games" ("game_id"));