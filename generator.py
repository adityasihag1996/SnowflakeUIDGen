from snowflake import SnowflakeGenerator
from config import DATA_CENTRE_ID, MACHINE_ID

# Example Usage
if __name__ == "__main__":
    generator = SnowflakeGenerator(DATA_CENTRE_ID, MACHINE_ID)

    for _ in range(5):
        id = generator.get_id()
        print(f"Generated Snowflake ID: {id}")
