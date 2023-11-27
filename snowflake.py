import time
import threading

class SnowflakeGenerator:
    def __init__(self, data_center_id, machine_id):
        # The epoch is typically the system start time. For this example, let's set it to 2023-11-06
        self.epoch = int(time.mktime(time.strptime('2023-11-06', '%Y-%m-%d')) * 1000)

        self.data_center_id = data_center_id
        self.machine_id = machine_id
        self.sequence = 0

        # Limits for bit lengths
        self.max_data_center_id = (1 << 5) - 1
        self.max_machine_id = (1 << 5) - 1
        self.max_sequence = (1 << 12) - 1

        # Shifts
        self.sequence_bits = 12
        self.machine_id_shift = self.sequence_bits
        self.data_center_id_shift = self.machine_id_shift + 5
        self.timestamp_shift = self.data_center_id_shift + 5

        # Thread safety
        self.lock = threading.Lock()
        self.last_timestamp = -1

        # Sanity check for data center and machine id
        if self.data_center_id > self.max_data_center_id or self.data_center_id < 0:
            raise ValueError(f"Data Center ID must be between 0 and {self.max_data_center_id}")
        if self.machine_id > self.max_machine_id or self.machine_id < 0:
            raise ValueError(f"Machine ID must be between 0 and {self.max_machine_id}")

    def _gen_current_time(self):
        """Get the current time in milliseconds."""
        return int(time.time() * 1000) - self.epoch

    def _next_millis(self, last_timestamp):
        """Wait for the next millisecond."""
        timestamp = self._gen_current_time()
        while timestamp <= last_timestamp:
            timestamp = self._gen_current_time()
        return timestamp

    def get_id(self):
        with self.lock:
            current_timestamp = self._gen_current_time()

            if current_timestamp < self.prev_timestamp:
                raise Exception("Clock is moving backwards. Rejecting requests until {}.".format(self.prev_timestamp))

            if self.prev_timestamp == current_timestamp:
                self.sequence = (self.sequence + 1)

                # Sequence Exhausted
                # wait till next millisecond OR Raise Exception
                if self.sequence > self.max_sequence:
                    # timestamp = self._next_millis(self.prev_timestamp)
                    raise Exception("Sequence overflow. Cannot generate ID.")
            else:
                self.sequence = 0

            self.prev_timestamp = current_timestamp

            snowflake_id = (current_timestamp << self.timestamp_shift) | \
                           (self.data_center_id << self.data_center_id_shift) | \
                           (self.machine_id << self.machine_id_shift) | \
                           self.sequence

            return snowflake_id


