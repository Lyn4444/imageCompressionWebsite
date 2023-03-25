import tensorflow as tf
print(tf.config.list_physical_devices("GPU"))
print(tf.test.is_gpu_available())
print(tf.test.is_built_with_gpu_support())
print(tf.test.is_built_with_cuda())

#tensorflow 2.0 以上版本所用的测试代码
tf.compat.v1.disable_eager_execution()
a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
c = a + b
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
print(sess.run(c))

#tensorflow 2.0 以下版本所用的测试代码
a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
c = a + b
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
print(sess.run(c))
