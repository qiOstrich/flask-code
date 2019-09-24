from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Songs(db.Model):
    __tablename__ = 'SongList'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_name = db.Column(db.String(32), nullable=False)
    singer =db.Column(db.String(32), nullable=False)
    writer =db.Column(db.String(32))
    song_type=db.Column(db.String(16))
    duration=db.Column(db.Integer)

    def to_dict(self):
        return {
            'id':self.id,
            'song':self.song_name,
            'singer':self.singer,
            'writer':self.writer,
            'type':self.song_type,
            'duration':self.duration
        }