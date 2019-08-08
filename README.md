### pretry2
-------------
practice_captcha_github


### Dependencies
-------------
>Python : 3.6.5<br> 
>Tensorflow : 1.9.0<br> 
>Keras : 2.1.3<br> 

    pip install tensorflow
    pip install opencv
    pip install requests
    pip shutil
    pip PIL


Download model.h5 file from : <br> 
https://drive.google.com/open?id=1LEidunJDabgK2KUrbaWxi8zIZiG0yhY7<br> 
Put model at path folder, set path and names list below at captcha_1.py:<br> 

    model_name = "0808_2"
    model_path = '../models/{}.h5'.format(model_name)
    IMGSAVEPATH = ''
    

Run captcha_1.py:<br> 
