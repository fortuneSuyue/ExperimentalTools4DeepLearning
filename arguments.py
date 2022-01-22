from argparse import ArgumentParser
import json
import os


class Args:
    def __init__(self):
        parser = ArgumentParser(usage='hello', prog='test')
        parser.add_argument('--seed', type=int, default=256)
        parser.add_argument('--logdir', type=str, default='runx_logs')
        parser.add_argument('--argument', type=str, default='argument/commandline_args.txt')
        self.args = vars(parser.parse_args())

    def saveArgs(self, path=''):
        if path == '':
            path = self.args['argument']
        with open(path, 'w') as f:
            json.dump(self.args, f, indent=2)
        print('Sucessfully Saved!')

    def loadArgs(self, path='', is_print=False):
        if path == '':
            path = self.args['argument']
        with open(path, 'r') as f:
            self.args = json.load(f)
        if is_print:
            print(self.args)


if __name__ == '__main__':
    a = Args()
    print(a.args)
