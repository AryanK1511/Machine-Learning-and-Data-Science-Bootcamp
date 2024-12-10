# Neural Networks

- **Convolutional Neural Network (CNN)** -> Good for image recognition
- **Long short-term memory network (LSTM)** -> Good for speech recognition

**Note:**

- GPUs are faster than CPUs for numerical computing because they are designed for massive parallelism, with thousands of smaller cores optimized to perform many calculations simultaneously. They use specialized hardware like Tensor Cores, have high memory bandwidth, and are built for throughput rather than low-latency tasks, making them ideal for data-intensive workloads like deep learning and simulations. In contrast, CPUs have fewer, more powerful cores optimized for sequential and general-purpose tasks, but they can't match the efficiency and speed of GPUs in parallel computation.
- Transfer learning allows you to use what one model know for another model.

**What are neural networks?**

- A neural network is a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates. In other words, neural networks are a subset of machine learning and are at the heart of deep learning algorithms. Their name and structure are inspired by the human brain, mimicking the way that biological neurons signal to one another.
- Neural networks consist of input and output layers, as well as (in most cases) a hidden layer or layers that are situated between the input and output. The layers are made up of nodes, or neurons, which have weighted connections to other neurons. A node combines input from the data with a set of coefficients, or weights, that either amplify or dampen that input, thereby assigning significance to inputs for the task the algorithm is trying to learn; e.g., which inputs are most important for predicting the output. The node then applies a transformation function to the weighted input, the result of which is passed on to the next layer.
- The network moves data through the layers to the output layer, where a prediction is made. The process of adjusting the weights of the connections in the network based on the prediction outcome is called training the neural network. This is typically done through a process known as backpropagation, where the difference between the output of the neural network and the desired output is computed and the weights are updated to minimize this difference.
- Neural networks are particularly good at performing complex tasks such as image recognition, speech recognition, and natural language processing. They have been used in a wide range of applications, from autonomous vehicles to medical diagnosis, financial analysis, and beyond.

**Use Cases:**

1. Classification
2. Sequence to sequence
3. Object Detection

Here’s a concise comparison of **GPU** (Graphics Processing Unit) and **TPU** (Tensor Processing Unit):

| **Feature**          | **GPU**                                                                          | **TPU**                                                                           |
| -------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Purpose**          | General-purpose parallel computing; excels at graphics and deep learning.        | Specialized for deep learning and machine learning workloads.                     |
| **Architecture**     | Optimized for general-purpose computation and a wide variety of tasks.           | Optimized specifically for TensorFlow operations (e.g., matrix multiplications).  |
| **Flexibility**      | More versatile; supports diverse workloads like gaming, video rendering, and AI. | Limited to machine learning tasks, particularly neural networks.                  |
| **Performance**      | Great for training and inference of models.                                      | Superior for large-scale AI training and inference, particularly with TensorFlow. |
| **Power Efficiency** | Consumes more power for equivalent workloads.                                    | More power-efficient for AI tasks.                                                |
| **Cost**             | Relatively expensive for large-scale deployment.                                 | More cost-effective for large AI deployments on Google Cloud.                     |

**Summary**:

- GPUs are versatile and widely used in AI, gaming, and other parallel computing tasks.
- TPUs are specialized for AI/ML workloads, particularly in TensorFlow, offering higher efficiency and scalability for deep learning.
