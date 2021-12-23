import onnx
import tensorflow as tf
from onnx_tf.backend import prepare

def onnx_to_tf_model(path_to_serial_tf):

    """Reads and loads the serialised model graph from onnx to tf

    Parameters
    ----------
    model_path : str
        The location of the Tensorflow (.pb) file to be loaded
   
    Returns
    -------
    list
        a list of the :
        - model_graph
        - graph definition
        - Layer list saved into a list
    """
    print('[ONXX Conversion] Converting model from ONNX to tensorflow')
    graph_list=[]
    with tf.gile.GFile(path_to_serial_tf, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    with tf.Graph().as_default() as model_graph:
        tf.import_graph_definition(graph_def, name="")

    for op in model_graph.get_operations():
        print(op.values())
        graph_list.append(op.values())

    return [model_graph, graph_def, graph_list]