# 远程大数据项目成果

关于本次项目最后需要提交的作业要求：将MNIST应用部署到容器里面，用户通过curl -XPOST命令提交带有手写体的数字图片，你的程序先将本图片识别出来，然后将识别的数字返回给用户。对MNIST中用户每次提交的图片、识别的文字和时间戳信息，都要记录到Cassandra以内。

依据个人的理解将本次项目分为以下四步，现对各步进行描述和重点提示：

- 用Python结合[mnist_deep.py](https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/examples/tutorials/mnist/mnist_deep.py)代码实现数字识别功能，该步的目标应为写好一个数字识别函数，使得输入一张图片后该函数就能快速返回一预测数值。

	> 注意：<dr>
	1、此步中对输入图片的读取以及返回预测值是最基本的，我认为还需要做到的是对模型参数的存储与还原。毕竟我们需要给用户提供高质量且快速的服务，通过对模型参数的存储与还原，既能保留下高精度的优质参数，又避免了每次重复构建模型的时间浪费，相关函数为 tf.train.Saver() ; 
	2、还有一个在实现过程中可能会遇到的问题就是我们的项目需要能够多次提交图片进行数字识别即多次调用此数字识别函数，第一次调用成功第二次却失败了，我当时检查到的错误原因就是每次运行此函数时函数中参数都会被重新定义，且为了避免重名其会自动重命名，而重命名的参数并无法在储存的参数文件中找到对应值，故出现错误，如有此情况可以了解下用于清除默认图形堆栈并重置全局默认图形的函数 tf.reset_default_graph() 。

- 用Flask实现提供数字识别功能的网站，因为Flask是使用Python编写的web微框架，所以这个网站的核心功能我们已经在上一步实现了，此步所需要做的就是理解Flask并构建我们所需的网站框架。

	> 注意：Flask不是一个特别难以学习的东西，毕竟它的实现形式是我们熟悉且直观的网页
	[Flask官方文档](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application)就是很完善的学习资料，因为我们需要有一个用户提交待识别图片的功能，所以文档中File Uploads部分是重点，此部分最后还提供了有更好例子的[Uploading Files](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/#uploading-files)模式链接

- 把前两步完成的内容放在Docker里实现。

	> 注意：其实实现过程比较简单，

- 通过Docker方式将Cassandra容器拉到本地运行起来，将网页中用户每次提交的图片、识别的结果和时间戳信息都记录到Cassandra以内。

	> 注意：


<dr>
远程大数据项目成果

容器相关: Dockerfile, app.py, requirements.txt, static(上传图片存放处), templates(网页模板) <br>
手写数字识别功能相关(参考mnist_deep.py): deep_run.py, deep_model_variable <br>
大数据存储功能相关: cassandra_run.py
