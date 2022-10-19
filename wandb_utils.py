import datetime
import wandb

import constants


def generate_wandb_run_name(root):
    time_now = datetime.datetime.now()
    time_now_str = time_now.strftime(format='%Y-%m-%d_%H:%M:%S')
    out = root + '__' + time_now_str
    return out


def upload_as_wandb_artifact(run_group, item, item_name):

    run = wandb.init(project=constants.WANDB_PROJECT_NAME,
                     entity=constants.WANDB_USER_NAME,
                     name=generate_wandb_run_name(root=run_group),
                     group=run_group)

    artifact_name = 'art_' + item_name

    artifact = wandb.Artifact(name=artifact_name, type=run_group)
    artifact.add(item, item_name)
    run.log_artifact(artifact)
    run.finish()


def upload_df_as_wandb_artifact(run_group, df, item_name):
    table = wandb.Table(dataframe=df.reset_index())
    upload_as_wandb_artifact(run_group=run_group, item=table, item_name=item_name)
