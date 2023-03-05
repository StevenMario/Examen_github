import web
import nav
import footer

from DB import Db
from list_artist import artist

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'artist' ##url vers la class artistes, à indiquer comme suivant href="/artist"
)

class index:
    def GET(self):
        d=Db()
        db=d.getDb()
        albums=db.select('Album',limit=10)
        artists=db.select('Artist', limit=10)
        playlists=db.select('Playlist',limit=10)
        genres=db.select('Genre',limit=10)
        tracks=db.select('Track',limit=10)
        result='<html><head><title>test</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.css"> '
        result += """
            <style>
                body{
                    background-image: url(https://images.pexels.com/photos/4813830/pexels-photo-4813830.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=loadhttps://images.pexels.com/photos/4813830/pexels-photo-4813830.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load);
                    background-size: 100% auto;
                    background-repeat:no-repeat;
                    min-height: 100vh;
                    display: flex;
                    flex-direction: column;
                }
                button{
                    margin-left:47%;
                    margin-top:10px;
                    width:200px;
                    padding:5px;
                    font-size:21px;
                    border-size:24px;
                }
                footer{
                    margin-top: auto;
                    width: 100%;
                }
                #welcome h1{
                    color:#ffff;
                    font-size:64px;
                    margin-left:45%;
                    margin-top:13%;
                }
            </style>
            <script>
               function hideButton() {
               var button = document.getElementsByTagName("button")[0];
               var text = document.getElementById("classement");
               var welcome = document.getElementById("welcome");
               button.style.display = "none";
               welcome.style.display = "none";
               classement.style.display = "block";      
               }
            </script>

        """
        result += '</head><body> '
        ##voici les liens
        result += nav.nav()
        result += """<div id="welcome"><h1>Bienvenue</h1></div>"""
        result += """<button class="btn btn-outline-info" onclick="hideButton()">Voir classement</button>"""
        result += '<div id="classement" style="display:none;">'
        result += '<br><br>'
        result += '<table border="1" class="table">'
        result += '<tr class="table-success"><th>Id_artists</th><th>Artiste</th><th>Album</th><th>Genre</th><th>Playlist</th></tr> '
        for album in albums:
            result += '<tr class="p-3 mb-2 bg-secondary text-white">'
            for artist in artists:
                result +='<td>'+str(artist.ArtistId)+'</td>'
                result +='<td>'+artist.Name+'</td>'
                break
            for playlist in playlists:
                result +='<td>'+playlist.Name+'</td>'
                break
            for genre in genres:
                result +='<td>'+genre.Name+'</td>'
                break
            result +='<td>'+album.Title+'</td>'           
            result += '</tr>'
        result += '</table>'
        result += '</div>'
        result += '</body>'        
        result += footer.footer()
        result += '</html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
