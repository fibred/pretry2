‧Practice_captcha
------------------

‧Dependencies
------------------
<ul>
<li><p>Python : 3.6.5</p></li>
<li><p>Tensorflow : 2.0</p></li>
<li><p>ImageCaptcha : 0.3</p></li>
<li><p>OpenCV : 4.1.1</p></li>
</ul>

‧Files
------------------
<p>1.Generate captcha images for pretrain:</p>

<pre><code>run a001_captcha_gen_.py
</code></pre>
<p>2.Get captcha images for target web:</p>

<pre><code>run a002_captcha_crawling.py
</code></pre>
<p>3.Load images and train model:</p>

<pre><code>run a003_train_model_.py
</code></pre>
<p>4.evaluate the accuracy of real test image:</p>

<pre><code>run a004_test_accuracy_.py
</code></pre>
