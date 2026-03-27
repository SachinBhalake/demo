import os
import time
import subprocess


def run_command(command):
    """
    Runs CLI command and returns result
    """
    return subprocess.run(
        command,
        capture_output=True,
        text=True
    )

def wait_for_video_complete(file_path, timeout=40, stable_time=3):
    """
    Wait until video file is created and fully written (size stops changing)
    """

    start_time = time.time()
    last_size = -1
    stable_counter = 0

    while time.time() - start_time < timeout:

        # Wait for file to appear
        if not os.path.exists(file_path):
            time.sleep(1)
            continue

        current_size = os.path.getsize(file_path)

        # Check if file size is stable
        if current_size > 0 and current_size == last_size:
            stable_counter += 1

            if stable_counter >= stable_time:
                return True
        else:
            stable_counter = 0

        last_size = current_size
        time.sleep(1)

    return False