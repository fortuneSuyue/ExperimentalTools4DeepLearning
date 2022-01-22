from tensorboard.backend.event_processing import event_accumulator


if __name__ == '__main__':
    event = event_accumulator.EventAccumulator(r'tensorboard_logger_logs/test2/events.out.tfevents.1639531546.DESKTOP'
                                               r'-JCJIVK8')
    event.Reload()
    print(event.scalars.Keys())
    v1 = event.scalars.Items('v1')
    print(v1[0])
