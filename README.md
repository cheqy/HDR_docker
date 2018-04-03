# 远程大数据项目成果

关于本次项目最后需要提交的作业要求：将MNIST应用部署到容器里面，用户通过curl -XPOST命令提交带有手写体的数字图片，你的程序先将本图片识别出来，然后将识别的数字返回给用户。对MNIST中用户每次提交的图片、识别的文字和时间戳信息，都要记录到Cassandra以内。

依据个人的理解将本次项目分为以下四步，现对各步进行描述和重点提示：

- 用Python结合[mnist_deep.py](https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/examples/tutorials/mnist/mnist_deep.py)代码实现数字识别功能，该步的目标应为写好一个数字识别函数，使得输入一张图片后该函数就能快速返回一预测数值。
	> 注意：此步中对输入图片的读取以及返回预测值都比较容易实现，最重要的是对模型参数的存储与还原。毕竟我们需要给用户提供高质量且快速的服务，通过对模型参数的存储与还原，既能保留下高精度的优质参数参数，又避免了每次重复构建模型的时间浪费，相关函数为tf.train.Saver() ; 











远程大数据项目成果

容器相关: Dockerfile, app.py, requirements.txt, static(上传图片存放处), templates(网页模板) <br>
手写数字识别功能相关(参考mnist_deep.py): deep_run.py, deep_model_variable <br>
大数据存储功能相关: cassandra_run.py
