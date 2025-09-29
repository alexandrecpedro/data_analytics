from collections.abc import Collection
from prettytable import PrettyTable

# ========== PART 1 - DICTIONARY OBJECT ==========
## (1.1) MUSIC DICTIONARY
music_dict = {"beatles": {"members": 4,
                           "bias": "George Harrisom",
                           "albuns": {"first": "Please Please Me",
                                      "peak_chart_position": {"UK": 1, "France": 5, "Germany": 5},
                                      "favorite_songs": ["Eleanor Rigby", "While My Guitar Gently Weeps"]},
                           "more_members_alive_than_dead": False,
                           (4, 5): "another random tuple"}}
music_dict_class = type(music_dict)
music_dict_class_name = music_dict_class.__name__
music_dict_id = id(music_dict)
music_dict_len = (len(music_dict) if isinstance(music_dict, Collection) else None)

# ========== PART 2 - DISPLAY THE RESULTS ==========
table = PrettyTable()
table.field_names = ["Description", "Value", "Object class", "Object class name", "ID (Object)", "Length (Object)"]
table.add_row(["Music Bands Dict", music_dict, music_dict_class, music_dict_class_name, music_dict_id, music_dict_len])

print(table)
