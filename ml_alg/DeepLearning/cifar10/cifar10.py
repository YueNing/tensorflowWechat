from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import sys
import tarfile

from six.moves import urllib
import tensorflow as tf 

import cifar10_input

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_integer('batch_size', 128, """ Number of images
					to process in a batch""")
tf.app.flags.DEFINE_string('data_dir', '/tmp/cifar10_data', """Path
					to the CIFAR-10 data directory""")
tf.app.flags.DEFINE_boolean('use_fp16', False, """Train the model us
					ing fp16.""")

IMAGE_SIZE = cifar10_input.IMAGE_SIZE
NUM_CLASSES = cifar10_input.NUM_CLASSES
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = cifar10_input.NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN
NUM_EXAMPLES_PER_EPOCH_FOR_EVAL = cifar10_input.NUM_EXAMPLES_PER_EPOCH_FOR_EVAL

MOVING_AVERAGE_DECAY = 0.9999


def _activation_summary(x):
    return

def _variable_on_cpu():
    return

def _variable_with_weight_decay():
    return

def distorted_inputs():
    return

def inputs(eval_data):
    return

def inference(images):
    return 

def loss():
    return

def _add_loss_summaries(total_loss):
    return

def train(total_loss, global_step):
    num_batches_per_epoch = NUM_EXAMPLES_PER_EPOCH_TRAIN /FLAGS.batch_size
    decay_steps = int(num_batchse_per_epoch * NUM_EPOCHS_PER_DECAY)
    
    lr = tf.train.exponential_decay(INITIAL_LEARNING_RATE, global_step, decay_steps, LEARNING_RATE_DECAY_FACTOR, staircase=True)
    tf.summary.scalar('learning_rate', lr)

    loss_averages_op = _add_loss_summaries(total_loss)

    with tf.control:dependencies([loss_averages_op]):
        opt = tf.train.GradientDescentOptimizer(lr)
        grads = opt.compute_gradients(total_loss)

    apply_gradient_op = opt.apply_gradients(grads, global_step=global_step)

    for var in tf.trainable_variables():
        tf.summary.histogram(var.op.name, var)

    for grad, var in grads:
        if grad is not None:
            tf.summary.histogram(var.op.name + '/gradients', grad)

    variable_averages = tf.train.ExponentialMovingAverage(

            )
    return 

def maybe_download_and_extract():
    return
