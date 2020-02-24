from pymysql import *

class database:
    conn = connect(host='localhost', database='world', user='system', password='abc123')

    def insert(self,name,current_score):
        cur=database.conn.cursor()
        cur.execute('SELECT player_id FROM ball_fall_players WHERE player_name="%s"'%(name))
        id=cur.fetchall()
        if id == tuple():
            cur.execute('INSERT INTO ball_fall_players (player_name,maximum_score,current_score) VALUES ("%s","%d","%d")' % (name, current_score,current_score))
        else:
            id=id[0][0]
            cur.execute('UPDATE ball_fall_players SET current_score="%d" WHERE player_id="%d"' %(current_score,id))
            cur.execute('SELECT maximum_score FROM ball_fall_players WHERE player_id="%d"'%(id))
            previous_maximum_score=cur.fetchall()
            previous_maximum_score=previous_maximum_score[0][0]
            if(previous_maximum_score<current_score):
                cur.execute('UPDATE ball_fall_players SET maximum_score="%d" WHERE player_id="%d"'%(current_score,id))
        database.conn.commit()

    def clear_data(self):
        cur = database.conn.cursor()
        cur.execute('TRUNCATE TABLE ball_fall_players')

    def get_max_score_players(self):
        cur = database.conn.cursor()
        cur.execute('SELECT player_name,maximum_score FROM ball_fall_players ORDER BY maximum_score DESC')
        maximum_score_players_tuple = cur.fetchall()
        return maximum_score_players_tuple