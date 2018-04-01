import logging

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "digit_recognition"

def createKeySpace():
    cluster = Cluster(contact_points=['172.17.0.1'], port=9021)
    session = cluster.connect()

    log.info("Creating keyspace...")
    try:
        session.execute("""
            CREATE KEYSPACE %s
            WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
            """ % KEYSPACE)

        log.info("setting keyspace...")
        session.set_keyspace(KEYSPACE)

        log.info("creating table...")
        session.execute("""
            CREATE TABLE managetable (
                time text PRIMARY KEY,
                image_name text,
                predict_number int
            )
            """)
    except Exception as e:
        log.error("Unable to create keyspace")
        log.error(e)

createKeySpace();

def insertData(time, image_name, predict_number):
    cluster = Cluster(contact_points=['172.17.0.1'], port=9021)
    session = cluster.connect()

    log.info("setting keyspace...")
    session.set_keyspace(KEYSPACE)

    prepared = session.prepare("""
    INSERT INTO managetable (time, image_name, predict_number)
    VALUES (?, ?, ?)
    """)

    log.info("inserting a row")
    session.execute(prepared.bind((time, image_name, predict_number)))



