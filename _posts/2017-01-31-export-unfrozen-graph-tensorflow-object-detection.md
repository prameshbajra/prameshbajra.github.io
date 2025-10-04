---
layout: post
title:  "Export an unfrozen graph tensorflow - Object Detection"
date:   2019-08-14
description: "Export an unfrozen graph tensorflow - Object Detection"
keywords: "deploy, aws, sagemaker, model, object detection, sdk, tensorflow, graph, code, s3, programming"
categories: [aws, sagemaker, prediction, detection, tensorflow, tensorflow-serving, numpy, data, images, code, programming, deployment, s3, cloudwatch]
tags: [aws, sagemaker, prediction, detection, tensorflow, numpy, data, images, code, tensorflow-serving, programming, deployment, s3, cloudwatch]
icon: icon-google-developers
---

## Why?

Because the [offical tutorial for tensorflow object detection](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/exporting_models.md) only exports a frozen graph. These frozen graphs are all good for testing the model and some small prediction works but for production they are a huge pain to work with. Again, the documentation is not clear on what needs to be done in order to make this model production ready.

Here are something we need to know before continuing:

- We should have a surfacial understanding on [object detection using tensorflow](https://github.com/tensorflow/models/tree/master/research/object_detection) as this part comes only after our training is done and the checkpoint files are generated. More on this later.

- We need to know that **tensorflow** has a [tensorflow serving](https://github.com/tensorflow/serving) that allows one to production ready models. But these servings only take in unfrozen graph and in the documentaion (when this blog was written) it is not mentioned how to export a unfrozen graph. This is the main reason this blog exists.

- Exporting checkpoints to a graph are no where to be found and many ways do not work.

<br>
## Diving into Tensorflow directories:

Just a second, before diving into tensorflow directories in order to export an unfrozen graph we will need to have checkpoint files that gets generated from the output from training the model. These checkpoint files look something like:

```
output_path
    |__ model.ckpt-<checkpoint>.data-00000-of-00001
    |__ model.ckpt-<checkpoint>.index
    |__ model.ckpt-<checkpoint>.meta
```

The **checkpoint** will be a number that means how much steps it has been trained on. We can have many files like this. Just make sure to remember the highest number among all.

With that out of the way we can start changing the code for exporting the unforzen graph. 

Start by changing `exporter.py` file located in `models/research/object_detection/exporter.py`.
Replace the function `write_saved_model()` with this: 

```python
def write_saved_model(saved_model_path, trained_checkpoint_prefix, inputs,
                      outputs):
    """Writes SavedModel to disk.
  Args:
    saved_model_path: Path to write SavedModel.
    trained_checkpoint_prefix: path to trained_checkpoint_prefix.
    inputs: The input image tensor to use for detection.
    outputs: A tensor dictionary containing the outputs of a DetectionModel.
  """
    saver = tf.train.Saver()
    with session.Session() as sess:
        saver.restore(sess, trained_checkpoint_prefix)
        builder = tf.saved_model.builder.SavedModelBuilder(saved_model_path)

        tensor_info_inputs = {
            'inputs': tf.saved_model.utils.build_tensor_info(inputs)
        }
        tensor_info_outputs = {}
        for k, v in outputs.items():
            tensor_info_outputs[k] = tf.saved_model.utils.build_tensor_info(v)

        detection_signature = (
            tf.saved_model.signature_def_utils.build_signature_def(
                inputs=tensor_info_inputs,
                outputs=tensor_info_outputs,
                method_name=signature_constants.PREDICT_METHOD_NAME))

        builder.add_meta_graph_and_variables(
            sess,
            [tf.saved_model.tag_constants.SERVING],
            signature_def_map={
                signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
                detection_signature,
            },
        )
        builder.save()
```

Notice that there are some changes, the `frozen_graph_def` has been changed with `trained_checkpoint_prefix`. 

After this we also need to change the caller of this function:

Replace 

```python
write_saved_model(saved_model_path, frozen_graph_def, placeholder_tensor, outputs)
```

with 

```python
write_saved_model(saved_model_path, trained_checkpoint_prefix, placeholder_tensor, outputs)
```

<br>
## Done

It was simple, wasn't it? I still am not sure why tensorflow still doesn't provide this code or include this in their official github documentation. This could help a lot of people. Anyways, we are done here. All we have to do is run the same command we run when we need to export a graph.

The command would be something like :

```
# From directory tensorflow/models/research/

INPUT_TYPE=image_tensor
PIPELINE_CONFIG_PATH={path to pipeline config file}
TRAINED_CKPT_PREFIX={path to model.ckpt}
EXPORT_DIR={path to folder that will be used for export}
python object_detection/export_inference_graph.py \
    --input_type=${INPUT_TYPE} \
    --pipeline_config_path=${PIPELINE_CONFIG_PATH} \
    --trained_checkpoint_prefix=${TRAINED_CKPT_PREFIX} \
    --output_directory=${EXPORT_DIR}
```

It's obvious we have to provide our own path to the necessary files like **configs** and **directories**. Also, this might be a bit confusing but the **TRAINED_CKPT_PREFIX** is the number that I asked you to remember in the beginning of the blog.

<br>
## Verify

You can verify that the unfrozen graph has been exported by checking files under **saved_model/variables** directory. There should be files like :

```
saved_model
    |__ saved_model.pb
    |__ variables
            |__ variables.data-00000-of-00001
            |__ variables.index
```

Congratulations on getting the graph, but we did this for a reason. Making this model production ready. 

I have another blog that deploys the model to sagemaker to makes predictions. Make sure to go through [this](https://prameshbajra.github.io/aws/sagemaker/prediction/detection/tensorflow/numpy/data/images/code/programming/deployment/s3/cloudwatch/2019/12/13/deploy_in_sagemaker.html).


Let me know if you get stuck somewhere or you have any confusion. Drop me a mail or message me at twitter - [@prameshbajra](https://twitter.com/prameshbajra). I will help as much as I can. Thank you.