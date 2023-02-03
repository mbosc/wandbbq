# WandBBQ Wandb Backup and Quit
Better APIs for good ole WandB

## Usage
+ Just import `wandbbq` and use `wandbbq.init` instead of `wandb.init`.  
+ If executing an offline run, upon program terination a `wandb sync` job will be launched to sync your run automatically.
+ If the env var `WANDBBQ_RELAY` is defined as `user@ip`, `wandb sync` will be executed over ssh on the provided relay (useful for computing clusters with no internet connection on compute nodes).

## Known Limits
+ The optional relay node must be capable of accessing the same wandb run folder at the same address.
+ No fallback if the sync node has no internet.
+ No upload of intermediate products (will implement sometimes later).