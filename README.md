# exploring-spotify

## Resources

* [Spotify web API documentation](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)

* [Spotify API search](https://developer.spotify.com/documentation/web-api/reference/search)

* [Spotipy documentation](https://spotipy.readthedocs.io/en/latest/#)

* [Medium article with Spotipy overview](https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b)

## Useful queries

* `current_user_recently_played(limit=10)`
* `current_user_saved_tracks(limit=20)`
* `current_user_top_artists(limit=20,time_range='long_term')`
* `current_user_top_tracks(limit=20,time_range='long_term')`
* `devices()`
* `me()`
* `playlist_items(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', 'episode'))`
* `playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))`
* `recommendations(seed_artists=None, seed_genres=None, seed_tracks=None, limit=20, country=None, **kwargs)`
* `user()`
* `user_playlists(user, limit=50, offset=0)`