CREATE TABLE dim_location(location_key INTEGER PRIMARY KEY, location TEXT UNIQUE, commodity TEXT, region TEXT, country TEXT);
CREATE TABLE dim_provider(provider_key INTEGER PRIMARY KEY, provider TEXT UNIQUE);
CREATE TABLE dim_time(time_key INTEGER PRIMARY KEY, timestamp TEXT UNIQUE, date TEXT, hour INTEGER);
CREATE TABLE fact_price(location_key INTEGER REFERENCES dim_location, provider_key INTEGER REFERENCES dim_provider, time_key INTEGER REFERENCES dim_time, price REAL NOT NULL, unit TEXT, currency TEXT, PRIMARY KEY(location_key, time_key));
