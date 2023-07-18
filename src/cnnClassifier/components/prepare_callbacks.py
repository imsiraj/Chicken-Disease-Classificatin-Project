import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from cnnClassifier.entity.config_entity import PrepareCallbacksConfig

class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    #Enable visualizations for TensorBoard.
    @property
    def _create_tb_callbacks(self):                                                 
        try:
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
            tb_running_log_dir = os.path.join(
                                            self.config.tensorboard_root_log_dir,
                                            f"tb_logs_at_{timestamp}"
                                                )   
            return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
        except Exception as e:
            raise e
        
    #ModelCheckpoint callback is used in conjunction with training using model. fit() to save a model or weights (in a checkpoint file) //
    # at some interval, so the model or weights can be loaded later to continue the training from the state saved.    
    @property
    def _create_ckpt_callbacks(self):
        try:
            return tf.keras.callbacks.ModelCheckpoint(filepath = str(self.config.checkpoint_model_filepath),
                                                      save_best_only = True)
        except Exception as e:
            raise e


    def get_tb_ckpt_callbacks(self):
        try:
            return [self._create_tb_callbacks,self._create_ckpt_callbacks]
        except Exception as e:
            raise e