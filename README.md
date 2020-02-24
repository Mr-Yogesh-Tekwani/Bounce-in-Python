# BallFall
Game

A ball will be moving back and forth and there will be slots below with different scores, when one presses on spacebar, ball will fall in one of the slot and that will be the score for that particular level, there are three such levels, where in each level the speed of the ball increases. At the end, sum of all three levels is shown as the score. 
After playing once, one can select to replay or to end the game.
All the scores of all the players will be shown. One can clear the data which will truncate the table.

To run the project:
pip install pygame
pip install pymysql

It is a game developed in python using pygame module and backend as mysql database,thus, to run project mysql a user named 'system' with password as 'abc123' is to be created in MySQL. Also, a table is to be created by running below query:
CREATE TABLE world.ball_fall_players(player_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, player_name VARCHAR(20), maximum_score INT,current_score INT);

Screenshots of the project: https://drive.google.com/open?id=1-0j47nBvUPMBs-WYjvdAuetqTL4xX7Ck
