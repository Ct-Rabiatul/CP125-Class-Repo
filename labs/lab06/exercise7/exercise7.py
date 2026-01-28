def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):
    """
    Manages a music playlist with adds, imports, and removals.
    
    Args:
        current_playlist: Set of currently in playlist
        add_songs: List of songs to add individually
        import_playlist: Set of songs to import from Spotify
        banned_songs: Set of songs to remove
    
    Returns:
        int: Count of final songs in playlist
    """
    add_songs_set = set(add_songs)

    for song in add_songs_set:

        current_playlist.add(song)

    import_playlist.add(current_playlist())
    import_playlist.disacrd(banned_songs())
