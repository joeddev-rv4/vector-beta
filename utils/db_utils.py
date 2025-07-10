from datetime import datetime

async def return_data(data_form):
    rows = data_form.fetchall()
    data = [dict(row._mapping) for row in rows]
    return data

async def return_date():
    timestamp_6 = datetime.now()
    return timestamp_6