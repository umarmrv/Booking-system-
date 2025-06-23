from database import connect
from notifier import send_notification





def is_cabinet_free(cabine_num, start, end):
     query = """
         SELECT * FROM bookings
         JOIN cabinet ON bookings.cabinet_id = cabinet.id
         WHERE cabinet.number = ?
         AND NOT (end_time <= ? OR start_time >= ?)
     """ 
     with connect() as conn:
        row = conn.execute(query, (cabine_num, start, end)).fetchone()
        return row is None, row
     

def book_cabinet(cabinet_number, user_name, email, phone, start, end):
    free, existing = is_cabinet_free(cabinet_number, start, end)
    if not free:
        return f"Кабинет уже занят {existing[3]} до {existing[6]}"
    with connect() as conn:
        cabinet_id = conn.execute("SELECT id FROM cabinet WHERE number=?", (cabinet_number,)).fetchone()[0]
        conn.execute("""
            INSERT INTO bookings (cabinet_id, user_name, email, phone, start_time, end_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (cabinet_id, user_name, email, phone, start, end))
    send_notification(email, phone, cabinet_number, start, end)
    return f"Бронирование успешно!"