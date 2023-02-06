import wandb
import atexit
import uuid
import os

filename = f'/tmp/wandbbq_{str(uuid.uuid4()).replace("-", "")}.wandbbq'

def init(*args, **kwargs):
    def cleanup_fn():
        if os.path.exists(filename):
            print('Wandbbq: CLEANUP IN PROGRESS')
            tgt_dir = open(filename).read()
            os.remove(filename)
            command = f'wandb sync {tgt_dir}'
            if 'WANDBBQ_RELAY' in os.environ:
                command = 'ssh ' + os.environ['WANDBBQ_RELAY'] + ' ' + command
                print('Wandbbq: WILL USE RELAY ' + os.environ['WANDBBQ_RELAY'])
            os.system(command)
            print('Wandbbq: CLEANUP DONE')
    atexit.register(cleanup_fn)

    wandb.init(*args, **kwargs)
    if wandb.run.offline:
        with open(filename, 'a') as f:
            f.write(os.path.abspath(os.path.dirname(wandb.run.dir)))