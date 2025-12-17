---
title: "Gradient-Based Learning Applied to Document Recognition"
authors: "Yann LeCun, Léon Bottou, Yoshua Bengio, Patrick Haffner"
year: 1998
field: "Machine Learning"
method: "Classification (Convolutional Neural Networks)"
arxiv: "http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf"
tags: ["classification", "mnist", "cnn", "supervised-learning", "computer-vision"]
date_reviewed: "2025-12-17"
---

# Summary

This paper introduces the MNIST handwritten digit dataset and demonstrates how gradient-based learning with convolutional neural networks can effectively solve image classification tasks. It established a standard benchmark for evaluating classification algorithms.

# Key Insights

- Convolutional Neural Networks can automatically learn hierarchical features from raw images.
- Gradient-based optimization enables end-to-end training without manual feature engineering.
- MNIST provides a clean, standardized benchmark for comparing classification models.

# Methodology

The authors use a convolutional neural network architecture consisting of convolutional layers, subsampling (pooling), and fully connected layers. The network is trained using backpropagation and gradient descent, with a softmax output layer for digit classification.

# Results

The proposed CNN achieves significantly higher accuracy on handwritten digit classification compared to traditional methods. The model demonstrates strong generalization across the MNIST test set.

# Strengths

- Introduced MNIST as a long-lasting benchmark dataset
- Clear demonstration of CNN effectiveness for classification
- End-to-end learning without handcrafted features

# Limitations

- Limited to simple grayscale images
- Small image resolution (28×28) compared to real-world tasks
- Does not address scalability to very deep architectures

# Personal Notes

This paper is ideal as a first classification reference. It clearly shows why neural networks outperform traditional methods when sufficient data is available. MNIST remains useful for rapid prototyping and sanity-checking new classification models.

# Code & Resources

- [Official MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- [PyTorch MNIST Example](https://github.com/pytorch/examples/tree/main/mnist)
