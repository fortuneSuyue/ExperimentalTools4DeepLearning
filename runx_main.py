from runx.logx import logx
from model.easyModel import EasyModel
from arguments import Args
import numpy
import torch
import numpy as np
import torch.optim as optim
from seedInitializer import randomSeedInitial


if __name__ == '__main__':
    args = Args()
    cfg = args.args
    logx.initialize(logdir='runx_logs/run1', coolname=True, tensorboard=True, hparams=cfg, eager_flush=True)
    # args.loadArgs(is_print=True)
    args.saveArgs()
    randomSeedInitial(cfg['seed'])
    # dataset
    x = torch.arange(16 * 10).view(16, 10).float()
    x = x + torch.rand_like(x) / 10
    y = x ** 2 + 1

    model = EasyModel().cuda()

    criterion = torch.nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001)

    best_loss = np.inf
    tmp_step = 0
    for epocn in range(10):
        losses = 0.0  # epochs training loss
        losses_valid = 0.0  # epoch validation loss
        for step, (x_, y_) in enumerate(zip(x, y)):
            tmp_step = step
            # data
            x_, y_ = x_.cuda().view(10, 1), y_.cuda().view(10, 1)
            x_train, y_train = x_[:5], y_[:5]
            x_val, y_val = x_[5:], y_[5:]
            # forward
            out = model(x_train)
            # loss
            loss_ = criterion(out, y_train)
            losses += loss_
            # backward
            optimizer.zero_grad()
            loss_.backward()
            optimizer.step()
            # valid
            with torch.no_grad():
                pred = model(x_val)
                valid_loss = criterion(pred, y_val)
                losses_valid += valid_loss

            metrics = {
                'loss': losses / (step + 1),
            }
            metrics_valid = {
                'loss': losses_valid / (step + 1)
            }
            logx.metric('train', metrics, epocn)
            logx.metric('val', metrics_valid, epocn)
        if losses_valid < best_loss:
            best_loss = losses_valid

        save_dict = {
            'state_dict': model.state_dict()
        }
        logx.save_model(save_dict, best_loss, epocn, higher_better=False, delete_old=True)

        logx.msg("epoch {}, train loss {:.6f}, valid loss {:.6f}".format(epocn, losses / (tmp_step + 1),
                                                                         losses_valid / (tmp_step+1)))








