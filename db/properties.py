import db
import mysql.connector
from app import appointment_info

data = appointment_info



# Schedule appointment
def schedule_appointments(user, meeting_info):
    conn = mysql.connector.connect(**db)
    cursor = conn.cursor()
    query = "INSERT INTO appointments (nombre, apellido, correo, telefono, hora, fecha, descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()
    return "The appointment was scheduled successfully"

