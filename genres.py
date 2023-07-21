ganres = '{"results":[{"genre":"Adventure"},{"genre":"Family"},{"genre":"Fantasy"},{"genre":"Crime"},{"genre":"Drama"},{"genre":"Comedy"},{"genre":"Animation"},{"genre":"Sci-Fi"},{"genre":"Sport"},{"genre":"Action"},{"genre":"Thriller"},{"genre":"Mystery"},{"genre":"Western"},{"genre":"Romance"},{"genre":"Biography"},{"genre":"Horror"},{"genre":"War"},{"genre":"Musical"},{"genre":"History"},{"genre":"Music"},{"genre":"Documentary"},{"genre":"Short"},{"genre":"Talk-Show"},{"genre":"Game-Show"},{"genre":"Reality-TV"},{"genre":"News"},{"genre":"Adult"}]}'

ganres_cleaned = ganres.replace("'", '"')

ganres_dict = eval(ganres_cleaned)

genres_data = [genre_data["genre"] for genre_data in ganres_dict["results"]]
