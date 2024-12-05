import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from models.sleep_time import Sleep_time
from models.weight import Weight


#### global vars for this scipt ####
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=Config.SQLALCHEMY_TRACK_MODIFICATIONS)
Session = sessionmaker(bind=engine)
session = Session()
#### end global ####


def print_table(args):
    table = table_map[args.table]
    results = session.query(table).all()
    for r in results:
        print(r)
    print( '------------------------')
    print(f'number of results: {len(results)}')

def delete_by_id(args):
    table = table_map[args.table]
    entiry_id = args.id
    result = session.query(table).filter_by(id=entry_id).first()
    print(f'deleting {result}')
    session.delete(result)
    session.commit()

table_map = {
    'sleep_time': Sleep_time,
    'weight'    : Weight,
    }
cmd_map = {
    'print': print_table,
    'delete': delete_by_id,
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd',   type=str, help='command',   choices=[key for key in cmd_map])
    parser.add_argument('table', type=str, help='db table',  choices=[key for key in table_map])
    parser.add_argument('id',    type=int, help='entry id', nargs='?')

    args     = parser.parse_args()
    cmd      = args.cmd   # 0
    table    = args.table # 1
    entry_id = args.id    # 2

    f = cmd_map[cmd]
    f(args)
