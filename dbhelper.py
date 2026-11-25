
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=int(os.getenv("DB_PORT")),
                database=os.getenv("DB_NAME"),
                charset="utf8mb4",
                use_unicode=True,

                ssl_ca=os.getenv("DB_SSL_CA"),
                ssl_verify_cert=True,
                ssl_verify_identity=True
            )

            self.mycursor = self.conn.cursor()
            print("Connection successful")

        except mysql.connector.Error as err:
            print("Connection unsuccessful:", err)
            raise


    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
            SELECT DISTINCT(Source) FROM flights
            UNION
            SELECT DISTINCT(Destination) FROM flights
        """)
        data = self.mycursor.fetchall()
        for item in data :
            city.append(item[0])
        return city

    def fetch_all_flights(self, source, destination) :
        self.mycursor.execute("""
            SELECT Airline, Route, Dep_Time, Duration, Price FROM flights
            WHERE Source = '{}' AND Destination = '{}'
        """.format(source, destination))
        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self) :
        airline = []
        frequency = []
        self.mycursor.execute("""
            SELECT Airline, COUNT(*) FROM flights
            GROUP BY Airline
        """)
        data = self.mycursor.fetchall()

        for item in data :
            airline.append(item[0])
            frequency.append(item[1])
        return airline, frequency

    def busy_airport(self) :
        city = []
        frequency = []
        self.mycursor.execute("""
            SELECT Source, COUNT(*) FROM (SELECT Source FROM flights
							UNION ALL
							SELECT Destination FROM flights) t
            GROUP BY t.Source
            ORDER BY COUNT(*) DESC
        """)
        data = self.mycursor.fetchall()

        for item in data :
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency


    def daily_frequency(self) :
        date = []
        frequency = []
        self.mycursor.execute("""
            SELECT Date_of_Journey,COUNT(*) FROM flights
            GROUP BY Date_of_Journey
        """)
        data = self.mycursor.fetchall()

        for item in data :
            date.append(item[0])
            frequency.append(item[1])
        return date, frequency

