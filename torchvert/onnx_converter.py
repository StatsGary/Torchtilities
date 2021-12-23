import onnx
from onnx_tf.backend import prepare

def convert_pytorch_to_tf(model_path, output_path='./tf_conv.pb'):

    """Converts model from PyTorch to tensorflow

    Parameters
    ----------
    model_path : str
        The location of the PyTorch (.pth) file to be converted to Tensorflow
    output_path : str, optional
        Optional - defaults to tf_conv.pb: An output path to save the converted tensorflow model

    Returns
    -------
    list
        a list of the :
        - converted model object
        - Model graph 
        - Exported model graph to output path specified
    """
    print('[ONXX Conversion] Converting model from ONNX to tensorflow')

    if model_path:
        model_onnx = onnx.load(model_path)
        tf_rep = prepare(model_onnx)
        tf_rep.export_graph('./convnet.pb')
        print('[ONXX Conversion Completed]')
        return [model_onnx, tf_rep]
    else:
        raise Exception("Please specify the model file path and try again. \n This only works with .pth files.")