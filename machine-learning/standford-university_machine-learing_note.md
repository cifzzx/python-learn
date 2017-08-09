# Machine Learning

## resume

standford university machine learning note

[coursera-machine learning](https://www.coursera.org/learn/machine-learning)

## content

- Supervised learning 监督学习
- unsupervised learning 非监督学习

## Supervised learning

在监督学习中，我们有一个数据集，并且知道正确的输出应该是怎样的，认为输入和输出应该是存在关系的。

监督学习问题可分为`回归问题`和`分类问题`。在回归问题中，我们尝试通过一连串的输出推测出结果，意思是我们试图将输入变量映射到某个连续函数；在分类问题中，相反的，我们试图在离散输出中预测结果。换句话说，我们试图将输入变量映射为离散类别。

### example1

给定有关房地产市场规模的数据，尝试预测它们的价格。价格作为大小的函数是连续的输出，所以这是一个回归问题。

我们可以将这个例子转换成分类问题，通过输出房子卖的价格是否多余问的价格，

### example2

- (a) 回归: 给一个人物照片，我们给予这张照片去推测出年龄
- (b) 分类: 一个患有肿瘤的患者，我们预测这个肿瘤是良性的还是恶性的

## unsupervised learning

无监督学习使我们能够解决问题，很少或根本不知道我们的结果应该是什么样子。我们可以从数据中提取结构，而我们并不知道变量的影响。


### example

- 聚类 

收集1000000个不同的基因，并找到一种方法，自动将这些基因分成不同的变量组，如寿命、位置、角色等。

- 非聚类

`鸡尾酒晚会算法`允许您在混乱的环境中找到结构。（在鸡尾酒会上从一片声音中辨别出个人的声音和音乐）