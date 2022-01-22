import math
import logging

from tensorboard_logger import Logger

if __name__ == '__main__':
    logging.root.handlers = []
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(message)s",
        handlers=[
            logging.FileHandler('tensorboard_logger_logs/test2/vv.log'),
            logging.StreamHandler()
        ])
    print = logging.info

    tb_logger = Logger(logdir='tensorboard_logger_logs/test2')
    for step in range(1, 1000):
        v1, v2 = math.log(1+1 / step), math.log(1+math.e / step)
        print(f'v1: {v1}, v2: {v2}')
        tb_logger.log_value('v1', v1, step)
        tb_logger.log_value('v2', v2, step)

# tensorboard --logdir tensorboard_logger_logs/test2 --port 1234
