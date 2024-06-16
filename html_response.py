def response(filename, prediction):
    """
    The response function takes the filename and prediction as arguments,
        and returns an HTML string that displays the image with its predicted label.


    :param filename: Get the name of the file that was uploaded
    :param prediction: Pass the prediction to the response function
    :return: A string of html code that is displayed in the browser
    :doc-author: Trelent
    """
    html = f"""
        <html>

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Convolutional Neural Network</title>
            <link rel="stylesheet" href="/static/styles/styles1.css">
            <link rel="stylesheet" href="/static/styles/styles3.css">
        </head>

        <body>
            <div class="container">
                <div class="imgs-container">
                    <img class="imgs"
                        src="/static/styles/cat.jpg"
                        alt="">
                </div>
                <h1>Image   Classification</h1>
                        
                        <p align="center"><img class="pos2" src="/static/upload/{filename}"></p>
                        <h2 align="center">{prediction}</h2>
                        <input type="button" onclick="history.back();" value="Повернутись на головну сторінку"/>
                <div class="imgs-container imgs-container-two">
                    <img class="imgs"
                        src="/static/styles/dog.jpg"
                        alt="">
        </body>

        </html>
        """

    return html
