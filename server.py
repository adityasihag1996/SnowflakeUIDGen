from flask import Flask

from snowflake import SnowflakeGenerator
from config import DATA_CENTRE_ID, MACHINE_ID

app = Flask(__name__)

generator = SnowflakeGenerator(
    data_center_id = DATA_CENTRE_ID,
    machine_id = MACHINE_ID,
)

@app.route('/new_uid')
def get_id():
    try:
        snowflake_id = generator.get_id()
        return {'id': snowflake_id}, 200
    except Exception as e:
        # Handle the sequence overflow or any other exception
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug = True, port = 6969)
    