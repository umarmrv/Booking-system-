CREATE TABLE cabinet (
    id INTEGER PRIMARY KEY,
    number INTEGER NOT NULL UNIQUE
);


CREATE TABLE bookings (
    id INTEGER PRIMARY KEY,
    room_id INTEGER,
    user_name TEXT,
    email TEXT,
    phone TEXT,
    start_time TEXT,
    end_time TEXT,
    FOREIGN KEY (cabinet_id) REFERENCES cabinet(id)
);